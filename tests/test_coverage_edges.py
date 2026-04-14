"""Targeted tests for uncovered branches and validators."""

# These tests intentionally exercise internal client branches and use small
# helper stubs, so a few production-oriented pylint rules are too strict here.
# pylint: disable=missing-function-docstring,protected-access,too-few-public-methods

from __future__ import annotations

from copy import deepcopy
from datetime import datetime
from types import TracebackType
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest
from aiohttp import ClientConnectorError, ClientError, ClientResponseError, ClientSession
from aioresponses import aioresponses

from pyteslamate.exceptions import (
    TeslamateAuthenticationError,
    TeslamateError,
    TeslamateNotFoundError,
    TeslamateRateLimitError,
    TeslamateServerError,
    TeslamateTimeoutError,
)
from pyteslamate.models import CarStatus
from pyteslamate.pyteslamate import Teslamate
from tests.response_examples import CAR_STATUS_PAYLOAD


class _RaiseOnEnter:
    """Async context manager that raises when entered."""

    def __init__(self, exc: Exception) -> None:
        self.exc = exc

    async def __aenter__(self) -> None:
        raise self.exc

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool:
        return False


class _FakeSession:
    """Minimal session stub for exercising request error paths."""

    def __init__(self, exc: Exception) -> None:
        self.closed = False
        self._exc = exc

    def request(self, _method: str, _url: str, **_kwargs: object) -> _RaiseOnEnter:
        return _RaiseOnEnter(self._exc)


class _ClosedSession:
    """Minimal closed session stub for exit-path tests."""

    def __init__(self) -> None:
        self.closed = True
        self.close = AsyncMock()


@pytest.mark.asyncio
async def test_context_manager_without_api_key_logs_warning(
    base_url: str, caplog: pytest.LogCaptureFixture
) -> None:
    client = Teslamate(base_url=base_url)

    async with client:
        assert client._session is not None
        assert "Authorization" not in client._session.headers

    assert "No API key provided" in caplog.text


@pytest.mark.asyncio
async def test_request_requires_initialized_session(base_url: str) -> None:
    client = Teslamate(base_url=base_url, api_key="test")

    with pytest.raises(TeslamateError, match="Client session not initialized"):
        await client._request("GET", "cars")


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("status", "expected_exception", "message"),
    [
        (401, TeslamateAuthenticationError, "Authentication failed"),
        (404, TeslamateNotFoundError, "Resource not found"),
        (429, TeslamateRateLimitError, "Rate limit exceeded"),
        (500, TeslamateServerError, "Server error: 500"),
    ],
)
async def test_request_status_specific_errors(
    base_url: str,
    status: int,
    expected_exception: type[Exception],
    message: str,
) -> None:
    async with Teslamate(base_url=base_url, api_key="test") as client:
        with aioresponses() as mocked:
            mocked.get(f"{base_url}/cars", status=status)

            with pytest.raises(expected_exception, match=message):
                await client._request("GET", "cars")


@pytest.mark.asyncio
async def test_request_wraps_timeout_as_teslamate_timeout(base_url: str) -> None:
    client = Teslamate(base_url=base_url, api_key="test")
    client._session = cast(ClientSession, _FakeSession(TimeoutError()))

    with pytest.raises(TeslamateTimeoutError, match="Request timeout"):
        await client._request("GET", "cars")


@pytest.mark.asyncio
async def test_request_wraps_client_errors(base_url: str) -> None:
    client = Teslamate(base_url=base_url, api_key="test")
    client._session = cast(ClientSession, _FakeSession(ClientError("boom")))

    with pytest.raises(TeslamateError, match="Request failed: boom"):
        await client._request("GET", "cars")


@pytest.mark.asyncio
async def test_request_wraps_client_response_error(base_url: str) -> None:
    client = Teslamate(base_url=base_url, api_key="test")
    client._session = cast(
        ClientSession,
        _FakeSession(
            ClientResponseError(
                request_info=MagicMock(),
                history=(),
                status=418,
                message="teapot",
            )
        ),
    )

    with pytest.raises(TeslamateError, match="HTTP error: 418 teapot"):
        await client._request("GET", "cars")


@pytest.mark.asyncio
async def test_request_wraps_connection_error(base_url: str) -> None:
    client = Teslamate(base_url=base_url, api_key="test")
    client._session = cast(
        ClientSession,
        _FakeSession(
            ClientConnectorError(
                connection_key=MagicMock(),
                os_error=OSError("network down"),
            )
        ),
    )

    with pytest.raises(TeslamateError, match="Connection error:"):
        await client._request("GET", "cars")


@pytest.mark.asyncio
async def test_exit_skips_close_when_session_already_closed(base_url: str) -> None:
    client = Teslamate(base_url=base_url, api_key="test")
    session = cast(ClientSession, _ClosedSession())
    client._session = session

    await client.__aexit__(None, None, None)

    close_mock = cast(AsyncMock, client._session.close)
    close_mock.assert_not_awaited()


@pytest.mark.parametrize(
    ("raw_value", "expected"),
    [
        ("0000-12-31T23:59:59", None),
        ("not-a-date", None),
        (datetime(2025, 1, 1, 12, 0, 0), datetime(2025, 1, 1, 12, 0, 0)),
        (123, None),
    ],
)
def test_scheduled_charging_start_time_validator_special_cases(
    raw_value: object,
    expected: datetime | None,
) -> None:
    payload = deepcopy(CAR_STATUS_PAYLOAD.model_dump(mode="json"))
    payload["data"]["status"]["charging_details"]["scheduled_charging_start_time"] = raw_value

    result = CarStatus.model_validate(payload)

    assert result.data.status.charging_details.scheduled_charging_start_time == expected


def test_scheduled_charging_start_time_validator_parses_iso_string() -> None:
    payload = deepcopy(CAR_STATUS_PAYLOAD.model_dump(mode="json"))
    payload["data"]["status"]["charging_details"]["scheduled_charging_start_time"] = (
        "2025-01-01T12:00:00"
    )

    result = CarStatus.model_validate(payload)

    assert result.data.status.charging_details.scheduled_charging_start_time == datetime(
        2025, 1, 1, 12, 0, 0
    )
