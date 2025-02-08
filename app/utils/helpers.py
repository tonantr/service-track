from app.utils.constants import (
    ERROR_USER_NOT_FOUND,
    ERROR_NO_CARS_FOUND,
    ERROR_CAR_NOT_FOUND,
    ERROR_SERVICE_NOT_FOUND,
    ERROR_NO_SERVICES_FOUND,
    PRESS_ENTER_TO_GO_BACK,
)
import os
import requests


def load_user_and_cars(db_handler, username):
    try:
        user = db_handler.load_user(username)
        if not user:
            print(ERROR_USER_NOT_FOUND)
            return None, None

        cars = db_handler.load_cars(user["user_id"])
        if not cars:
            print(ERROR_NO_CARS_FOUND)
            return user, None
        else:
            print("\n*** List of Cars ***\n")
            print(f"{'ID':<5} {'Name':<20} {'Model':<20} {'Year':<10} {'VIN':<20}")
            print("-" * 80)
            for car in cars:
                car_id = str(car["car_id"])
                name = str(car["name"])
                model = str(car["model"])
                year = str(car["year"])
                vin = str(car["vin"])
                print(f"{car_id:<5} {name:<20} {model:<20} {year:<10} {vin:<20}")
            print()

            return user, cars
    except Exception as e:
        print(f"\nError loading user or cars: {e}\n")
        return None, None


def select_car_by_id(cars):
    car_id = input("Enter the ID of the car: ").strip()
    if not car_id.isdigit():
        print("\nError: Invalid ID.\n")
        return None
    car_id = int(car_id)
    for car in cars:
        if car["car_id"] == car_id:
            return car

    print(ERROR_CAR_NOT_FOUND)
    return None


def get_selected_service(services):
    print("\n*** Services for Selected Car ***\n")
    print(
        f"{'ID':<5} {'Service Type':<30} {'Service Date':<20} {'Next Service Date':<20} {'Notes':<30}"
    )
    print("-" * 105)

    service_dict = {}

    for service in services:
        service_id = service["service_id"]
        service_type = (
            str(service["service_type"][:30] + "...")
            if len(service["service_type"]) > 30
            else str(service["service_type"])
        )
        service_date = str(service["service_date"]) or "N/A"
        next_service_date = str(service["next_service_date"]) or "N/A"
        notes = (
            str(service["notes"][:30]) + "..."
            if service["notes"] and len(service["notes"]) > 30
            else str(service["notes"]) or "N/A"
        )
        print(
            f"{service_id:<5} {service_type:<30} {service_date:<20} {next_service_date:<20} {notes:<30}"
        )

        service_dict[service_id] = service

    print()

    service_id_input = int(input("Enter the ID of the service: ").strip())

    selected_service = service_dict.get(service_id_input)

    if not selected_service:
        print(ERROR_SERVICE_NOT_FOUND)
        return

    return selected_service


def get_downloads_folder():
    if os.name == "nt":  # Windows
        return os.path.join(os.environ["USERPROFILE"], "Downloads")
    else:  # macOS/Linux
        return os.path.join(os.path.expanduser("~"), "Downloads")


def get_car_by_vin(db_handler, vin, user_id=None):
    try:
        vin = vin.upper()
        if user_id:
            car = db_handler.load_user_car_by_vin(user_id, vin)
        else:
            car = db_handler.load_cars_by_vin(vin)

        if not car:
            print(ERROR_CAR_NOT_FOUND)
            return None

        print(f"\nID: {car['car_id']}")
        print(f"Name: {car['name']}")
        print(f"Model: {car['model']}")
        print(f"Year: {car['year']}")

        user_input = input("\nPress Enter to view services or type 'back': ")
        if user_input == "back":
            return

        services = db_handler.load_services_by_car_id(car["car_id"])

        if not services:
            print(ERROR_NO_SERVICES_FOUND)
        else:
            print("\n*** Service History ***\n")
            print(
                f"{'ID':<10} {'Mileage':<10} {'Service Type':<30} {'Service Date':<20} {'Next Service Date':<20} {'Cost':<10} {'Notes':<30}"
            )
            print("-" * 140)
            for service in services:
                service_id = service["service_id"]
                mileage = str(service.get("mileage", "N/A")).strip()
                service_type = str(service.get("service_type", "N/A")).strip()
                service_date = str(service.get("service_date", "N/A")).strip()
                next_service_date = str(service.get("next_service_date", "N/A")).strip()
                cost = str(service.get("cost", "N/A")).strip()
                notes = str(service.get("notes", "N/A")).strip()

                service_type = (
                    service_type[:27] + "..."
                    if len(service_type) > 30
                    else service_type
                )
                notes = notes[:27] + "..." if len(notes) > 30 else notes

                print(
                    f"{service_id:<10} {mileage:<10} {service_type:<30} {service_date:<20} {next_service_date:<20} {cost:<10} {notes:<30}"
                )

            print("\n*** FOR FULL DETAILS, EXPORT TO A CSV FILE! ***\n")

            input(PRESS_ENTER_TO_GO_BACK)

    except Exception as e:
        print(f"\nError loading car: {e}\n")
        return None
