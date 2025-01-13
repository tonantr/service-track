import logging
from app.menu.menu import Menu

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(module)s - Line: %(lineno)d - %(message)s",
)


class AdminActions:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def add_user(self):
        try:
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

            if any(user["username"] == username for user in users):
                print(f"\nError: username already exists.\n")
            elif any(user["email"] == email for user in users):
                print(f"\nError: email already exists.\n")
            else:
                self.db_handler.add_user(username, password, email, role)
                print("\nUser added successfully.\n")
                self.list_users()
        except Exception as e:
            logging.error("Error in add_user: %s", str(e))
            print("\nAn error occurred while adding the user.\n")

    def list_users(self):
        try:
            print("\n*** List of Users ***\n")
            users = self.db_handler.load_users()
            if not users:
                print("No users found.\n")
                return

            print(f"{'Username':<15} {'Email':<25} {'Password':<15} {'Role':<10}")
            print("-" * 65)

            for user in users:
                print(
                    f"{user['username']:<15} {user['email']: <25} {"********":<15} {user['role']:<10}"
                )

            print()
            input("\nPress Enter to go back to the Menu.\n")
        except Exception as e:
            logging.error("Error in list_users: %s", str(e))
            print("\nAn error occurred while listing the users.\n")
        
