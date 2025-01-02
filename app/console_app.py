import json
from app.actions.admin_actions import AdminActions
from app.actions.user_actions import UserActions
from app.database.database_handler import DatabaseHandler
from app.auth.login_module import LoginModule
from app.menu.menu import Menu
from app.menu.admin_menu import AdminMenu
from app.menu.user_menu import UserMenu

# from app.file_handler import FileHandler


class ConsoleApp:
    def __init__(self, target_server="macos", config_path="config.json"):
        with open(config_path, "r") as file:
            self.config = json.load(file)

        if target_server not in self.config:
            raise ValueError("Invalid target server.")
        db_config = self.config[target_server]

        # self.login_module = LoginModule(FileHandler())
        self.db_handler = DatabaseHandler(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"],
        )
        # self.db_handler.connect() # manually connect to the database

        self.login_module = LoginModule(self.db_handler)
        self.admin_actions = AdminActions(self.db_handler)
        self.admin_menu = AdminMenu(self.admin_actions)

        self.user_menu = None
        self.user_actions = None
        self.user_details = None

    def run(self):
        print("*** SERVICE TRACK ***\n")

        while True:
            try:
                choice = int(Menu.display_main_menu())
            except ValueError:
                Menu.handle_invalid_input()
                continue

            if choice == 1:
                with self.db_handler: # Automatically calls __enter__ and __exit__ methods
                    if self.login_module.login():
                        logged_in_user = self.login_module.logged_in_user
                        self.user_details = self.db_handler.load_user(logged_in_user)

                        if self.user_details.get("role") == "admin":
                            self.run_admin_menu()
                        else:
                            self.user_actions = UserActions(
                                self.db_handler, self.user_details.get("username")
                            )
                            self.user_menu = UserMenu(self.user_actions)
                            self.run_user_menu()
            elif choice == 2:
                break
            else:
                Menu.handle_invalid_input()

    def run_admin_menu(self):
        while True:
            result = self.admin_menu.display_admin_menu()

            if result == "logout":
                print("\nLogging out...")
                break

    def run_user_menu(self):
        while True:
            result = self.user_menu.display_user_menu()

            if result == "logout":
                print("\nLogging out...")
                break
