from app.menu.menu import Menu
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(module)s - Line: %(lineno)d - %(message)s",
)


class UserMenu:
    def __init__(self, user_actions):
        self.user_actions = user_actions
        self.menu_options = {
            "1": "Profile Management",
            "2": "Car Management",
            "3": "Service Management",
            "4": "Export Data",
            "5": "Logout\n",
        }

        self.COMMON_OPTIONS = {
            "1": "List",
            "2": "Add",
            "3": "Update",
            "4": "Delete",
            "5": "Back\n",
        }

        self.export_options = {"1": "CSV", "2": "PDF", "3": "Back\n"}
        self.export_type = {"1": "Cars", "2": "Services", "3": "Back\n"}

    def display_user_menu(self):
        try:
            choice = int(Menu.display_menu(self.menu_options))
        except ValueError:
            Menu.handle_invalid_input()
            return

        if choice == 1:
            result = self.display_profile_menu()
            if result == "logout":
                return "logout"
        elif choice == 2:
            self.display_car_menu()
        elif choice == 3:
            self.display_service_menu()
        elif choice == 4:
            self.export_data()
        elif choice == 5:
            return "logout"

    def display_profile_menu(self):
        options = {
            "1": "View Profile",
            "2": "Change Password",
            "3": "Update Email",
            "4": "Back\n",
        }
        while True:
            try:
                choice = int(Menu.display_menu(options, "Profile Management"))
            except ValueError:
                Menu.handle_invalid_input()
                continue

            if choice == 1:
                self.user_actions.view_profile()
            elif choice == 2:
                result = self.user_actions.change_password()
                if result == "logout":
                    return "logout"
            elif choice == 3:
                self.user_actions.update_email()
            elif choice == 4:
                return

    def display_car_menu(self):
        while True:
            try:
                choice = int(Menu.display_menu(self.COMMON_OPTIONS, "Car Management"))
            except ValueError:
                Menu.handle_invalid_input()
                continue

            if choice == 1:
                self.user_actions.view_cars()
            elif choice == 2:
                self.user_actions.add_car()
            elif choice == 3:
                self.user_actions.edit_car()
            elif choice == 4:
                self.user_actions.delete_car()
            elif choice == 5:
                return

    def display_service_menu(self):
        while True:
            try:
                choice = int(
                    Menu.display_menu(self.COMMON_OPTIONS, "Service Management")
                )
            except ValueError:
                Menu.handle_invalid_input()
                continue

            if choice == 1:
                self.user_actions.list_services()
            elif choice == 2:
                self.user_actions.add_service()
            elif choice == 3:
                self.user_actions.update_service()
            elif choice == 4:
                self.user_actions.delete_service()
            elif choice == 5:
                return

    def export_data(self):
        while True:
            choice = Menu.display_menu(self.export_options)

            if choice == "1":
                user_choice = Menu.display_menu(self.export_type)

                export_types = {"1": "cars", "2": "services", "3": "back"}

                if user_choice in export_types:
                    if export_types[user_choice] == "back":
                        return
                    self.user_actions.export_to_csv(export_types[user_choice])
                    return

                Menu.handle_invalid_input()

            elif choice == "2":
                print("\nExport to PDF is coming soon.")
                continue
            elif choice == "3":
                return
            else:
                Menu.handle_invalid_input()
