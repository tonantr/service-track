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
            "4": "Logout\n",
        }
        self.COMMON_OPTIONS = {
            "1": "List",
            "2": "Add",
            "3": "Update",
            "4": "Delete",
            "5": "Back\n",
        }

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
                print("Delete Service coming soon.")
            elif choice == "5":
                return
