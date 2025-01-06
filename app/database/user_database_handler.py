from app.database.database_handler import DatabaseHandler


class UserDatabaseHandler(DatabaseHandler):
    def load_user(self, username):
        query = "SELECT * FROM users WHERE username = %s"
        return self.fetch_one(query, (username,))

    def update_password(self, username, hashed_password):
        query = "UPDATE users SET password = %s WHERE username = %s"
        self.execute_commit(query, (hashed_password, username))
        
    def update_email(self, username, email):
        query = "UPDATE users SET email = %s WHERE username = %s"
        self.execute_commit(query, (email, username))

    def load_user_by_email(self, email):
        query = "SELECT COUNT(*) FROM users WHERE email = %s"
        result = self.fetch_one(query, (email,)) 
        return result['COUNT(*)'] > 0