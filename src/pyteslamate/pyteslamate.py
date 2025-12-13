import logging
from datetime import datetime
from typing import Any
from urllib.parse import urljoin

from aiohttp import (
    ClientConnectorError,
    ClientError,
    ClientResponseError,
    ClientSession,
    ClientTimeout,
)
from pydantic import ValidationError

from pyteslamate.exceptions import (
    TeslamateAuthenticationError,
    TeslamateError,
    TeslamateNotFoundError,
    TeslamateRateLimitError,
    TeslamateServerError,
    TeslamateTimeoutError,
    TeslamateValidationError,
)
from pyteslamate.models import (
    CarBatteryHealth,
    CarCharge,
    CarCharges,
    CarDrive,
    CarDrives,
    Cars,
    CarStatus,
    CarUpdates,
    GlobalSettings,
)

logger = logging.getLogger(__name__)


class Teslamate:
    def __init__(
        self,
        base_url: str,
        api_key: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        session: ClientSession | None = None,
    ) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries
        self._session = session

    async def __aenter__(self) -> "Teslamate":
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        else:
            logger.warning("No API key provided; requests may be unauthorized.")

        timeout = ClientTimeout(total=self.timeout)
        self._session = ClientSession(base_url=self.base_url, headers=headers, timeout=timeout)
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if self._session and not self._session.closed:
            await self._session.close()
            logger.debug("Client session closed.")

    async def _request(
        self,
        method: str,
        endpoint: str,
        **kwargs: Any,
    ) -> Any:
        if not self._session:
            raise TeslamateError(
                "Client session not initialized. Use 'async with' context manager."
            )
        url = urljoin(self.base_url, endpoint)

        logger.debug(f"Making {method} request to {url}")

        try:
            async with self._session.request(method, url, **kwargs) as response:
                if response.status == 401:
                    raise TeslamateAuthenticationError("Authentication failed")
                elif response.status == 404:
                    raise TeslamateNotFoundError(f"Resource not found: {url}")
                elif response.status == 429:
                    raise TeslamateRateLimitError("Rate limit exceeded")
                elif 500 <= response.status < 600:
                    raise TeslamateServerError(f"Server error: {response.status}")

                response.raise_for_status()
                return await response.json()

        except ClientResponseError as e:
            raise TeslamateError(f"HTTP error: {e.status} {e.message}") from e
        except ClientConnectorError as e:
            raise TeslamateError(f"Connection error: {str(e)}") from e
        except TimeoutError:
            raise TeslamateTimeoutError("Request timeout")
        except ClientError as e:
            raise TeslamateError(f"Request failed: {str(e)}") from e

    async def get_cars(self) -> Cars:
        data = await self._request("GET", "cars")
        return Cars.model_validate(data)

    async def get_car(self, car_id: int) -> Cars:
        data = await self._request("GET", f"cars/{car_id}")
        return Cars.model_validate(data)

    async def get_car_battery_health(self, car_id: int) -> CarBatteryHealth:
        data = await self._request("GET", f"cars/{car_id}/battery-health")
        return CarBatteryHealth.model_validate(data)

    async def get_car_charges(
        self, car_id: int, start_date: datetime | None = None, end_date: datetime | None = None
    ) -> CarCharges:
        params: dict[str, str] = {}
        if start_date:
            params["startDate"] = start_date.isoformat()
        if end_date:
            params["endDate"] = end_date.isoformat()
        data = await self._request("GET", f"cars/{car_id}/charges", params=params or None)
        print(data)
        return CarCharges.model_validate(data)

    async def get_car_charge(self, car_id: int, charge_id: int) -> CarCharge:
        data = await self._request("GET", f"cars/{car_id}/charges/{charge_id}")
        return CarCharge.model_validate(data)

    async def get_car_drives(
        self,
        car_id: int,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
        min_distance: str | None = None,
        max_distance: str | None = None,
    ) -> CarDrives:
        params: dict[str, str] = {}
        if start_date:
            params["startDate"] = start_date.isoformat()
        if end_date:
            params["endDate"] = end_date.isoformat()
        if min_distance:
            params["minDistance"] = min_distance
        if max_distance:
            params["maxDistance"] = max_distance
        data = await self._request("GET", f"cars/{car_id}/drives", params=params or None)
        return CarDrives.model_validate(data)

    async def get_car_drive(self, car_id: int, drive_id: int) -> CarDrive:
        data = await self._request("GET", f"cars/{car_id}/drives/{drive_id}")
        return CarDrive.model_validate(data)

    async def get_car_status(self, car_id: int) -> CarStatus:
        try:
            data = await self._request("GET", f"cars/{car_id}/status")
            return CarStatus.model_validate(data)
        except ValidationError as e:
            raise TeslamateValidationError(f"Received invalid data for car status: {e}")

    async def get_car_updates(self, car_id: int) -> CarUpdates:
        data = await self._request("GET", f"cars/{car_id}/updates")
        return CarUpdates.model_validate(data)

    async def get_global_settings(self) -> GlobalSettings:
        data = await self._request("GET", "globalsettings")
        return GlobalSettings.model_validate(data)
