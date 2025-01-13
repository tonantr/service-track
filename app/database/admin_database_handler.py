from app.auth.password_hashing import hash_password
from app.database.database_handler import DatabaseHandler


class AdminDatabaseHandler(DatabaseHandler):
    def add_user(self, username, password, email, role):
        hashed_password = hash_password(password)
        query = "INSERT INTO users (username, password, email, role) VALUES (%s, %s, %s, %s)"
        self.execute_commit(query, (username, hashed_password, email, role))

    def load_users(self):
        query = "SELECT * FROM users"
        return self.execute_query(query)
    
    def update_user(self, username, email, role):
        query = "UPDATE users SET email = %s, role = %s WHERE username = %s"
        self.execute_commit(query, (email, role, username))
