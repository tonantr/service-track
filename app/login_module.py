import json
import getpass
import os


class LoginModule:
    def __init__(self, filename="users.json"):
        self.filepath = os.path.join(os.path.dirname(__file__), filename)
        self.file_exists()
        self.users = self.load_users()
        self.logged_in_user = None

    def file_exists(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.isfile(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump({}, f, indent=4)

    def load_users(self):
        with open(self.filepath, "r") as f:
            return json.load(f)

    def save_users(self):
        with open(self.filepath, "w") as f:
            json.dump(self.users, f, indent=4)

    def add_user(self, username, password):
        self.users[username] = password
        self.save_users()

    def authenticate(self, username, password):
        return self.users.get(username) == password

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



