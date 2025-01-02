from app.auth.password_hashing import hash_password
from app.database.database_handler import DatabaseHandler


class AdminDatabaseHandler(DatabaseHandler):
    def add_user(self, username, password, email, role):
        hashed_password = hash_password(password)
        query = "INSERT INTO users (username, password, email, role) VALUES (%s, %s, %s, %s)"
        self.execute_commit(query, (username, hashed_password, email, role))
       