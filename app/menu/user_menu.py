from app.menu.menu import Menu

class UserMenu:
    def __init__(self, user_actions):
        self.user_actions = user_actions
        self.menu_options = {
            "1": "Profile Management",
            "2": "Car Management",
            "3": "Service Management",
            "4": "Logout",
        }

    def display_user_menu(self):
        try:
            choice = int(Menu.display_menu(self.menu_options))
        except ValueError:
            Menu.handle_invalid_input()
            return

        if choice == 1:
            self.user_actions.display_profile_menu()
        elif choice == 2:
            print("Car Management coming soon.")
        elif choice == 3:
            print("Service Management coming soon.")
        elif choice == 4:
            return "logout"
    
    def display_profile_menu(self):
        options = {
            "1": "View",
            "2": "Update",
            "3": "Back",
        }
        try:
            choice = int(Menu.display_menu(options))
        except ValueError:
            Menu.handle_invalid_input()
            return

        if choice == 1:
            self.user_actions.view_profile()
        elif choice == 2:
            print("Update User coming soon.")
        elif choice == 3:
            return