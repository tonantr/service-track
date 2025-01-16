from app.actions.admin_actions import AdminActions
from app.menu.menu import Menu


class AdminMenu:
    def __init__(self, admin_actions):
        self.admin_actions = admin_actions
        self.menu_options = {
            "1": "User Management",
            "2": "Car Management",
            "3": "Service Management",
            "4": "Logout",
        }

    def display_admin_menu(self):
        try:
            choice = int(Menu.display_menu(self.menu_options))
        except ValueError:
            Menu.handle_invalid_input()
            return

        if choice == 1:
            self.display_user_management_menu()
        elif choice == 2:
            self.display_car_management_menu()
        elif choice == 3:
            print("Service Management coming soon.")
        elif choice == 4:
            return "logout"

    def display_user_management_menu(self):
        options = {
            "1": "Add User",
            "2": "List Users",
            "3": "Update User",
            "4": "Delete User",
            "5": "Back",
        }
        try:
            choice = int(Menu.display_menu(options))
        except ValueError:
            Menu.handle_invalid_input()
            return

        if choice == 1:
            self.admin_actions.add_user()
        elif choice == 2:
            self.admin_actions.list_users()
        elif choice == 3:
            self.admin_actions.update_user()
        elif choice == 4:
            self.admin_actions.delete_user()
        elif choice == 5:
            return

    def display_car_management_menu(self):
        options = {
            "1": "List Cars",
            "2": "Add Car",
            "3": "Update Car",
            "4": "Delete Car",
            "5": "Back",
        }
        try:
            choice = Menu.display_menu(options)
        except ValueError:
            Menu.handle_invalid_input()
            return

        if choice == "1":
            self.admin_actions.list_cars()
        elif choice == "2":
            self.admin_actions.add_car()
        elif choice == "3":
            print("Update Car coming soon.")
        elif choice == "4":
            print("Delete Car coming soon.")
        elif choice == "5":
            return

    def display_service_management_menu(self):
        options = {
            "1": "List Services",
            "2": "Add Service",
            "3": "Update Service",
            "4": "Delete Service",
            "5": "Back",
        }
        try:
            choice = Menu.display_menu(options)
        except ValueError:
            Menu.handle_invalid_input()
            return

        if choice == "1":
            print("List Services coming soon.")
        elif choice == "2":
            print("Add Service coming soon.")
        elif choice == "3":
            print("Update Service coming soon.")
        elif choice == "4":
            print("Delete Service coming soon.")
        elif choice == "5":
            return
