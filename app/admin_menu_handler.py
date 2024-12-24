class AdminMenuHandler:
    def __init__(self, login_module):
        self.login_module = login_module

    def handle_add_user(self):
        username = input("\nEnter new username: ").strip()
        password = input("Enter new password: ").strip()

        if username in self.login_module.users:
            print(f"Error: username already exists.\n")
        else:
            self.login_module.add_user(username, password)
            self.handle_list_users()

    def handle_list_users(self):
        print("\n*** List of Users ***\n")
        if not self.login_module.users:
            print("No users found.\n")
            return

        print(f"{'Username':<15} {'Password':<15}")
        print("-" * 30)

        for username, _ in self.login_module.users.items():
            print(f"{username:<15} {"********":<15}")

        print()

        input("\nPress Enter to go back to the Menu.\n")

    def handle_exit(self):
        confirm_exit = input("Are you sure? (y/n): ").strip().lower()
        if confirm_exit == "y":
            return True
        else:
            return False
