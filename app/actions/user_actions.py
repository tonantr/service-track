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
