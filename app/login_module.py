import getpass
from app.password_hashing import hash_password, verify_password


class LoginModule:
    # def __init__(self, file_handler):
    #     self.file_handler = file_handler
    #     self.file_handler.file_exists()
    #     self.users = self.file_handler.load_users()
    #     self.logged_in_user = None

    def __init__(self, db_handler):
        self.db_handler = db_handler
        self.users = self.db_handler.load_users()
        self.logged_in_user = None

    # def add_user(self, username, password):
    #     self.users[username] = password
    #     self.file_handler.save_users(self.users)

    def add_user(self, username, password):
        hashed_password = hash_password(password)
        self.db_handler.save_users(username, hashed_password)
        self.users = self.db_handler.load_users()

    def authenticate(self, username, password):
        stored_password = self.users.get(username)
        if stored_password:
            if stored_password == password:
                hashed_password = hash_password(password)
                self.db_handler.update_password(username, hashed_password)
                self.users[username] = hashed_password
                return True
        
            return verify_password(password, stored_password)
        return False

    def login(self, max_attempts=3):

        attempts = 0
        while attempts < max_attempts:
            username = input("\nEnter your username: ")
            # password = input('Enter your password: ')
            password = getpass.getpass("Enter your password: ")

            if self.authenticate(username, password):
                self.logged_in_user = username
                print(f"\nWelcome, {username}!\n")
                return True
            else:
                attempts += 1
                print("Invalid username or password.\n")
                if attempts < max_attempts:
                    print(f"Attempts remaining: {max_attempts - attempts}\n")
                else:
                    print("Too many failed attempts.")
        return False
