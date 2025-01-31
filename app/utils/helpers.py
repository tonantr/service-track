from app.utils.constants import (
    ERROR_USER_NOT_FOUND,
    ERROR_NO_CARS_FOUND,
    ERROR_CAR_NOT_FOUND,
    ERROR_SERVICE_NOT_FOUND,
)


def load_user_and_cars(db_handler, username):
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
        print(f"{'ID':<5} {'Name':<20} {'Model':<20} {'Year':<10}")
        print("-" * 55)
        for car in cars:
            car_id = str(car["car_id"])
            name = str(car["name"])
            model = str(car["model"])
            year = str(car["year"])
            print(f"{car_id:<5} {name:<20} {model:<20} {year:<10}")
        print()

        return user, cars


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
        f"{'ID':<5} {'Service Type':<30} {'Service Date':<20} {'Next Service Date':<20} {'Notes':<50}"
    )
    print("-" * 125)

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
            str(service["notes"][:50]) + "..."
            if service["notes"] and len(service["notes"]) > 50
            else str(service["notes"]) or "N/A"
        )
        print(
            f"{service_id:<5} {service_type:<30} {service_date:<20} {next_service_date:<20} {notes:<50}"
        )

        service_dict[service_id] = service

    print()

    service_id_input = int(input("Enter the ID of the service: ").strip())

    selected_service = service_dict.get(service_id_input)

    if not selected_service:
        print(ERROR_SERVICE_NOT_FOUND)
        return

    return selected_service
