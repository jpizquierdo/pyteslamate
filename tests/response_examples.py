"""Test response example fixtures for unit tests."""

from pyteslamate.models import (
    CarBatteryHealth,
    CarCharge,
    CarChargeCurrent,
    CarCharges,
    CarDrive,
    CarDrives,
    Cars,
    CarsChargesCurrentError,
    CarStatus,
    CarUpdates,
    GlobalSettings,
)

CARS_PAYLOAD = Cars.model_validate(
    {
        "data": {
            "cars": [
                {
                    "car_id": 1,
                    "name": "Tesli",
                    "car_details": {
                        "eid": 123456789,
                        "vid": 123456789,
                        "vin": "FANCYVIN12345",
                        "model": "3",
                        "trim_badging": "50",
                        "efficiency": 0.13732,
                    },
                    "car_exterior": {
                        "exterior_color": "PearlWhite",
                        "spoiler_type": "None",
                        "wheel_type": "Glider18",
                    },
                    "car_settings": {
                        "suspend_min": 12,
                        "suspend_after_idle_min": 15,
                        "req_not_unlocked": False,
                        "free_supercharging": False,
                        "use_streaming_api": True,
                    },
                    "teslamate_details": {
                        "inserted_at": "2024-04-19T16:25:06+02:00",
                        "updated_at": "2024-08-20T15:29:20+02:00",
                    },
                    "teslamate_stats": {
                        "total_charges": 295,
                        "total_drives": 1423,
                        "total_updates": 38,
                    },
                }
            ]
        }
    }
)
CAR_BATTERY_HEALTH_PAYLOAD = CarBatteryHealth.model_validate(
    {
        "data": {
            "car": {"car_id": 1, "car_name": "Tesli"},
            "battery_health": {
                "max_range": 437.9637776632106,
                "current_range": 423.94736842105266,
                "max_capacity": 60.24955555555555,
                "current_capacity": 58.903896678023614,
                "rated_efficiency": 13.7,
                "battery_health_percentage": 97.76652480649236,
            },
            "units": {"unit_of_length": "km", "unit_of_temperature": "C"},
        }
    }
)

CAR_CHARGES_PAYLOAD = CarCharges.model_validate(
    {
        "data": {
            "car": {"car_id": 1, "car_name": "Tesli"},
            "charges": [
                {
                    "charge_id": 207,
                    "start_date": "2025-05-14T06:55:36+02:00",
                    "end_date": "2025-05-14T12:58:36+02:00",
                    "address": "The Moon",
                    "charge_energy_added": 38.7,
                    "charge_energy_used": 40.3,
                    "cost": 6.05,
                    "duration_min": 363,
                    "duration_str": "06:03",
                    "battery_details": {"start_battery_level": 35, "end_battery_level": 100},
                    "range_ideal": {"start_range": 150.44, "end_range": 432.41},
                    "range_rated": {"start_range": 150.44, "end_range": 432.41},
                    "outside_temp_avg": 16.7,
                    "odometer": 22677.025078,
                    "latitude": 41.59372,
                    "longitude": -4.507798,
                },
                {
                    "charge_id": 206,
                    "start_date": "2025-05-08T06:57:57+02:00",
                    "end_date": "2025-05-08T09:40:59+02:00",
                    "address": "The Moon",
                    "charge_energy_added": 17.34,
                    "charge_energy_used": 18.12,
                    "cost": 2.72,
                    "duration_min": 163,
                    "duration_str": "02:43",
                    "battery_details": {"start_battery_level": 72, "end_battery_level": 100},
                    "range_ideal": {"start_range": 306.0, "end_range": 432.41},
                    "range_rated": {"start_range": 306.0, "end_range": 432.41},
                    "outside_temp_avg": 15.4,
                    "odometer": 22405.854064,
                    "latitude": 41.593624,
                    "longitude": -4.507771,
                },
            ],
            "units": {"unit_of_length": "km", "unit_of_temperature": "C"},
        }
    }
)

CAR_CHARGE_PAYLOAD = CarCharge.model_validate(
    {
        "data": {
            "car": {"car_id": 1, "car_name": "Tesli"},
            "charge": {
                "charge_id": 111,
                "start_date": "2024-10-01T17:01:27+02:00",
                "end_date": "2024-10-01T17:23:53+02:00",
                "address": "Lidl-Bucaramanga",
                "charge_energy_added": 3.8,
                "charge_energy_used": 4.03,
                "cost": 0.0,
                "duration_min": 22,
                "duration_str": "00:22",
                "battery_details": {"start_battery_level": 29, "end_battery_level": 35},
                "range_ideal": {"start_range": 123.65, "end_range": 151.33},
                "range_rated": {"start_range": 123.65, "end_range": 151.33},
                "outside_temp_avg": 26.5,
                "odometer": 12317.597585,
                "latitude": 40.4719,
                "longitude": -3.634852,
                "charge_details": [
                    {
                        "detail_id": 61772,
                        "date": "2024-10-01T17:01:27+02:00",
                        "battery_level": 29,
                        "usable_battery_level": 29,
                        "charge_energy_added": 0.0,
                        "not_enough_power_to_heat": None,
                        "charger_details": {
                            "charger_actual_current": 3,
                            "charger_phases": 2,
                            "charger_pilot_current": 16,
                            "charger_power": 1,
                            "charger_voltage": 231,
                        },
                        "battery_info": {
                            "ideal_battery_range": 123.65,
                            "rated_battery_range": 123.65,
                            "battery_heater": False,
                            "battery_heater_on": False,
                            "battery_heater_no_power": None,
                        },
                        "conn_charge_cable": "IEC",
                        "fast_charger_info": {
                            "fast_charger_present": False,
                            "fast_charger_brand": "<invalid>",
                            "fast_charger_type": "<invalid>",
                        },
                        "outside_temp": 26.5,
                    },
                    {
                        "detail_id": 61773,
                        "date": "2024-10-01T17:01:32+02:00",
                        "battery_level": 29,
                        "usable_battery_level": 29,
                        "charge_energy_added": 0.0,
                        "not_enough_power_to_heat": None,
                        "charger_details": {
                            "charger_actual_current": 6,
                            "charger_phases": 2,
                            "charger_pilot_current": 16,
                            "charger_power": 3,
                            "charger_voltage": 230,
                        },
                        "battery_info": {
                            "ideal_battery_range": 123.65,
                            "rated_battery_range": 123.65,
                            "battery_heater": False,
                            "battery_heater_on": False,
                            "battery_heater_no_power": None,
                        },
                        "conn_charge_cable": "IEC",
                        "fast_charger_info": {
                            "fast_charger_present": False,
                            "fast_charger_brand": "<invalid>",
                            "fast_charger_type": "<invalid>",
                        },
                        "outside_temp": 26.5,
                    },
                ],
            },
            "units": {"unit_of_length": "km", "unit_of_temperature": "C"},
        }
    }
)


CAR_DRIVES_PAYLOAD = CarDrives.model_validate(
    {
        "data": {
            "car": {"car_id": 1, "car_name": "Tesli"},
            "drives": [
                {
                    "drive_id": 1555,
                    "start_date": "2025-12-11T19:57:31+01:00",
                    "end_date": "2025-12-11T20:18:46+01:00",
                    "start_address": "Street Velazquez, Madrid",
                    "end_address": "Casa",
                    "odometer_details": {
                        "odometer_start": 31286.291098,
                        "odometer_end": 31295.707487,
                        "odometer_distance": 9.416388999998162,
                    },
                    "duration_min": 21,
                    "duration_str": "00:21",
                    "speed_max": 87,
                    "speed_avg": 26.90396857142332,
                    "power_max": 86,
                    "power_min": -49,
                    "battery_details": {
                        "start_usable_battery_level": 80,
                        "start_battery_level": 80,
                        "end_usable_battery_level": 76,
                        "end_battery_level": 77,
                        "reduced_range": True,
                        "is_sufficiently_precise": True,
                    },
                    "range_ideal": {
                        "start_range": 344.74,
                        "end_range": 331.48,
                        "range_diff": 13.26,
                    },
                    "range_rated": {
                        "start_range": 344.74,
                        "end_range": 331.48,
                        "range_diff": 13.26,
                    },
                    "outside_temp_avg": 8.8,
                    "inside_temp_avg": 21.5,
                    "energy_consumed_net": 1.8208632,
                    "consumption_net": 193.37170543829012,
                },
                {
                    "drive_id": 1554,
                    "start_date": "2025-12-11T17:58:30+01:00",
                    "end_date": "2025-12-11T18:22:09+01:00",
                    "start_address": "Casa",
                    "end_address": "Street Velazquez, Madrid",
                    "odometer_details": {
                        "odometer_start": 31278.566246,
                        "odometer_end": 31286.258486,
                        "odometer_distance": 7.692240000000311,
                    },
                    "duration_min": 24,
                    "duration_str": "00:24",
                    "speed_max": 60,
                    "speed_avg": 19.230600000000777,
                    "power_max": 33,
                    "power_min": -46,
                    "battery_details": {
                        "start_usable_battery_level": 82,
                        "start_battery_level": 82,
                        "end_usable_battery_level": 80,
                        "end_battery_level": 81,
                        "reduced_range": True,
                        "is_sufficiently_precise": True,
                    },
                    "range_ideal": {"start_range": 355.36, "end_range": 348.81, "range_diff": 6.55},
                    "range_rated": {"start_range": 355.36, "end_range": 348.81, "range_diff": 6.55},
                    "outside_temp_avg": 14.9,
                    "inside_temp_avg": 22.1,
                    "energy_consumed_net": 0.899446,
                    "consumption_net": 116.92900897527426,
                },
            ],
            "units": {"unit_of_length": "km", "unit_of_temperature": "C"},
        }
    }
)

CAR_DRIVE_PAYLOAD = CarDrive.model_validate(
    {
        "data": {
            "car": {"car_id": 1, "car_name": "Tesli"},
            "drive": {
                "drive_id": 1441,
                "start_date": "2025-10-21T17:20:07+02:00",
                "end_date": "2025-10-21T17:57:43+02:00",
                "start_address": "The Moon",
                "end_address": "King's Castle, Madrid",
                "odometer_details": {
                    "odometer_start": 29910.945715,
                    "odometer_end": 29937.858422,
                    "odometer_distance": 26.9127069999995,
                },
                "duration_min": 38,
                "duration_str": "00:38",
                "speed_max": 113,
                "speed_avg": 42.49374789473605,
                "power_max": 143,
                "power_min": -63,
                "battery_details": {
                    "start_usable_battery_level": 100,
                    "start_battery_level": 100,
                    "end_usable_battery_level": 94,
                    "end_battery_level": 95,
                    "reduced_range": True,
                    "is_sufficiently_precise": True,
                },
                "range_ideal": {"start_range": 433.57, "end_range": 409.98, "range_diff": 23.59},
                "range_rated": {"start_range": 433.57, "end_range": 409.98, "range_diff": 23.59},
                "outside_temp_avg": 21.8,
                "inside_temp_avg": 22.3,
                "energy_consumed_net": 3.2393788,
                "consumption_net": 120.36614525621893,
                "drive_details": [
                    {
                        "detail_id": 4691723,
                        "date": "2025-10-21T17:20:07+02:00",
                        "latitude": 21.874135,
                        "longitude": -8.913827,
                        "speed": 0,
                        "power": 1,
                        "odometer": 29910.945715,
                        "battery_level": 100,
                        "usable_battery_level": None,
                        "elevation": 603.0,
                        "climate_info": {
                            "inside_temp": None,
                            "outside_temp": None,
                            "is_climate_on": None,
                            "fan_status": None,
                            "driver_temp_setting": None,
                            "passenger_temp_setting": None,
                            "is_rear_defroster_on": None,
                            "is_front_defroster_on": None,
                        },
                        "battery_info": {
                            "est_battery_range": None,
                            "ideal_battery_range": None,
                            "rated_battery_range": None,
                            "battery_heater": None,
                            "battery_heater_on": None,
                            "battery_heater_no_power": None,
                        },
                    },
                    {
                        "detail_id": 4691724,
                        "date": "2025-10-21T17:20:07+02:00",
                        "latitude": 11.813135,
                        "longitude": -1.275827,
                        "speed": 0,
                        "power": 1,
                        "odometer": 29910.95742,
                        "battery_level": 100,
                        "usable_battery_level": 100,
                        "elevation": None,
                        "climate_info": {
                            "inside_temp": 21.8,
                            "outside_temp": 20.5,
                            "is_climate_on": True,
                            "fan_status": 1,
                            "driver_temp_setting": 22.0,
                            "passenger_temp_setting": 22.0,
                            "is_rear_defroster_on": False,
                            "is_front_defroster_on": False,
                        },
                        "battery_info": {
                            "est_battery_range": 510.37,
                            "ideal_battery_range": 433.57,
                            "rated_battery_range": 433.57,
                            "battery_heater": False,
                            "battery_heater_on": False,
                            "battery_heater_no_power": None,
                        },
                    },
                ],
            },
            "units": {"unit_of_length": "km", "unit_of_temperature": "C"},
        }
    }
)

CAR_STATUS_PAYLOAD = CarStatus.model_validate(
    {
        "data": {
            "car": {"car_id": 1, "car_name": "Tesli"},
            "status": {
                "display_name": "Tesli",
                "state": "offline",
                "state_since": "2025-12-12T08:03:38+01:00",
                "odometer": 31295.71,
                "car_status": {
                    "healthy": True,
                    "locked": True,
                    "sentry_mode": False,
                    "windows_open": False,
                    "doors_open": False,
                    "driver_front_door_open": False,
                    "driver_rear_door_open": False,
                    "passenger_front_door_open": False,
                    "passenger_rear_door_open": False,
                    "trunk_open": False,
                    "frunk_open": False,
                    "is_user_present": False,
                    "center_display_state": 0,
                },
                "car_details": {"model": "3", "trim_badging": "50"},
                "car_exterior": {
                    "exterior_color": "PearlWhite",
                    "spoiler_type": "None",
                    "wheel_type": "Glider18",
                },
                "car_geodata": {
                    "geofence": "King's Castle",
                    "location": {"latitude": 22.87154, "longitude": -1.854736},
                    "latitude": 22.87154,
                    "longitude": -1.854736,
                },
                "car_versions": {
                    "version": "2025.44.3",
                    "update_available": True,
                    "update_version": "2025.44.25.1",
                },
                "driving_details": {
                    "active_route": {
                        "destination": "",
                        "energy_at_arrival": 0.0,
                        "distance_to_arrival": 0.0,
                        "minutes_to_arrival": 0,
                        "traffic_minutes_delay": 0,
                        "location": {"latitude": 0.0, "longitude": 0.0},
                    },
                    "active_route_destination": "",
                    "active_route_latitude": 0.0,
                    "active_route_longitude": 0.0,
                    "shift_state": "P",
                    "power": 0,
                    "speed": 0,
                    "heading": 355,
                    "elevation": 683,
                },
                "climate_details": {
                    "is_climate_on": False,
                    "inside_temp": 16.1,
                    "outside_temp": 14.5,
                    "is_preconditioning": False,
                    "climate_keeper_mode": "off",
                },
                "battery_details": {
                    "est_battery_range": 389.33,
                    "rated_battery_range": 330.75,
                    "ideal_battery_range": 330.75,
                    "battery_level": 77,
                    "usable_battery_level": 76,
                },
                "charging_details": {
                    "plugged_in": False,
                    "charging_state": "disconnected",
                    "charge_energy_added": 52.16,
                    "charge_limit_soc": 100,
                    "charge_port_door_open": False,
                    "charger_actual_current": 0,
                    "charger_phases": 0,
                    "charger_power": 0,
                    "charger_voltage": 1,
                    "charge_current_request": 16,
                    "charge_current_request_max": 16,
                    "scheduled_charging_start_time": None,
                    "time_to_full_charge": 12.1,
                },
                "tpms_details": {
                    "tpms_pressure_fl": 2.8,
                    "tpms_pressure_fr": 2.75,
                    "tpms_pressure_rl": 2.8,
                    "tpms_pressure_rr": 2.65,
                    "tpms_soft_warning_fl": False,
                    "tpms_soft_warning_fr": False,
                    "tpms_soft_warning_rl": False,
                    "tpms_soft_warning_rr": True,
                },
            },
            "units": {
                "unit_of_length": "km",
                "unit_of_temperature": "C",
                "unit_of_pressure": "bar",
            },
        }
    }
)

CAR_UPDATES_PAYLOAD = CarUpdates.model_validate(
    {
        "data": {
            "car": {"car_id": 1, "car_name": "Tesli"},
            "updates": [
                {
                    "update_id": 2,
                    "start_date": "2024-04-19T18:51:14+02:00",
                    "end_date": "2024-04-19T19:07:45+02:00",
                    "version": "2024.8.9 0cac3042b6cd",
                },
                {
                    "update_id": 1,
                    "start_date": "2024-04-19T16:25:07+02:00",
                    "end_date": "2024-04-19T16:25:07+02:00",
                    "version": "2023.44.200 2fa4e3cb0681",
                },
            ],
        }
    }
)


GLOBAL_SETTINGS_PAYLOAD = GlobalSettings.model_validate(
    {
        "data": {
            "settings": {
                "setting_id": 1,
                "account_info": {
                    "inserted_at": "2024-04-13T11:51:28+02:00",
                    "updated_at": "2024-10-25T14:12:58+02:00",
                },
                "teslamate_units": {"unit_of_length": "km", "unit_of_temperature": "C"},
                "teslamate_webgui": {"preferred_range": "rated", "language": "es"},
                "teslamate_urls": {
                    "base_url": "https://teslamate.domain.com",
                    "grafana_url": "https://teslamate-grafana.domain.com",
                },
            }
        }
    }
)

CAR_CHARGE_CURRENT_PAYLOAD = CarChargeCurrent.model_validate(
    {
        "data": {
            "car": {"car_id": 1, "car_name": "Tesli"},
            "charge": {
                "charge_id": 111,
                "start_date": "2024-04-19T18:51:14+02:00",
                "is_charging": True,
                "address": "Lidl",
                "charge_energy_added": 52.16,
                "cost": 0.0,
                "duration_min": 15,
                "duration_str": "00:15",
                "battery_details": {"start_battery_level": 29, "current_battery_level": 35},
                "rated_range": {
                    "start_range": 123.65,
                    "current_range": 151.33,
                    "added_range": 27.68,
                },
                "outside_temp_avg": 26.5,
                "odometer": 12317.597585,
                "charge_details": [
                    {
                        "detail_id": 61772,
                        "date": "2024-04-19T18:51:14+02:00",
                        "battery_level": 29,
                        "usable_battery_level": 29,
                        "charge_energy_added": 0.0,
                        "not_enough_power_to_heat": None,
                        "charger_details": {
                            "charger_actual_current": 3,
                            "charger_phases": 2,
                            "charger_pilot_current": 16,
                            "charger_power": 1,
                            "charger_voltage": 231,
                        },
                        "battery_info": {
                            "ideal_battery_range": 123.65,
                            "rated_battery_range": 123.65,
                            "battery_heater": False,
                            "battery_heater_on": False,
                            "battery_heater_no_power": None,
                        },
                        "conn_charge_cable": "IEC",
                        "fast_charger_info": {
                            "fast_charger_present": False,
                        },
                        "outside_temp": 26.5,
                    },
                ],
            },
            "units": {
                "unit_of_length": "km",
                "unit_of_temperature": "C",
            },
        }
    }
)

CAR_CHARGE_CURRENT_ERROR_PAYLOAD = CarsChargesCurrentError.model_validate(
    {"error": "No active charging in progress."}
)
