from app.admin_menu_handler import AdminMenuHandler
from app.database_handler import DatabaseHandler
from app.login_module import LoginModule
from app.menu import Menu
# from app.file_handler import FileHandler


class ConsoleApp:
    def __init__(self):
        # self.login_module = LoginModule(FileHandler())
        self.db_handler = DatabaseHandler(
            host="192.168.2.234", 
            user="root", 
            password="P@ssw0rd123", 
            database="service_track"
        )
        self.login_module = LoginModule(self.db_handler)
        self.admin_menu_handler = AdminMenuHandler(self.login_module)

    def run(self):
        print("*** SERVICE TRACK ***\n")

        while True:
            Menu.display_main_menu()
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    if self.login_module.login():
                        if self.login_module.logged_in_user == "admin":
                            self.run_admin_menu()
                        else:
                            self.run_user_menu()
                elif choice == 2:
                    if self.admin_menu_handler.handle_exit():
                        break
                else:
                    print("Invalid choice, please enter 1 or 2.\n")
            except ValueError:
                print("Invalid input, please enter a number.\n")

    def run_admin_menu(self):
        while True:
            Menu.display_admin_menu()

            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.admin_menu_handler.handle_add_user()
                elif choice == 2:
                    self.admin_menu_handler.handle_list_users()
                elif choice == 3:
                    break
                else:
                    print("Invalid choice, please enter a number between 1 and 3.\n")
            except ValueError:
                print("Invalid input, please enter a number.\n")

    def run_user_menu(self):
        while True:
            Menu.display_user_menu()

            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.admin_menu_handler.handle_list_users()
                elif choice == 2:
                    break
                else:
                    print("Invalid choice, please enter 1 or 2.\n")
            except ValueError:
                print("Invalid input, please enter a number.\n")
