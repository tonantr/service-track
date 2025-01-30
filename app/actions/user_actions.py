import logging
from app.menu.menu import Menu
from app.auth.password_hashing import hash_password
from getpass import getpass
from app.utils.validation import validate_email, validate_date
from app.utils.constants import (
    ERROR_USER_NOT_FOUND,
    PRESS_ENTER_TO_GO_BACK,
    ERROR_NO_CARS_FOUND,
    ERROR_CAR_NOT_FOUND,
    ERROR_NO_SERVICES_FOUND,
)
from app.utils.helpers import load_user_and_cars, select_car_by_id

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(module)s - Line: %(lineno)d - %(message)s",
)


class UserActions:
    def __init__(self, db_handler, username):
        self.db_handler = db_handler
        self.username = username

    def view_profile(self):
        try:
            user = self.db_handler.load_user(self.username)
            if not user:
                print(ERROR_USER_NOT_FOUND)
                return

            print("\n*** User Details ***\n")
            print(f"Username: {user['username']}")
            print(f"Password: {'*' * 8}")
            print(f"Email: {user['email']}")
            print(f"Role: {user['role']}\n")

            input(PRESS_ENTER_TO_GO_BACK)
        except Exception as e:
            logging.error("Error in view_profile: %s", str(e))
            print("\nAn error occured while fetching your profile.\n")

    def change_password(self, current_password=None, new_password=None):
        try:
            if current_password is None:
                current_password = getpass("Enter current password: ")

            user = self.db_handler.load_user(self.username)
            if not user:
                print(ERROR_USER_NOT_FOUND)
                return

            if new_password is None:
                new_password = getpass("Enter new password: ")
                confirm_password = getpass("Confirm new password: ")
                if new_password != confirm_password:
                    print("\nError: Passwords do not match.\n")
                    return

            if len(new_password) < 4:
                print("\nError: Password must be at least 4 characters long.\n")
                return

            hashed_password = hash_password(new_password)

            self.db_handler.update_password(self.username, hashed_password)
            print("\nPassword updated successfully.\n")
            print("For security reasons, you will be logged out.")
            return "logout"
        except Exception as e:
            logging.error("Error in change_password: %s", str(e))
            print("\nAn error occurred while updating the password.\n")

    def update_email(self, new_email=None):
        try:
            user = self.db_handler.load_user(self.username)
            if not user:
                print(ERROR_USER_NOT_FOUND)
                return

            print(f"Current email: {user['email']}")
            if new_email is None:
                new_email = input("Enter new email: ")

            if not validate_email(new_email):
                print("\nError: Invalid email.\n")
                return

            existing_email = self.db_handler.load_user_by_email(new_email)
            if existing_email:
                print("\nError: Email already exists.\n")
                return

            self.db_handler.update_email(self.username, new_email)
            print("\nEmail updated successfully.\n")
        except Exception as e:
            logging.error("Error in update_email: %s", str(e))
            print("\nAn error occurred while updating the email.\n")
        finally:
            input(PRESS_ENTER_TO_GO_BACK)

    def view_cars(self):
        try:
            user, cars = load_user_and_cars(self.db_handler, self.username)
            if not cars:
                return

            input(PRESS_ENTER_TO_GO_BACK)
        except Exception as e:
            logging.error("Error in view_cars: %s", str(e))
            print("\nAn error occurred while fetching your cars.\n")

    def add_car(self):
        try:
            print("\n*** Add Car ***\n")
            car_name = Menu.get_name_car()
            if not car_name:
                print("Error: Car name cannot be empty.")
                return

            car_model = Menu.get_model_car()
            if not car_model:
                print("Error: Car model cannot be empty.")
                return

            car_year = Menu.get_year_car()
            if not car_year:
                print("Error: Car year is invalid.")
                return

            user = self.db_handler.load_user(self.username)
            if not user:
                print(ERROR_USER_NOT_FOUND)
                return

            # Option 1: Check for duplicates manually by loading all cars for the user

            # existing_car = self.db_handler.load_cars(user["user_id"])
            # for car in existing_car:
            #     if (
            #         car["name"].lower() == car_name.lower()
            #         and car["model"].lower() == car_model.lower()
            #     ):
            #         print(
            #             f"\nError: The name '{car_name}' and model '{car_model}' already exists.\n"
            #         )
            #         return

            # self.db_handler.add_car(car_name, car_model, car_year, user["user_id"])
            # print("\nCar added successfully.\n")

            # Option 2: Check for duplicates using a database query

            duplicate_car = self.db_handler.find_car_by_name_and_model(
                user["user_id"], car_name, car_model
            )
            if duplicate_car:
                print(
                    f"\nError: The name '{car_name}' and model '{car_model}' already exists.\n"
                )
            else:
                self.db_handler.add_car(car_name, car_model, car_year, user["user_id"])
                print("\nCar added successfully.\n")

        except Exception as e:
            logging.error("Error in add_car: %s", str(e))
            print("\nAn error occurred while adding the car.\n")

    def edit_car(self):
        try:
            user, cars = load_user_and_cars(self.db_handler, self.username)
            if not user or not cars:
                return

            selected_car = select_car_by_id(cars)
            if not selected_car:
                return

            print(
                f"\nSelected Car: {selected_car['name']} (ID: {selected_car["car_id"]})\n"
            )
            print("Which fields would you like to update?")
            print("1. Name")
            print("2. Model")
            print("3. Year")
            print("4. Cancel\n")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                name = Menu.get_name_car()
                if not name:
                    print("\nError: Name cannot be empty.\n")
                    return

                if self.db_handler.find_car_by_name_and_model(
                    user["user_id"], name, selected_car["model"]
                ):
                    print(
                        f"\nError: The name '{name}' and model '{selected_car["model"]}' already exists.\n"
                    )
                    return

                self.db_handler.update_car(selected_car["car_id"], name=name)
                print("\nName updated successfully.\n")
            elif choice == "2":
                model = Menu.get_model_car()
                if not model:
                    print("\nError: Model cannot be empty.\n")
                    return

                if self.db_handler.find_car_by_name_and_model(
                    user["user_id"], selected_car["name"], model
                ):
                    print(
                        f"\nError: The name '{selected_car["name"]}' and model '{model}' already exists.\n"
                    )
                    return

                self.db_handler.update_car(selected_car["car_id"], model=model)
                print("\nModel updated successfully.\n")
            elif choice == "3":
                year = Menu.get_year_car()
                if not year:
                    print("\nError: Year cannot be empty or invalid.\n")
                    return

                self.db_handler.update_car(selected_car["car_id"], year=year)
                print("\nYear updated successfully.\n")
            elif choice == "4":
                print("\nCancelled.\n")
                return
            else:
                print("\nError: Invalid choice.\n")
                return

        except Exception as e:
            logging.error("Error in edit_car: %s", str(e))
            print("\nAn error occurred while editing the car.\n")

    def delete_car(self):
        try:
            user, cars = load_user_and_cars(self.db_handler, self.username)
            if not cars:
                return

            selected_car = select_car_by_id(cars)
            if not selected_car:
                return

            print(
                f"\nSelected Car: {selected_car['name']} (ID: {selected_car["car_id"]})\n"
            )

            if not Menu.confirm_action("delete this car? (y/n): "):
                print("\nCancelled.\n")
                return

            self.db_handler.delete_car_and_related_services(selected_car["car_id"])
            print("\nCar deleted successfully.\n")
        except Exception as e:
            logging.error("Error in delete_car: %s", str(e))
            print("\nAn error occurred while deleting the car.\n")

    def list_services(self):
        try:
            user, cars = load_user_and_cars(self.db_handler, self.username)
            if not user or not cars:
                return

            print("\nPlease select a car from your list to view its services:\n")

            selected_car = select_car_by_id(cars)
            if not selected_car:
                return

            print(
                f"\nSelected Car: {selected_car['name']} (ID: {selected_car['car_id']})\n"
            )

            services = self.db_handler.load_services(selected_car["car_id"])
            if not services:
                print(ERROR_NO_SERVICES_FOUND)
                return

            print("\n*** Services for Selected Car ***\n")
            print(
                f"{'Car Name':<20} {'Service Type':<30} {'Service Date':<20} {'Next Service Date':<20} {'Notes':<50}"
            )
            print("-" * 140)
            for service in services:
                car_name = str(service["car_name"]) or "N/A"
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
                    f"{car_name:<20} {service_type:<30} {service_date:<20} {next_service_date:<20} {notes:<50}"
                )
            print()
            input(PRESS_ENTER_TO_GO_BACK)

        except Exception as e:
            logging.error("Error in list_services: %s", str(e))
            print("\nAn error occurred while listing the services.\n")

    def add_service(self):
        try:
            user, cars = load_user_and_cars(self.db_handler, self.username)
            if not user or not cars:
                return

            print("\n*** Select a Car to Add Services ***\n")

            selected_car = select_car_by_id(cars)
            if not selected_car:
                return

            print(
                f"\nSelected Car: {selected_car['name']} (ID: {selected_car['car_id']})"
            )

            service_type = Menu.get_service_type()
            if not service_type:
                return

            service_date = Menu.get_service_date()
            if not service_date:
                return
            if not validate_date(service_date):
                print("\nError: Invalid date format. Please use YYYY-MM-DD.\n")
                return

            next_service_date = Menu.get_next_service_date()
            if not validate_date(next_service_date):
                print("\nError: Invalid date format. Please use YYYY-MM-DD.\n")
                return

            notes = Menu.get_notes()
            if not notes:
                return
            if not Menu.confirm_action("add this service? (y/n): "):
                print("\nCancelled.\n")
                return
            self.db_handler.add_service(
                service_type=service_type,
                service_date=service_date,
                next_service_date=next_service_date or None,
                notes=notes,
                car_id=selected_car["car_id"],
            )
            print("\nService added successfully.\n")
        except Exception as e:
            logging.error("Error in add_service: %s", str(e))
            print("\nAn error occurred while adding the service.\n")

    def update_service(self):
        try:
            print()
        except Exception as e:
            logging.error("Error in update_service: %s", str(e))
            print("\nAn error occurred while updating the service.\n")
