import logging
import csv
import os
from app.menu.menu import Menu
from app.auth.password_hashing import hash_password
from getpass import getpass
from app.utils.validation import validate_email, validate_date
from app.utils.constants import (
    ERROR_USER_NOT_FOUND,
    PRESS_ENTER_TO_GO_BACK,
    ERROR_NO_SERVICES_FOUND,
)
from app.utils.helpers import (
    load_user_and_cars,
    select_car_by_id,
    get_selected_service,
    get_downloads_folder,
    get_car_by_vin
)

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
            print(f"Username: {user.get('username', 'Not available')}")
            print(f"Email: {user.get('email', 'Not available')}")
            print(f"Role: {user.get('role', 'Not available')}\n")

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
                return

            car_model = Menu.get_model_car()
            if not car_model:
                return

            car_year = Menu.get_year_car()
            if not car_year:
                return
            
            car_vin = Menu.get_vin_car()
            if not car_vin:
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
                self.db_handler.add_car(car_name, car_model, car_year, car_vin, user["user_id"])
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
                f"{'Car Name':<10} {'Mileage':<10} {'Service Type':<30} {'Service Date':<20} {'Next Service Date':<20} {'Cost':<10} {'Notes':<30}"
            )
            print("-" * 140)
            for service in services:
                car_name = str(service.get("car_name", "N/A")).strip()
                mileage = str(service.get("mileage", "N/A")).strip()
                service_type = str(service.get("service_type", "N/A")).strip()
                service_date = str(service.get("service_date", "N/A")).strip()
                next_service_date = str(service.get("next_service_date", "N/A")).strip()
                cost = str(service.get("cost", "N/A")).strip()
                notes = str(service.get("notes", "N/A")).strip()

                service_type = service_type[:27] + "..." if len(service_type) > 30 else service_type
                notes = notes[:27] + "..." if len(notes) > 30 else notes

                print(
                    f"{car_name:<10} {mileage:<10} {service_type:<30} {service_date:<20} {next_service_date:<20} {cost:<10} {notes:<30}"
                )

            print()
            print("\n*** FOR FULL DETAILS, EXPORT TO A CSV FILE! ***\n")
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
                f"\nSelected Car: {selected_car['name']} (ID: {selected_car['car_id']})\n"
            )

            service_mileage = Menu.get_service_mileage()
            if not service_mileage:
                return

            service_type = Menu.get_service_type()
            if not service_type:
                return

            service_date = Menu.get_service_date()
            if not service_date:
                return
            if not validate_date(service_date):
                print("\nError: Invalid date format.\n")
                return

            next_service_date = Menu.get_next_service_date()
            if not validate_date(next_service_date):
                print("\nError: Invalid date format.\n")
                return
            
            cost = Menu.get_service_cost()
            if cost is None:
                return

            notes = Menu.get_notes()

            self.db_handler.add_service(
                service_mileage=service_mileage,
                service_type=service_type,
                service_date=service_date,
                next_service_date=next_service_date or None,
                cost=cost,
                notes=notes,
                car_id=selected_car["car_id"],
            )
            print("\nService added successfully.\n")
        except Exception as e:
            logging.error("Error in add_service: %s", str(e))
            print("\nAn error occurred while adding the service.\n")

    def update_service(self):
        try:
            user, cars = load_user_and_cars(self.db_handler, self.username)
            if not cars:
                return

            print("\nPlease select a car from the list to view its services:\n")

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

            selected_service = get_selected_service(services)
            if not selected_service:
                return

            updated_data = {}

            while True:
                print("\nWhich fields would you like to update?")
                print("1. Mileage")
                print("2. Service Type")
                print("3. Service Date")
                print("4. Next Service Date")
                print("5. Cost")
                print("6. Notes")
                print("7. Done (Save Changes)")
                print("8. Cancel\n")

                choice = input("Enter your choice: ").strip()

                if choice == "1":
                    mileage = Menu.get_service_mileage()
                    if mileage:
                        updated_data["mileage"] = mileage

                elif choice == "2":
                    service_type = Menu.get_service_type()
                    if service_type:
                        updated_data["service_type"] = service_type

                elif choice == "3":
                    service_date = Menu.get_service_date()
                    if service_date and validate_date(service_date):
                        updated_data["service_date"] = service_date
                    else:
                        print("\nError: Invalid date format. Please use YYYY-MM-DD.\n")

                elif choice == "4":
                    next_service_date = Menu.get_next_service_date()
                    if next_service_date and validate_date(next_service_date):
                        updated_data["next_service_date"] = next_service_date
                    else:
                        print("\nError: Invalid date format. Please use YYYY-MM-DD.\n")
                
                elif choice == "5":
                    cost = Menu.get_service_cost()
                    if cost:
                        updated_data["cost"] = cost

                elif choice == "6":
                    notes = Menu.get_notes()
                    if notes:
                        updated_data["notes"] = notes

                elif choice == "7":
                    if updated_data:
                        if not Menu.confirm_action("\nupdate this service? (y/n): "):
                            print("\nCancelled.\n")
                            return
                        self.db_handler.update_service(
                            selected_service["service_id"], **updated_data
                        )
                        print("\nService updated successfully.\n")
                    else:
                        print("\nNo changes were made.\n")
                    return

                elif choice == "8":
                    print("\nCancelled.\n")
                    return
                else:
                    print("\nInvalid choice.\n")

        except Exception as e:
            logging.error("Error in update_service: %s", str(e))
            print("\nAn error occurred while updating the service.\n")

    def delete_service(self):
        try:
            user, cars = load_user_and_cars(self.db_handler, self.username)
            if not user or not cars:
                return

            print("\nPlease select a car from the list to view its services:\n")

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

            selected_service = get_selected_service(services)
            if not selected_service:
                return

            print(
                f"\nSelected service: {selected_service['service_type']} (ID: {selected_service['service_id']})\n"
            )

            if not Menu.confirm_action("delete this service? (y/n): "):
                print("\nCancelled.\n")
                return
            self.db_handler.delete_service(selected_service["service_id"])
        except Exception as e:
            logging.error("Error in delete_service: %s", str(e))
            print("\nAn error occurred while deleting the service.\n")

    def export_to_csv(self, export_type="cars"):
        try:
            user, cars = load_user_and_cars(self.db_handler, self.username)
            if not user or not cars:
                return
            
            print("\nPlease select a car from your list to export its services:\n")

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
            
            downloads_folder = get_downloads_folder()
            file_name = f"{export_type}_usr.csv"
            file_path = os.path.join(downloads_folder, file_name)

            data, headers = [], []
            if export_type == "cars":
                for car in cars:
                    car["owner"] = self.username
                headers = ["ID", "User ID", "Name", "Model", "Year", "Owner"]
                data = cars                
            elif export_type == "services":
                data = services
                headers = [
                    "ID",
                    "Car Name",
                    "Service Type",
                    "Service Date",
                    "Next Service Date",
                    "Notes",
                ]
            else:
                print("Invalid export type selected.")
                logging.error(f"Invalid export type selected: {export_type}")
                return

            if not data:
                return

            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                for row in data:
                    writer.writerow(row.values())

            print(f"\nFile saved at: {file_path}")
        except Exception as e:
            logging.error("Error in export_to_csv: %s", str(e))
            print("\nAn error occurred while exporting to CSV.")

    def vehicle_lookup(self):
        try:
            print("\n*** Vehicle Lookup  ***\n")
            vin = Menu.get_vin_car()
            if not vin:
                return

            user = self.db_handler.load_user(self.username)
            if not user:
                print(ERROR_USER_NOT_FOUND)
                return

            get_car_by_vin(self.db_handler, vin, user["user_id"])

        except Exception as e:
            logging.error("Error in vehicle_lookup: %s", str(e))
            print("\nAn error occurred while looking up the vehicle.")