import mysql.connector
from app.auth.password_hashing import hash_password


class DatabaseHandler:
    def __init__(
        self, host="localhost", user="root", password="", database="service_track"
    ):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            self.cursor = self.connection.cursor(dictionary=True)
        except mysql.connector.Error as e:
            print(f"Error: {str(e)}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        if exc_type:
            print(f"Error: {exc_value}")
        return True

    def execute_query(self, query, params=None):
        # Execute a query and return the result
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error: {str(e)}")

    def execute_commit(self, query, params=None):
        # Execute a query and commit the changes (e.g. INSERT, UPDATE, DELETE)
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error: {str(e)}")

    def fetch_one(self, query, params=None):
        # Fetch a single row from a query
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchone()
        except mysql.connector.Error as e:
            print(f"Error: {str(e)}")

    def load_users(self):
        try:
            query = "SELECT * FROM users"
            self.cursor.execute(query)
            return {
                row["username"]: {
                    "username": row["username"],
                    "email": row["email"],
                    "password": row["password"],
                    "role": row["role"],
                }
                for row in self.cursor.fetchall()
            }
        except mysql.connector.Error as e:
            print(f"Error: {str(e)}")
            return None


# The DatabaseHandler class is similar to the FileHandler class, but it interacts with a MySQL database
# instead of a JSON file. The load_users method retrieves all users from the users table, while the save_users
# method inserts a new user into the table. The close method closes the connection and cursor to the database.
