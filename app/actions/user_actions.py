from app.menu.menu import Menu

class UserActions:
    def __init__(self, db_handler, username):
        self.db_handler = db_handler
        self.username = username

    def view_profile(self):
        user = self.db_handler.load_user(self.username)
        if not user:
            print("\nError: User not found.\n")
            return

        print("\n*** User Details ***\n")
        print(f"Username: {user['username']}")
        print(f"Password: {'*' * 8}")
        print(f"Email: {user['email']}")
        print(f"Role: {user['role']}\n")

        input("Press Enter to go back to the Menu.\n")

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
            self.view_profile()
        elif choice == 2:
            print("Update User coming soon.")
        elif choice == 3:
            return