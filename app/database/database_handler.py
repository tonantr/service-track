import mysql.connector
from app.auth.password_hashing import hash_password

class DatabaseHandler:
    def __init__(
        self,
        host="localhost",
        user="root",
        password="",
        database="service_track",
    ):
        self.connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def load_users(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        return {
            row["username"]: {
                "email": row["email"],
                "password": row["password"],
                "role": row["role"],
            }
            for row in self.cursor.fetchall()
        }

    def add_user(self, username, password, email, role):
        try:
            hashed_password = hash_password(password)
            query = "INSERT INTO users (username, password, email, role) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (username, hashed_password, email, role))
            self.connection.commit()
        except mysql.connector.IntegrityError as e:
            print(f"Error: {str(e)}")

    # def update_password(self, username, hashed_password):
    #     query = "UPDATE users SET password = %s WHERE username = %s"
    #     self.cursor.execute(query, (hashed_password, username))
    #     self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()


# The DatabaseHandler class is similar to the FileHandler class, but it interacts with a MySQL database
# instead of a JSON file. The load_users method retrieves all users from the users table, while the save_users
# method inserts a new user into the table. The close method closes the connection and cursor to the database.