import logging
from app.menu.menu import Menu
from app.auth.password_hashing import hash_password
from getpass import getpass
from app.utils.validation import validate_email

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(module)s - Line: %(lineno)d - %(message)s",
)


class UserActions:
    def __init__(self, db_handler, username):
        self.db_handler = db_handler
        self.username = username

    def view_profile(self):
        try:
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
        except Exception as e:
            logging.error("Error in view_profile: %s", str(e))
            print("\nAn error occured while fetching your profile.\n")

    def change_password(self):
        try:
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

            self.db_handler.update_password(self.username, hashed_password)
            print("\nPassword updated successfully.\n")
            print("For security reasons, you will be logged out.")
            return "logout"
        except Exception as e:
            logging.error("Error in change_password: %s", str(e))
            print("\nAn error occurred while updating the password.\n")

    def update_email(self):
        try:
            user = self.db_handler.load_user(self.username)
            if not user:
                print("\nError: User not found.\n")
                return

            print(f"Current email: {user['email']}")
            new_email = input("Enter new email: ")

            if not validate_email(new_email):
                print("\nError: Invalid email.\n")
                return

            existing_email = self.db_handler.load_user_by_email(new_email)
            if existing_email:
                print("\nError: Email already exists.\n")
                return

            self.db_handler.update_email(self.username, new_email)
            print("\nEmail updated successfully.\n")
        except Exception as e:
            logging.error("Error in update_email: %s", str(e))
            print("\nAn error occurred while updating the email.\n")
        finally:
            input("Press Enter to go back to the Menu.\n")

    def view_cars(self):
        try:
            user = self.db_handler.load_user(self.username)
            if not user:
                print("\nError: User not found.\n")
                return

            cars = self.db_handler.load_cars(user["user_id"])

            if not cars:
                print("\nNo cars found.\n")
            else:
                print("\n*** Cars ***\n")
                for car in cars:
                    print(f"Name: {car['name']}")
                    print(f"Model: {car['model']}")
                    print(f"Year: {car['year']}")
                    print()
        except Exception as e:
            logging.error("Error in view_cars: %s", str(e))
            print("\nAn error occurred while fetching your cars.\n")
        finally:
            input("Press Enter to go back to the Menu.\n")
