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

    def update_user(self, user_id, username=None, role=None, email=None, password=None):
        fields = []
        values = []

        if username:
            fields.append("username = %s")
            values.append(username)
        if email:
            fields.append("email = %s")
            values.append(email)
        if role:
            fields.append("role = %s")
            values.append(role)
        if password:
            fields.append("password = %s")
            values.append(hash_password(password))
        if not fields:
            raise ValueError("No fields to update.")

        query = f"UPDATE users SET {', '.join(fields)} WHERE user_id = %s"
        values.append(user_id)
        self.execute_commit(query, tuple(values))
