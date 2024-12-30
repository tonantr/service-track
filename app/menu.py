class Menu:

    @staticmethod
    def display_main_menu():
        print("\nMain Menu:")
        print("1. Login")
        print("2. Exit\n")
        return input("Enter your choice: ")

    @staticmethod
    def display_admin_menu():
        print("\nAdmin Menu:")
        print("1. Add User")
        print("2. List Users")
        print("3. Logout\n")
        return input("Enter your choice: ")

    @staticmethod
    def display_user_menu():
        print("\nUser Menu:")
        print("1. List Users")
        print("2. Logout\n")
        return input("Enter your choice: ")

    @staticmethod
    def handle_invalid_input():
        print("Invalid input, please enter a number.\n")

    @staticmethod
    def get_username():
        username = input("\nEnter new username: ").strip()
        if not username:
            print("Username cannot be empty.\n")
            return None
        return username

    @staticmethod
    def get_email():
        email = input("Enter email: ").strip()
        if not email:
            print("Error: Email cannot be empty.\n")
            return None
        return email

    @staticmethod
    def get_role():
        print("\nSelect role for the new user:")
        print("1. Admin")
        print("2. User")

        try:
            role = int(input("Enter role number: ").strip())
        except ValueError:
            print("Invalid role number.\n")
            return None

        if role == 1:
            return "admin"
        elif role == 2:
            return "user"
        else:
            print("Invalid role number.\n")
            return None

    @staticmethod
    def confirm_action(message="Are you sure? (y/n): "):
        return input(message).strip().lower() == "y"
