from bcrypt import hashpw, gensalt
import mysql.connector

def hash_password(password):
    return hashpw(password.encode(), gensalt()).decode()

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="service_track"
)
cursor = connection.cursor()

admin_plaintext_password = "password123"
hashed_password = hash_password(admin_plaintext_password)

cursor.execute("Update users SET password = %s WHERE username = %s", (hashed_password, "admin"))
connection.commit()

print("Admin password updated successfully.")

cursor.close()
connection.close()