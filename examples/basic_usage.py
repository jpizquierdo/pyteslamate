"""Basic usage example of the API client."""

import asyncio
import logging
from datetime import datetime

from pyteslamate import Teslamate, TeslamateError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main() -> None:
    """Demonstrate basic API client usage."""
    # Initialize the client
    async with Teslamate(
        base_url="http://192.168.250.9:8079/api/v1/",
        timeout=30.0,
    ) as client:
        try:
            # Get all cars
            logger.info("Fetching cars...")
            cars = await client.get_cars()
            logger.info(cars)
            #            Get a single car
            logger.info("Fetching car 1...")
            car = await client.get_car(1)
            logger.info(car)
            logger.info("Fetching car 1 battery health..")
            car_batt_health = await client.get_car_battery_health(1)
            logger.info(car_batt_health)
            logger.info("Fetching car 1 charges..")
            car_charges = await client.get_car_charges(1)
            logger.info(car_charges)

            logger.info("Fetching car 1 charges from 01/12/2025 to 08/12/2025")
            car_charges = await client.get_car_charges(
                1, start_date=datetime(2025, 12, 1), end_date=datetime(2025, 12, 8)
            )
            logger.info(car_charges)

            logger.info("Fetching car 1 charge 111")
            car_charge = await client.get_car_charge(car_id=1, charge_id=111)
            logger.info(car_charge)

            logger.info("Fetching car 1 drives")
            car_drives = await client.get_car_drives(car_id=1)
            logger.info(car_drives)

            logger.info("Fetching car 1 drive 1441")
            car_drive = await client.get_car_drive(car_id=1, drive_id=1441)
            logger.info(car_drive)

            logger.info("Fetching car 1 status")
            car_status = await client.get_car_status(car_id=1)
            logger.info(car_status)

            logger.info("Fetching car 1 updates")
            car_updates = await client.get_car_updates(car_id=1)
            logger.info(car_updates)

            logger.info("Fetching global settings")
            global_settings = await client.get_global_settings()
            logger.info(global_settings)
            car_current_charge = await client.get_current_car_charge(car_id=1)
            logger.info(car_current_charge)

        except TeslamateError as e:
            logger.error("API error occurred: %s", e.message)


if __name__ == "__main__":
    asyncio.run(main())
