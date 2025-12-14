"""Unit tests for the Teslamate client using mocked responses."""

# pylint: disable=missing-function-docstring
from datetime import datetime
from urllib.parse import urlencode

import pytest
from aioresponses import aioresponses

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
from pyteslamate.pyteslamate import Teslamate
from tests.response_examples import (
    CAR_BATTERY_HEALTH_PAYLOAD,
    CAR_CHARGE_PAYLOAD,
    CAR_CHARGES_PAYLOAD,
    CAR_DRIVE_PAYLOAD,
    CAR_DRIVES_PAYLOAD,
    CAR_STATUS_PAYLOAD,
    CAR_UPDATES_PAYLOAD,
    CARS_PAYLOAD,
    GLOBAL_SETTINGS_PAYLOAD,
)


@pytest.mark.asyncio
async def test_get_cars_success(teslamate_client: Teslamate, base_url: str) -> None:
    url = f"{base_url}/cars"

    with aioresponses() as mocked:
        mocked.get(url, status=200, body=CARS_PAYLOAD.model_dump_json())
        cars = await teslamate_client.get_cars()

    assert isinstance(cars, Cars)
    assert cars.model_dump() == CARS_PAYLOAD.model_dump()


@pytest.mark.asyncio
async def test_get_car_by_id_success(teslamate_client: Teslamate, base_url: str) -> None:
    url = f"{base_url}/cars/1"

    with aioresponses() as mocked:
        mocked.get(url, status=200, body=CARS_PAYLOAD.model_dump_json())
        cars = await teslamate_client.get_car(1)

    assert isinstance(cars, Cars)
    assert cars.model_dump() == CARS_PAYLOAD.model_dump()


@pytest.mark.asyncio
async def test_get_car_battery_health_success(teslamate_client: Teslamate, base_url: str) -> None:
    url = f"{base_url}/cars/1/battery-health"

    with aioresponses() as mocked:
        mocked.get(url, status=200, body=CAR_BATTERY_HEALTH_PAYLOAD.model_dump_json())
        car_battery_health = await teslamate_client.get_car_battery_health(1)

    assert isinstance(car_battery_health, CarBatteryHealth)
    assert car_battery_health.model_dump() == CAR_BATTERY_HEALTH_PAYLOAD.model_dump()


@pytest.mark.asyncio
async def test_get_car_charges_all_success(teslamate_client: Teslamate, base_url: str) -> None:
    url = f"{base_url}/cars/1/charges"

    with aioresponses() as mocked:
        mocked.get(url, status=200, body=CAR_CHARGES_PAYLOAD.model_dump_json())
        car_charges = await teslamate_client.get_car_charges(1)
    assert isinstance(car_charges, CarCharges)
    assert car_charges.model_dump() == CAR_CHARGES_PAYLOAD.model_dump()


@pytest.mark.asyncio
async def test_get_car_charges_range_date_success(
    teslamate_client: Teslamate, base_url: str
) -> None:
    start = datetime(2025, 5, 1)
    end = datetime(2025, 5, 15)
    query = urlencode(
        {
            "startDate": start.isoformat(),
            "endDate": end.isoformat(),
        }
    )
    url = f"{base_url}/cars/1/charges?{query}"

    with aioresponses() as mocked:
        mocked.get(url, status=200, body=CAR_CHARGES_PAYLOAD.model_dump_json())
        car_charges = await teslamate_client.get_car_charges(1, start_date=start, end_date=end)
    assert isinstance(car_charges, CarCharges)
    assert car_charges.model_dump() == CAR_CHARGES_PAYLOAD.model_dump()


@pytest.mark.asyncio
async def test_get_car_charge_by_id_success(teslamate_client: Teslamate, base_url: str) -> None:
    url = f"{base_url}/cars/1/charges/111"

    with aioresponses() as mocked:
        mocked.get(url, status=200, body=CAR_CHARGE_PAYLOAD.model_dump_json())
        car_charge = await teslamate_client.get_car_charge(1, charge_id=111)
    assert isinstance(car_charge, CarCharge)
    assert car_charge.model_dump() == CAR_CHARGE_PAYLOAD.model_dump()


@pytest.mark.asyncio
async def test_get_car_drives_success(teslamate_client: Teslamate, base_url: str) -> None:
    start = datetime(2025, 5, 1)
    end = datetime(2025, 12, 15)
    min_distance = "1"
    max_distance = "200"
    query = urlencode(
        {
            "startDate": start.isoformat(),
            "endDate": end.isoformat(),
            "minDistance": min_distance,
            "maxDistance": max_distance,
        }
    )
    url = f"{base_url}/cars/1/drives?{query}"

    with aioresponses() as mocked:
        mocked.get(url, status=200, body=CAR_DRIVES_PAYLOAD.model_dump_json())
        car_drives = await teslamate_client.get_car_drives(
            1, start_date=start, end_date=end, min_distance=min_distance, max_distance=max_distance
        )
    assert isinstance(car_drives, CarDrives)
    assert car_drives.model_dump() == CAR_DRIVES_PAYLOAD.model_dump()


@pytest.mark.asyncio
async def test_get_car_drive_by_id_success(teslamate_client: Teslamate, base_url: str) -> None:
    url = f"{base_url}/cars/1/drives/1441"

    with aioresponses() as mocked:
        mocked.get(url, status=200, body=CAR_DRIVE_PAYLOAD.model_dump_json())
        car_drive = await teslamate_client.get_car_drive(1, drive_id=1441)
    assert isinstance(car_drive, CarDrive)
    assert car_drive.model_dump() == CAR_DRIVE_PAYLOAD.model_dump()


@pytest.mark.asyncio
async def test_get_car_status_success(teslamate_client: Teslamate, base_url: str) -> None:
    url = f"{base_url}/cars/1/status"

    with aioresponses() as mocked:
        mocked.get(url, status=200, body=CAR_STATUS_PAYLOAD.model_dump_json())
        car_status = await teslamate_client.get_car_status(1)
    assert isinstance(car_status, CarStatus)
    assert car_status.model_dump() == CAR_STATUS_PAYLOAD.model_dump()


@pytest.mark.asyncio
async def test_get_car_updates_success(teslamate_client: Teslamate, base_url: str) -> None:
    url = f"{base_url}/cars/1/updates"

    with aioresponses() as mocked:
        mocked.get(url, status=200, body=CAR_UPDATES_PAYLOAD.model_dump_json())
        car_updates = await teslamate_client.get_car_updates(1)
    assert isinstance(car_updates, CarUpdates)
    assert car_updates.model_dump() == CAR_UPDATES_PAYLOAD.model_dump()


@pytest.mark.asyncio
async def test_get_global_settings_success(teslamate_client: Teslamate, base_url: str) -> None:
    url = f"{base_url}/globalsettings"

    with aioresponses() as mocked:
        mocked.get(url, status=200, body=GLOBAL_SETTINGS_PAYLOAD.model_dump_json())
        global_settings = await teslamate_client.get_global_settings()
    assert isinstance(global_settings, GlobalSettings)
    assert global_settings.model_dump() == GLOBAL_SETTINGS_PAYLOAD.model_dump()
