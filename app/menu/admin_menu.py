from app.actions.admin_actions import AdminActions
from app.menu.menu import Menu


class AdminMenu:
    def __init__(self, admin_actions):
        self.admin_actions = admin_actions
        self.menu_options = {
            "1": "User Management",
            "2": "Car Management",
            "3": "Service Management",
            "4": "Logout",
        }
        self.is_logged_out = False

    def display_admin_menu(self):
        try:
            choice = int(Menu.display_menu(self.menu_options))
        except ValueError:
            Menu.handle_invalid_input()
            return

        if choice == 1:
            self.display_user_management_menu()
        elif choice == 2:
            print("Car Management coming soon.")
        elif choice == 3:
            print("Service Management coming soon.")
        elif choice == 4:
            self.logout()


    def display_user_management_menu(self):
        options = {
            "1": "Add User",
            "2": "List Users",
            "3": "Update User",
            "4": "Delete User",
            "5": "Back",
        }
        try:
            choice = int(Menu.display_menu(options))
        except ValueError:
            Menu.handle_invalid_input()
            return

        if choice == 1:
            self.admin_actions.add_user()
        elif choice == 2:
            self.admin_actions.list_users()
        elif choice == 3:
            print("Update User coming soon.")
        elif choice == 4:
            print("Delete User coming soon.")
        elif choice == 5:
            return

    # @staticmethod
    # def display_car_management_menu():
    #     car_management_options = {
    #         "1": "List Cars",
    #         "2": "Add Car",
    #         "3": "Update Car",
    #         "4": "Delete Car",
    #         "5": "Back to Admin Menu"
    #     }
    #     choice = Menu.display_menu(car_management_options)
    #     if choice == "1":
    #         AdminActions.list_cars()
    #     elif choice == "2":
    #         AdminActions.add_car()
    #     elif choice == "3":
    #         AdminActions.update_car()
    #     elif choice == "4":
    #         AdminActions.delete_car()
    #     elif choice == "5":
    #         AdminMenu.display_admin_menu()
    #     else:
    #         print("Invalid choice, please try again.\n")

    # @staticmethod
    # def display_service_management_menu():
    #     service_management_options = {
    #         "1": "List Services",
    #         "2": "Add Service",
    #         "3": "Update Service",
    #         "4": "Delete Service",
    #         "5": "Back to Admin Menu"
    #     }
    #     choice = Menu.display_menu(service_management_options)
    #     if choice == "1":
    #         AdminActions.list_services()
    #     elif choice == "2":
    #         AdminActions.add_service()
    #     elif choice == "3":
    #         AdminActions.update_service()
    #     elif choice == "4":
    #         AdminActions.delete_service()
    #     elif choice == "5":
    #         AdminMenu.display_admin_menu()
    #     else:
    #         print("Invalid choice, please try again.\n")

    def logout(self):
        self.is_logged_out = True
        print("\nLogging out...")
