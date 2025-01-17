class Menu:

    @staticmethod
    def display_main_menu():
        print("\nMain Menu:")
        print("1. Login")
        print("2. Exit\n")
        return input("Enter your choice: ")

    @staticmethod
    def display_menu(menu_options):
        print("\nMenu:")
        for key, value in menu_options.items():
            print(f"{key}. {value}")
        return input("Enter your choice: ")

    @staticmethod
    def handle_invalid_input():
        print("\nInvalid input, please enter a number.\n")

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
    def get_name_car():
        name = input("\nEnter car name: ").strip()
        if not name:
            print("Error: Name cannot be empty.\n")
            return None
        return name

    @staticmethod
    def get_model_car():
        model = input("Enter car model: ").strip()
        if not model:
            print("Error: Model cannot be empty.\n")
            return None
        return model

    @staticmethod
    def get_year_car():
        while True:
            year = input("Enter car year (YYYY): ").strip()
            if not year.isdigit():
                print("Error: Year must be a number.\n")
                continue
            if len(year) != 4:
                print("Error: Year must have 4 digits.\n")
                continue
            return year

    @staticmethod
    def get_service_type():
        service_type = input("\nEnter service type: ").strip()
        if not service_type:
            print("Error: Service type cannot be empty.\n")
            return None
        return service_type
    
    @staticmethod
    def get_service_date():
        service_date = input("Enter service date (YYYY-MM-DD): ").strip()
        if not service_date:
            print("Error: Service date cannot be empty.\n")
            return None
        return service_date
    
    @staticmethod
    def get_next_service_date():
        next_service_date = input("Enter next service date (YYYY-MM-DD): ").strip()
        if not next_service_date:
            return None
        return next_service_date
    
    @staticmethod
    def get_notes():
        notes = input("Enter notes: ").strip()
        if not notes:
            print("Error: Notes cannot be empty.\n")
            return None
        return notes

    @staticmethod
    def confirm_action(message="Are you sure? (y/n): "):
        return input(message).strip().lower() == "y"
