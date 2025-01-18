from app.actions.admin_actions import AdminActions
from app.menu.menu import Menu

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
        try:
            choice = Menu.display_menu(self.menu_options)
        except ValueError:
            Menu.handle_invalid_input()
            return

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
                choice = Menu.display_menu(self.COMMON_OPTIONS)
            except ValueError:
                Menu.handle_invalid_input()
                return

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
                choice = Menu.display_menu(self.COMMON_OPTIONS)
            except ValueError:
                Menu.handle_invalid_input()
                return

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
                choice = Menu.display_menu(self.COMMON_OPTIONS)
            except ValueError:
                Menu.handle_invalid_input()
                return

            if choice == "1":
                self.admin_actions.list_services()
            elif choice == "2":
                self.admin_actions.add_service()
            elif choice == "3":
                print("Update Service coming soon.")
            elif choice == "4":
                print("Delete Service coming soon.")
            elif choice == "5":
                return
