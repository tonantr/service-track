from app.menu.menu import Menu


class AdminMenu:

    menu_options = {
        "1": "User Management",
        "2": "Car Management",
        "3": "Service Management",
        "4": "Logout",
    }

    @staticmethod
    def display_admin_menu():
        choice = Menu.display_menu(AdminMenu.menu_options)
        if choice == "1":
            AdminMenu.display_user_management_menu()
        elif choice == "2":
            AdminMenu.display_car_management_menu()
        elif choice == "3":
            AdminMenu.display_service_management_menu()
        elif choice == "4":
            print("Logging out...")
    
    # @staticmethod 
    # def display_user_management_menu():
    #     user_management_options = {
    #         "1": "Add User",
    #         "2": "List Users",
    #         "3": "Update User",
    #         "4": "Delete User",
    #         "5": "Back to Admin Menu"
    #     }
    #     choice = Menu.display_menu(user_management_options)
    #     if choice == "1":
    #         AdminActions.add_user()
    #     elif choice == "2":
    #         AdminActions.list_users()
    #     elif choice == "3":
    #         AdminActions.update_user()
    #     elif choice == "4":
    #         AdminActions.delete_user()
    #     elif choice == "5":
    #         AdminMenu.display_admin_menu()
    #     else:
    #         print("Invalid choice, please try again.\n")

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
