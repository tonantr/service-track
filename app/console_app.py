import os
import sys
from dotenv import load_dotenv
from app.actions.admin_actions import AdminActions
from app.actions.user_actions import UserActions
from app.database.user_database_handler import UserDatabaseHandler
from app.database.admin_database_handler import AdminDatabaseHandler
from app.auth.login_module import LoginModule
from app.menu.menu import Menu
from app.menu.admin_menu import AdminMenu
from app.menu.user_menu import UserMenu

# from app.file_handler import FileHandler


class ConsoleApp:
    def __init__(self):
        if getattr(sys, "_MEIPASS", False):
            base_path = sys._MEIPASS
            env_file_path = os.path.join(base_path, ".env")  
        else:
            base_path = os.path.dirname(__file__)
            env_file_path = os.path.join(base_path, "../.env") 

        load_dotenv(env_file_path)

        db_config = {
            "host": os.getenv("MYSQL_HOST_WINDOWS"),
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_PASSWORD"),
            "database": os.getenv("MYSQL_DATABASE"),
        }

        if not all(db_config.values()):
            raise ValueError("Missing database configuration in environment variables.")

        self.user_db_handler = UserDatabaseHandler(**db_config)
        self.admin_db_handler = AdminDatabaseHandler(**db_config)

        # self.login_module = LoginModule(FileHandler())

        # self.db_handler.connect() # manually connect to the database

        self.login_module = LoginModule(self.user_db_handler)

        self.admin_actions = AdminActions(self.admin_db_handler)
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
                with self.user_db_handler:  # Automatically calls __enter__ and __exit__ methods
                    if self.login_module.login():
                        logged_in_user = self.login_module.logged_in_user
                        self.user_details = self.user_db_handler.load_user(
                            logged_in_user
                        )

                        if self.user_details.get("role") == "admin":
                            self.run_admin_menu()
                        else:
                            self.user_actions = UserActions(
                                self.user_db_handler, self.user_details.get("username")
                            )
                            self.user_menu = UserMenu(self.user_actions)
                            self.run_user_menu()
            elif choice == 2:
                break
            else:
                Menu.handle_invalid_input()

    def run_admin_menu(self):
        with self.admin_db_handler:
            while True:
                result = self.admin_menu.display_admin_menu()

                if result == "logout":
                    print("\nLogging out...")
                    break

    def run_user_menu(self):
        with self.user_db_handler:
            while True:
                result = self.user_menu.display_user_menu()

                if result == "logout":
                    print("\nLogging out...")
                    break
