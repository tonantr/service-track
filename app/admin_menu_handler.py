from app.menu import Menu

class AdminMenuHandler:
    def __init__(self, login_module):
        self.login_module = login_module

    def handle_add_user(self):
        cancel = input("\nAdd new user? (y/n): ").strip().lower()
        if cancel == "n":
            self.handle_list_users()
            return

        username = Menu.get_username()
        if not username:
            return
        
        password = input("Enter new password: ").strip()

        email = Menu.get_email()
        if not email:
            return
        
        role = Menu.get_role()
        if role is None:
            return

        if username in self.login_module.users:
            print(f"Error: username already exists.\n")
        elif any(user[email] == email for user in self.login_module.users.values()):
            print(f"Error: email already exists.\n")
        else:
            self.login_module.add_user(username, password, email, role)
            print(f"User {username} added successfully.\n")
            self.handle_list_users()

    def handle_list_users(self):
        print("\n*** List of Users ***\n")
        if not self.login_module.users:
            print("No users found.\n")
            return

        print(f"{'Username':<15} {'Email':<25} {'Password':<15} {'Role':<10}")
        print("-" * 65)

        for username, details in self.login_module.users.items():
            print(
                f"{username:<15} {details['email']: <25} {"********":<15} {details['role']:<10}"
            )

        print()
        input("\nPress Enter to go back to the Menu.\n")
