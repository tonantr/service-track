import json
import os


class FileHandler:
    def __init__(self, filename="users.json"):
        self.filepath = os.path.join(os.path.dirname(__file__), filename)
        self.file_exists()

    def file_exists(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.isfile(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump({}, f, indent=4)

    def load_users(self):
        with open(self.filepath, "r") as f:
            return json.load(f)

    def save_users(self, users):
        with open(self.filepath, "w") as f:
            json.dump(users, f, indent=4)
