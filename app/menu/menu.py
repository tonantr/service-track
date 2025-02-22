class Menu:

    @staticmethod
    def display_main_menu():
        print("\nMain Menu:")
        print("1. Login")
        print("2. Exit\n")
        return input("Enter your choice: ")

    @staticmethod
    def display_menu(menu_options, menu_context="Menu"):
        print(f"\n{menu_context}:\n")
        for key, value in menu_options.items():
            print(f"{key}. {value}")
        return input("Enter your choice: ")

    @staticmethod
    def handle_invalid_input(message="Invalid input"):
        print(f"\n{message}\n")

    @staticmethod
    def get_username():
        username = input("\nEnter new username: ").strip()
        if not username:
            print("\nUsername cannot be empty.\n")
            return None
        return username

    @staticmethod
    def get_email():
        email = input("Enter email: ").strip()
        if not email:
            print("\nError: Email cannot be empty.\n")
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
            print("\nInvalid role number.\n")
            return None

        if role == 1:
            return "admin"
        elif role == 2:
            return "user"
        else:
            print("\nInvalid role number.\n")
            return None

    @staticmethod
    def get_name_car():
        name = input("\nEnter car name: ").strip()
        if not name:
            print("\nError: Name cannot be empty.\n")
            return None
        return name

    @staticmethod
    def get_model_car():
        model = input("Enter car model: ").strip()
        if not model:
            print("\nError: Model cannot be empty.\n")
            return None
        return model

    @staticmethod
    def get_year_car():
        while True:
            year = input("Enter car year (YYYY): ").strip()
            if not year.isdigit():
                print("\nError: Year must be a number.\n")
                continue
            if len(year) != 4:
                print("\nError: Year must have 4 digits.\n")
                continue
            return year

    @staticmethod
    def get_vin_car():
        vin = input("Enter the VIN to look up (or type 'exit'): ").strip()
        if vin.lower() == "exit":
            return
        if not vin or len(vin) != 17:
            print("\nError: VIN must be exactly 17 characters.\n")
            return None
        
        return vin

    @staticmethod
    def get_service_mileage():
        service_mileage = input("\nEnter service mileage: ").strip()
            
        if not service_mileage:
            print("\nError: Service mileage cannot be empty.\n")
            return None
            
        if not service_mileage.isdigit():
            print("\nError: Service mileage must be a positive number.\n")
            return None
        
        return int(service_mileage)  

    @staticmethod
    def get_service_type():
        service_type = input("Enter service type: ").strip()
        if not service_type:
            print("\nError: Service type cannot be empty.\n")
            return None
        return service_type

    @staticmethod
    def get_service_date():
        service_date = input("Enter service date (YYYY-MM-DD): ").strip()
        if not service_date:
            print("\nError: Service date cannot be empty.\n")
            return None
        return service_date

    @staticmethod
    def get_next_service_date():
        next_service_date = input("Enter next service date (YYYY-MM-DD): ").strip()
        if not next_service_date:
            return None
        return next_service_date

    @staticmethod
    def get_service_cost():
        service_cost = input("Enter service cost: ").strip()

        if not service_cost:
            print("\nError: Service cost cannot be empty.\n")
            return None

        try:
            cost = float(service_cost)
            if cost < 0:
                print("\nError: Service cost cannot be negative.\n")
                return None
            return cost
        except ValueError:
            print("\nError: Service cost must be a valid number.\n")
            return None
           
    @staticmethod
    def get_notes():
        notes = input("Enter notes: ").strip()
        return notes

    @staticmethod
    def confirm_action(message="Are you sure? (y/n): "):
        return input(message).strip().lower() == "y"
