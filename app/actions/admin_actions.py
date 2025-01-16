import logging
from getpass import getpass
from app.menu.menu import Menu
from app.utils.validation import validate_email

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(module)s - Line: %(lineno)d - %(message)s",
)


class AdminActions:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def add_user(self):
        try:
            if not Menu.confirm_action("add a new user? (y/n): "):
                self.list_users()
                return

            username = Menu.get_username()
            if not username:
                return

            password = getpass("Enter new password: ").strip()

            email = Menu.get_email()
            if not email:
                return
            if not validate_email(email):
                print("\nError: Invalid email.\n")
                return

            role = Menu.get_role()
            if role is None:
                return

            users = self.db_handler.load_users()

            if any(user["username"] == username for user in users):
                print(f"\nError: username already exists.\n")
            elif any(user["email"] == email for user in users):
                print(f"\nError: email already exists.\n")
            else:
                self.db_handler.add_user(username, password, email, role)
                print("\nUser added successfully.\n")
                self.list_users()
        except Exception as e:
            logging.error("Error in add_user: %s", str(e))
            print("\nAn error occurred while adding the user.\n")

    def list_users(self):
        try:
            print("\n*** List of Users ***\n")
            users = self.db_handler.load_users()
            if not users:
                print("No users found.\n")
                return

            print(f"{'Username':<15} {'Email':<25} {'Password':<15} {'Role':<10}")
            print("-" * 65)

            for user in users:
                print(
                    f"{user['username']:<15} {user['email']: <25} {'********':<15} {user['role']:<10}"
                )

            print()
            input("\nPress Enter to go back to the Menu.\n")
        except Exception as e:
            logging.error("Error in list_users: %s", str(e))
            print("\nAn error occurred while listing the users.\n")

    def update_user(self):
        try:
            users = self.db_handler.load_users()
            if not users:
                print("\nNo users found.\n")
                return
            print("\n*** List of Users ***\n")
            print(f"{'ID':<5} {'Username':<15} {'Email':<25} {'Role':<10}")
            print("-" * 55)
            for user in users:
                print(
                    f"{user['user_id']:<5} {user['username']:<15} {user['email']: <25} {user['role']:<10}"
                )
            print()

            user_id = input("Enter the ID of the user: ").strip()
            if not user_id.isdigit():
                print("\nError: Invalid ID.\n")
                return
            user_id = int(user_id)

            selected_user = None
            for user in users:
                if user["user_id"] == user_id:
                    selected_user = user
                    break

            if not selected_user:
                print("\nError: User not found.\n")
                return
            print(f"\nSelected User: {selected_user['username']} (ID: {user_id})\n")
            print("Which fields would you like to update?")
            print("1. Username")
            print("2. Email")
            print("3. Role")
            print("4. Password")
            print("5. Cancel\n")

            choice = input("Enter your choice: ").strip()
            if choice == "1":
                username = Menu.get_username()
                if not username:
                    return
                self.db_handler.update_user(user_id, username=username)
                print("\nUsername updated successfully.\n")
            elif choice == "2":
                email = Menu.get_email()
                if not email:
                    return
                if not validate_email(email):
                    print("\nError: Invalid email.\n")
                    return
                self.db_handler.update_user(user_id, email=email)
            elif choice == "3":
                role = Menu.get_role()
                if role:
                    self.db_handler.update_user(user_id, role=role)
                    print("\nRole updated successfully.\n")
            elif choice == "4":
                password = getpass("Enter new password: ").strip()
                if not password:
                    print("\nError: Password cannot be empty.\n")
                else:
                    self.db_handler.update_user(user_id, password=password)
                    print("\nPassword updated successfully.\n")
            elif choice == "5":
                return
            else:
                print("\nError: Invalid choice.\n")
                return

        except Exception as e:
            logging.error("Error in update_user: %s", str(e))
            print("\nAn error occurred while updating the user.\n")

    def delete_user(self):
        try:
            users = self.db_handler.load_users()
            if not users:
                print("\nNo users found.\n")
                return
            print("\n*** List of Users ***\n")
            print(f"{'ID':<5} {'Username':<15} {'Email':<25} {'Role':<10}")
            print("-" * 55)
            for user in users:
                print(
                    f"{user['user_id']:<5} {user['username']:<15} {user['email']: <25} {user['role']:<10}"
                )
            print()

            user_id = input("Enter the ID of the user: ").strip()
            if not user_id.isdigit():
                print("\nError: Invalid ID.\n")
                return
            user_id = int(user_id)

            selected_user = None
            for user in users:
                if user["user_id"] == user_id:
                    selected_user = user
                    break

            if not selected_user:
                print("\nError: User not found.\n")
                return
            print(f"\nSelected User: {selected_user['username']} (ID: {user_id})\n")
            if not Menu.confirm_action("delete this user? (y/n): "):
                return

            self.db_handler.delete_user(user_id)
            print("\nUser deleted successfully.\n")
        except Exception as e:
            logging.error("Error in delete_user: %s", str(e))
            print("\nAn error occurred while deleting the user.\n")

    def list_cars(self):
        try:
            print("\n*** List of Cars ***\n")
            cars = self.db_handler.load_cars()
            if not cars:
                print("No cars found.\n")
                return

            print(
                f"{'ID':<5} {'Name':<20} {'Model':<20} {'Year':<10} {'Owner':<20} {'Services':<50}"
            )
            print("-" * 125)

            for car in cars:
                car_id = str(car["car_id"])
                name = str(car["name"])
                model = str(car["model"])
                year = str(car["year"])
                owner = str(car["owner"])
                services = str(car["services"])
                print(
                    f"{car_id:<5} {name:<20} {model:<20} {year:<10} {owner:<20} {services:<50}"
                )

            print()
            input("\nPress Enter to go back to the Menu.\n")
        except Exception as e:
            logging.error("Error in list_cars: %s", str(e))
            print("\nAn error occurred while listing the cars.\n")

    def add_car(self):
        try:
            print("\n*** Add Car ***\n")

            users = self.db_handler.load_users()
            if not users:
                print("\nNo users found.\n")
                return
            print("\n*** List of Users ***\n")
            print(f"{'ID':<5} {'Username':<15} {'Email':<25} {'Role':<10}")
            print("-" * 55)
            for user in users:
                print(
                    f"{user['user_id']:<5} {user['username']:<15} {user['email']: <25} {user['role']:<10}"
                )
            print()

            user_id = input("Enter the ID of the user: ").strip()
            if not user_id.isdigit():
                print("\nError: Invalid ID.\n")
                return
            user_id = int(user_id)

            selected_user = None
            for user in users:
                if user["user_id"] == user_id:
                    selected_user = user
                    break
            print(f"\nSelected User: {selected_user['username']} (ID: {user_id})\n")
            print("Enter the details of the car:")
            car_name = Menu.get_name_car()
            if not car_name:
                return

            car_model = Menu.get_model_car()
            if not car_model:
                return

            car_year = Menu.get_year_car()
            if not car_year:
                return

            if not Menu.confirm_action("add this car? (y/n): "):
                print("\nCancelled.\n")
                return

            self.db_handler.add_car(car_name, car_model, car_year, user_id)
            print("\nCar added successfully.\n")

        except Exception as e:
            logging.error("Error in add_car: %s", str(e))
            print("\nAn error occurred while adding the car.\n")
