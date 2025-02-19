import mysql.connector
import os
import logging
from app.auth.password_hashing import hash_password

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(module)s - Line: %(lineno)d - %(message)s",
)


class DatabaseHandler:
    def __init__(self, host=None, port=None, user=None, password=None, database=None):
        self.host = host or os.getenv("MYSQL_HOST_LOCAL")  
        self.port = port or os.getenv("MYSQL_PORT_REMOTE")  
        self.user = user or os.getenv("MYSQL_USER")
        self.password = password or os.getenv("MYSQL_PASSWORD")
        self.database = database or os.getenv("MYSQL_DATABASE")

        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            self.cursor = self.connection.cursor(dictionary=True)
        except mysql.connector.Error as e:
            logging.error(f"Connection Error: {str(e)}")
            print(f"Error: {str(e)}")

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except mysql.connector.Error as e:
            logging.error(f"Close Error: {str(e)}")
            print(f"Error: {str(e)}")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        if exc_type:
            logging.error(f"Error: {exc_value}")
        return True

    def execute_query(self, query, params=None):
        # Execute a query and return the result
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            logging.error(f"Query Error: {str(e)} | Query: {query} | Params: {params}")
            print(f"Error: {str(e)}")

    def execute_commit(self, query, params=None):
        # Execute a query and commit the changes (e.g. INSERT, UPDATE, DELETE)
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
        except mysql.connector.Error as e:
            logging.error(f"Commit Error: {str(e)} | Query: {query} | Params: {params}")
            print(f"Error: {str(e)}")

    def fetch_one(self, query, params=None):
        # Fetch a single row from a query
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchone()
        except mysql.connector.Error as e:
            logging.error(f"Fetch Error: {str(e)} | Query: {query} | Params: {params}")
            print(f"Error: {str(e)}")

    def start_transaction(self):
        try:
            self.connection.start_transaction()
        except mysql.connector.Error as e:
            logging.error(f"Transaction Error: {str(e)}")
            print(f"Error: {str(e)}")

    def commit_transaction(self):
        try:
            self.connection.commit()
        except mysql.connector.Error as e:
            logging.error(f"Commit Error: {str(e)}")
            print(f"Error: {str(e)}")

    def rollback_transaction(self):
        try:
            self.connection.rollback()
        except mysql.connector.Error as e:
            logging.error(f"Rollback Error: {str(e)}")
            print(f"Error: {str(e)}")


# The DatabaseHandler class is similar to the FileHandler class, but it interacts with a MySQL database
# instead of a JSON file. The load_users method retrieves all users from the users table, while the save_users
# method inserts a new user into the table. The close method closes the connection and cursor to the database.
