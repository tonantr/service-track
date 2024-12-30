import json
from app.actions.admin_actions import AdminActions
from app.database.database_handler import DatabaseHandler
from app.auth.login_module import LoginModule
from app.menu.menu import Menu
from app.menu.admin_menu import AdminMenu

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
        self.login_module = LoginModule(self.db_handler)
        self.admin_actions = AdminActions(self.db_handler)

        self.admin_menu = AdminMenu(self.admin_actions)

    def run(self):
        print("*** SERVICE TRACK ***\n")

        while True:
            try:
                choice = int(Menu.display_main_menu())
            except ValueError:
                Menu.handle_invalid_input()
                continue

            if choice == 1:
                if self.login_module.login():
                    logged_in_user = self.login_module.logged_in_user
                    user_details = self.login_module.users.get(logged_in_user)

                    if user_details and user_details.get("role") == "admin":
                        self.run_admin_menu()
                    else:
                        self.run_user_menu()
            elif choice == 2:
                break
            else:
                Menu.handle_invalid_input()

    # def run_admin_menu(self):
    #     while True:
    #         try:
    #             choice = int(Menu.display_admin_menu())
    #         except ValueError:
    #             Menu.handle_invalid_input()
    #             continue

    #         if choice == 1:
    #             self.admin_actions.add_user()
    #         elif choice == 2:
    #             self.admin_actions.list_users()
    #         elif choice == 3:
    #             break
    #         else:
    #             Menu.handle_invalid_input()

    def run_admin_menu(self):
        while True:
            result = self.admin_menu.display_admin_menu()

            if result == "logout":
                print("\nLogging out...")
                break

    def run_user_menu(self):
        while True:
            try:
                choice = int(Menu.display_user_menu())
            except ValueError:
                Menu.handle_invalid_input()
                continue

            if choice == 1:
                self.admin_actions.list_users()
            elif choice == 2:
                break
            else:
                Menu.handle_invalid_input()
