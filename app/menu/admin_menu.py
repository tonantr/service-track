from app.actions.admin_actions import AdminActions
from app.menu.menu import Menu
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(module)s - Line: %(lineno)d - %(message)s",
)


class AdminMenu:
    def __init__(self, admin_actions):
        self.admin_actions = admin_actions
        self.menu_options = {
            "1": "User Management",
            "2": "Car Management",
            "3": "Service Management",
            "4": "Export Data",
            "5": "Vehicle Lookup",
            "6": "Logout\n",
        }
        self.COMMON_OPTIONS = {
            "1": "List",
            "2": "Add",
            "3": "Update",
            "4": "Delete",
            "5": "Back\n",
        }
        self.export_options = {"1": "CSV", "2": "PDF", "3": "Back\n"}
        self.export_type = {"1": "Users", "2": "Cars", "3": "Services", "4": "Back\n"}

    def display_admin_menu(self):
        while True:
            try:
                choice = Menu.display_menu(self.menu_options)
            except ValueError as e:
                logging.error(f"Error in display_admin_menu: {e}")
                Menu.handle_invalid_input("Invalid option in Admin Menu.")
                continue

            if choice == "1":
                self.display_user_management_menu()
            elif choice == "2":
                self.display_car_management_menu()
            elif choice == "3":
                self.display_service_management_menu()
            elif choice == "4":
                self.export_data()
            elif choice == "5":
                self.display_vehicle_lookup_menu()
            elif choice == "6":
                return "logout"

    def display_user_management_menu(self):
        while True:
            try:
                choice = Menu.display_menu(self.COMMON_OPTIONS, "User Management")
            except ValueError as e:
                logging.error(f"Error in display_user_management_menu: {e}")
                Menu.handle_invalid_input("Invalid option in User Menu.")
                continue

            if choice == "1":
                self.admin_actions.list_users()
            elif choice == "2":
                self.admin_actions.add_user()
            elif choice == "3":
                self.admin_actions.update_user()
            elif choice == "4":
                self.admin_actions.delete_user()
            elif choice == "5":
                return

    def display_car_management_menu(self):
        while True:
            try:
                choice = Menu.display_menu(self.COMMON_OPTIONS, "Car Management")
            except ValueError as e:
                logging.error(f"Error in display_car_management_menu: {e}")
                Menu.handle_invalid_input("Invalid option in Car Menu")
                continue

            if choice == "1":
                self.admin_actions.list_cars()
            elif choice == "2":
                self.admin_actions.add_car()
            elif choice == "3":
                self.admin_actions.update_car()
            elif choice == "4":
                self.admin_actions.delete_car()
            elif choice == "5":
                return

    def display_service_management_menu(self):
        while True:
            try:
                choice = Menu.display_menu(self.COMMON_OPTIONS, "Service Management")
            except ValueError as e:
                logging.error(f"Error in display_service_management_menu: {e}")
                Menu.handle_invalid_input("Invalid option in Service Menu")
                continue

            if choice == "1":
                self.admin_actions.list_services()
            elif choice == "2":
                self.admin_actions.add_service()
            elif choice == "3":
                self.admin_actions.update_service()
            elif choice == "4":
                self.admin_actions.delete_service()
            elif choice == "5":
                return

    def export_data(self):
        while True:
            choice = Menu.display_menu(self.export_options)

            if choice == "1":
                user_choice = Menu.display_menu(self.export_type)

                export_types = {"1": "users", "2": "cars", "3": "services", "4": "back"}

                if user_choice in export_types:
                    if export_types[user_choice] == "back":
                        return
                    self.admin_actions.export_to_csv(export_types[user_choice])
                    return

                Menu.handle_invalid_input()

            elif choice == "2":
                print("\nExport to PDF is coming soon.")
                break
            elif choice == "3":
                return
            else:
                Menu.handle_invalid_input()

    def display_vehicle_lookup_menu(self):
        self.admin_actions.vehicle_lookup()