from app.menu.menu import Menu
from app.auth.password_hashing import hash_password
from getpass import getpass


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

    def change_password(self):
        current_password = getpass("Enter current password: ")

        user = self.db_handler.load_user(self.username)
        if not user:
            print("\nError: User not found.\n")
            return

        new_password = getpass("Enter new password: ")
        confirm_password = getpass("Confirm new password: ")
        if new_password != confirm_password:
            print("\nError: Passwords do not match.\n")
            return

        hashed_password = hash_password(new_password)

        try:
            self.db_handler.update_password(self.username, hashed_password)
            print("\nPassword updated successfully.\n")
            print("For security reasons, you will be logged out.\n")
            return "logout"
        except Exception as e:
            print(f"Error: {str(e)}")

        input("Press Enter to go back to the Menu.\n")
