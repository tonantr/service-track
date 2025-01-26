import logging
from app.menu.menu import Menu
from app.auth.password_hashing import hash_password
from getpass import getpass
from app.utils.validation import validate_email
from app.utils.constants import ERROR_USER_NOT_FOUND, PRESS_ENTER_TO_GO_BACK

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
            user = self.db_handler.load_user(self.username)
            if not user:
                print(ERROR_USER_NOT_FOUND)
                return

            cars = self.db_handler.load_cars(user["user_id"])

            if not cars:
                print("\nNo cars found.\n")
            else:
                print("\n*** Cars ***\n")
                for car in cars:
                    print(f"Name: {car['name']}")
                    print(f"Model: {car['model']}")
                    print(f"Year: {car['year']}")
                    print()
        except Exception as e:
            logging.error("Error in view_cars: %s", str(e))
            print("\nAn error occurred while fetching your cars.\n")
        finally:
            input(PRESS_ENTER_TO_GO_BACK)

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
            user = self.db_handler.load_user(self.username)
            if not user:
                print(ERROR_USER_NOT_FOUND)
                return

            cars = self.db_handler.load_cars(user["user_id"])

            if not cars:
                print("\nNo cars found.\n")
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

            car_id = input("Enter the ID of the car: ").strip()

            if not car_id.isdigit():
                print("\nError: Invalid ID.\n")
                return
            car_id = int(car_id)
            selected_car = None
            for car in cars:
                if car["car_id"] == car_id:
                    selected_car = car
                    break
            if not selected_car:
                print("\nError: Car not found.\n")
                return
            print(f"\nSelected Car: {selected_car['name']} (ID: {car_id})\n")
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

                self.db_handler.update_car(car_id, name=name)
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

                self.db_handler.update_car(car_id, model=model)
                print("\nModel updated successfully.\n")
            elif choice == "3":
                year = Menu.get_year_car()
                if not year:
                    print("\nError: Year cannot be empty or invalid.\n")
                    return

                self.db_handler.update_car(car_id, year=year)
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
            user = self.db_handler.load_user(self.username)
            if not user:
                print(ERROR_USER_NOT_FOUND)
                return

            cars = self.db_handler.load_cars(user["user_id"])
            if not cars:
                print("\nNo cars found.\n")
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

            car_id = input("Enter the ID of the car: ").strip()
            if not car_id.isdigit():
                print("\nError: Invalid ID.\n")
                return
            car_id = int(car_id)
            selected_car = None
            for car in cars:
                if car["car_id"] == car_id:
                    selected_car = car
                    break
            if not selected_car:
                print("\nError: Car not found.\n")
                return

            print(f"\nSelected car: {selected_car["name"]} (ID: {car_id})\n")
            if not Menu.confirm_action("delete this car? (y/n): "):
                print("\nCancelled.\n")
                return
            self.db_handler.delete_car_and_related_services(car_id)
            print("\nCar deleted successfully.\n")
        except Exception as e:
            logging.error("Error in delete_car: %s", str(e))
            print("\nAn error occurred while deleting the car.\n")
