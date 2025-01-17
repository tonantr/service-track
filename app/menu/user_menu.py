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
            print("Service Management coming soon.")
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
                choice = int(Menu.display_menu(options))
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
        options = {
            "1": "View Cars",
            "2": "Add Car",
            "3": "Edit Car",
            "4": "Delete Car",
            "5": "Back\n",
        }
        while True:
            try:
                choice = int(Menu.display_menu(options))
            except ValueError:
                Menu.handle_invalid_input()
                continue

            if choice == 1:
                self.user_actions.view_cars()
            elif choice == 2:
                print("Add Car coming soon.")
            elif choice == 3:
                print("Edit Car coming soon.")
            elif choice == 4:
                print("Delete Car coming soon.")
            elif choice == 5:
                return