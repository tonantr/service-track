import getpass
import logging
from app.auth.password_hashing import verify_password

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(module)s - Line: %(lineno)d - %(message)s",
)


class LoginModule:
    # def __init__(self, file_handler):
    #     self.file_handler = file_handler
    #     self.file_handler.file_exists()
    #     self.users = self.file_handler.load_users()
    #     self.logged_in_user = None

    def __init__(self, db_handler):
        self.db_handler = db_handler
        self.logged_in_user = None

    # def add_user(self, username, password):
    #     self.users[username] = password
    #     self.file_handler.save_users(self.users)

    def authenticate(self, username, password):
        try:
            user = self.db_handler.load_user(username)
            if user:
                stored_password = user["password"]
                return verify_password(password, stored_password)
            return False
        except Exception as e:
            logging.error(f"Error authenticating user: {e}")
            print("Error authenticating user.")
            return False

    def login(self, max_attempts=3):
        try:
            attempts = 0
            while attempts < max_attempts:
                username = input("\nEnter your username: ")
                password = getpass.getpass("Enter your password: ")

                if self.authenticate(username, password):
                    self.logged_in_user = username
                    user = self.db_handler.load_user(username)
                    if user:
                        role = user.get("role")
                        print(f"\nLogged in as {username} ({role})!\n")
                        return True
                    else:
                        print("Error: User not found.")
                        return False
                else:
                    attempts += 1
                    print("\nInvalid username or password.\n")
                    if attempts < max_attempts:
                        print(f"Attempts remaining: {max_attempts - attempts}\n")
                    else:
                        print("Too many failed attempts.")
            return False
        except Exception as e:
            logging.error(f"Error logging in: {e}")
            print("Error logging in.")
