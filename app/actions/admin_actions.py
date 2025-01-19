import logging
from getpass import getpass
from app.menu.menu import Menu
from app.utils.validation import validate_email, validate_date

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

    def update_car(self):
        try:
            cars = self.db_handler.load_cars()
            if not cars:
                print("\nNo cars found.\n")
                return
            print("\n*** List of Cars ***\n")
            print(f"{'ID':<5} {'Name':<20} {'Model':<20} {'Year':<10} {'Owner':<20}")
            print("-" * 75)
            for car in cars:
                car_id = str(car["car_id"])
                name = str(car["name"])
                model = str(car["model"])
                year = str(car["year"])
                owner = str(car["owner"])
                print(f"{car_id:<5} {name:<20} {model:<20} {year:<10} {owner:<20}")
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
            print("4. Owners")
            print("5. Cancel\n")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                name = Menu.get_name_car()
                if not name:
                    return
                self.db_handler.update_car(car_id, name=name)
                print("\nName updated successfully.\n")
            elif choice == "2":
                model = Menu.get_model_car()
                if not model:
                    return
                self.db_handler.update_car(car_id, model=model)
                print("\nModel updated successfully.\n")
            elif choice == "3":
                year = Menu.get_year_car()
                if not year:
                    return
                self.db_handler.update_car(car_id, year=year)
                print("\nYear updated successfully.\n")
            elif choice == "4":
                users = self.db_handler.load_users()
                if not users:
                    print("\nNo users found.\n")
                    return
                print("\n*** List of Users ***\n")
                print(f"{'ID':<5} {'Username':<15}")
                print("-" * 20)
                for user in users:
                    print(f"{user['user_id']:<5} {user['username']:<15}")
                print()
                owner_id = input("Enter the ID of the user: ").strip()
                if not owner_id.isdigit():
                    print("\nError: Invalid ID.\n")
                    return
                owner_id = int(owner_id)
                if any(user["user_id"] == owner_id for user in users):
                    self.db_handler.update_car(car_id, user_id=owner_id)
                    print("\nOwner updated successfully.\n")
                else:
                    print("\nError: User not found.\n")
            elif choice == "5":
                print("\nCancelled.\n")
                return
            else:
                print("\nError: Invalid choice.\n")
                return
        except Exception as e:
            logging.error("Error in update_car: %s", str(e))
            print("\nAn error occurred while updating the car.\n")

    def delete_car(self):
        try:
            print("\n*** Delete Car ***\n")
            cars = self.db_handler.load_cars()
            if not cars:
                print("\nNo cars found.\n")
                return
            print("\n*** List of Cars ***\n")
            print(f"{'ID':<5} {'Name':<20} {'Model':<20} {'Year':<10} {'Owner':<20}")
            print("-" * 75)
            for car in cars:
                car_id = str(car["car_id"])
                name = str(car["name"])
                model = str(car["model"])
                year = str(car["year"])
                owner = str(car["owner"])
                print(f"{car_id:<5} {name:<20} {model:<20} {year:<10} {owner:<20}")
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
            if not Menu.confirm_action("delete this car? (y/n): "):
                print("\nCancelled.\n")
                return
            self.db_handler.delete_car(car_id)
            print("\nCar deleted successfully.\n")
        except Exception as e:
            logging.error("Error in delete_car: %s", str(e))
            print("\nAn error occurred while deleting the car.\n")

    def list_services(self):
        try:
            print("\n*** List of Services ***\n")
            services = self.db_handler.load_services()
            if not services:
                print("No services found.\n")
                return
            print(
                f"{'Car Name':<20} {'Service Type':<30} {'Service Date':<20} {'Next Service Date':<20} {'Notes':<50}"
            )
            print("-" * 140)
            for service in services:
                car_name = str(service["car_name"])
                service_type = (
                    str(service["service_type"] + "...")
                    if len(service["service_type"]) > 30
                    else str(service["service_type"])
                )
                service_date = str(service["service_date"])
                next_service_date = str(service["next_service_date"])
                notes = (
                    str(service["notes"] + "...")
                    if len(service["notes"]) > 50
                    else str(service["notes"])
                )
                print(
                    f"{car_name:<20} {service_type:<30} {service_date:<20} {next_service_date:<20} {notes:<50}"
                )
            print()
            input("\nPress Enter to go back to the Menu.\n")
        except Exception as e:
            logging.error("Error in list_services: %s", str(e))
            print("\nAn error occurred while listing the services.\n")

    def add_service(self):
        try:
            print("\n*** Add Service ***\n")
            cars = self.db_handler.load_cars()
            if not cars:
                print("\nNo cars found.\n")
                return
            print("\n*** List of Cars ***\n")
            print(f"{'ID':<5} {'Name':<20}")
            print("-" * 25)
            for car in cars:
                print(f"{car['car_id']:<5} {car['name']:<20}")
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
                next_service_date=next_service_date,
                notes=notes,
                car_id=car_id,
            )
            print("\nService added successfully.\n")
        except Exception as e:
            logging.error("Error in add_service: %s", str(e))
            print("\nAn error occurred while adding the service.\n")

    def update_service(self):
        try:
            services = self.db_handler.load_services()
            if not services:
                print("\nNo services found\n")
                return
            print("\n*** List of Services ***\n")
            print(
                f"{'ID':<5} {'Car Name':<20} {'Service Type':<30} {'Service Date':<20} {'Next Service Date':<20} {'Notes':<50}"
            )
            print("-" * 140)
            for service in services:
                service_id = str(service["service_id"])
                car_name = str(service["car_name"])
                service_type = str(service["service_type"][:30])
                service_date = str(service["service_date"])
                next_service_date = str(service["next_service_date"])
                notes = str(service["notes"][:50])
                print(
                    f"{service_id:<5} {car_name:<20} {service_type:<30} {service_date:<20} {next_service_date:<20} {notes:<50}"
                )
            service_id = input("\nEnter the ID of the service: ").strip()
            if not service_id.isdigit():
                print("\nError: Invalid ID.\n")
                return
            service_id = int(service_id)
            selected_service = None
            for service in services:
                if service["service_id"] == service_id:
                    selected_service = service
                    break
            if not selected_service:
                print("\nService not found\n")
                return
            print(
                f"\nSelected Service: {selected_service['service_type']} (ID: {service_id})\n"
            )
            print("Which fields would you like to update?\n")
            print("1. Service Type")
            print("2. Service Date")
            print("3. Next Service Date")
            print("4. Notes")
            print("5. Cancel\n")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                service_type = Menu.get_service_type()
                if not service_type:
                    return
                self.db_handler.update_service(service_id, service_type=service_type)
                print("\nService type updated successfully.\n")
            elif choice == "2":
                service_date = Menu.get_service_date()
                if not service_date:
                    return
                self.db_handler.update_service(service_id, service_date=service_date)
                print("\nService Date updated successfully.\n")
            elif choice == "3":
                next_service_date = Menu.get_next_service_date()
                if not next_service_date:
                    return
                self.db_handler.update_service(
                    service_id, next_service_date=next_service_date
                )
                print("\nNext service date updated successfully.\n")
            elif choice == "4":
                notes = Menu.get_notes()
                if not notes:
                    return
                self.db_handler.update_service(service_id, notes=notes)
                print("\nNotes updated successfully.\n")
            elif choice == "5":
                print("\nCancelled.\n")
                return
            else:
                print("\nError: Invalid choice.\n")

        except Exception as e:
            logging.error("Error in update_service: %s", str(e))
            print("\nAn error occurred while updating the service")
