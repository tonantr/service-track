import mysql.connector


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
                "role": row["role"]
        }
        for row in self.cursor.fetchall()
        }

    def save_users(self, username, password):
        try:
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            self.cursor.execute(query, (username, password))
            self.connection.commit()
        except mysql.connector.IntegrityError:
            print(f"Error: User {username} already exists.")
    
    def update_password(self, username, hashed_password):
        query = "UPDATE users SET password = %s WHERE username = %s"
        self.cursor.execute(query, (hashed_password, username))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

# The DatabaseHandler class is similar to the FileHandler class, but it interacts with a MySQL database 
# instead of a JSON file. The load_users method retrieves all users from the users table, while the save_users 
# method inserts a new user into the table. The close method closes the connection and cursor to the database.