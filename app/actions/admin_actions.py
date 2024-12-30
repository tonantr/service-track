from app.menu.menu import Menu

class AdminActions:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def add_user(self):
        if not Menu.confirm_action("add a new user? (y/n): "):
            self.list_users()
            return

        username = Menu.get_username()
        if not username:
            return

        password = input("Enter new password: ").strip()

        email = Menu.get_email()
        if not email:
            return

        role = Menu.get_role()
        if role is None:
            return
        
        users = self.db_handler.load_users()

        if username in users:
            print(f"\nError: username already exists.\n")
        elif any(user["email"] == email for user in users.values()):
            print(f"\nError: email already exists.\n")
        else:
            self.db_handler.add_user(username, password, email, role)
            self.list_users()

    def list_users(self):
        print("\n*** List of Users ***\n")
        users = self.db_handler.load_users()
        if not users:
            print("No users found.\n")
            return

        print(f"{'Username':<15} {'Email':<25} {'Password':<15} {'Role':<10}")
        print("-" * 65)

        for username, details in users.items():
            print(
                f"{username:<15} {details['email']: <25} {"********":<15} {details['role']:<10}"
            )

        print()
        input("\nPress Enter to go back to the Menu.\n")
