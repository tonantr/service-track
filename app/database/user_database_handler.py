from app.database.database_handler import DatabaseHandler


class UserDatabaseHandler(DatabaseHandler):
    def load_user(self, username):
        query = "SELECT * FROM users WHERE username = %s"
        return self.fetch_one(query, (username,))

    def update_password(self, username, hashed_password):
        query = "UPDATE users SET password = %s WHERE username = %s"
        self.execute_commit(query, (hashed_password, username))
        
        