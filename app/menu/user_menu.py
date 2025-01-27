from app.menu.menu import Menu


class UserMenu:
    def __init__(self, user_actions):
        self.user_actions = user_actions
        self.menu_options = {
            "1": "Profile Management",
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
                print("Update service is coming soon")
            elif choice == 4:
                print("Delete service is coming soon")
            elif choice == 5:
                return
