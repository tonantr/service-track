from app.auth.password_hashing import hash_password
from app.database.database_handler import DatabaseHandler


class AdminDatabaseHandler(DatabaseHandler):
    def add_user(self, username, password, email, role):
        hashed_password = hash_password(password)
        query = "INSERT INTO users (username, password, email, role) VALUES (%s, %s, %s, %s)"
        self.execute_commit(query, (username, hashed_password, email, role))

    def load_users(self):
        query = "SELECT user_id, username, role, email FROM users"
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

    def delete_user(self, user_id):
        query_services = "DELETE FROM services WHERE car_id in (SELECT car_id FROM cars WHERE user_id = %s)"
        self.execute_commit(query_services, (user_id,))

        query_cars = "DELETE FROM cars WHERE user_id = %s"
        self.execute_commit(query_cars, (user_id,))

        query_user = "DELETE FROM users WHERE user_id = %s"
        self.execute_commit(query_user, (user_id,))

    def load_cars(self):
        query = """
        SELECT 
            c.car_id, 
            c.name, 
            c.model, 
            c.year,
            c.vin, 
            u.username AS owner,
            IFNULL(GROUP_CONCAT(DISTINCT s.service_type ORDER BY s.service_date SEPARATOR ', '), 'No services') AS services
        FROM cars c
        LEFT JOIN users u ON c.user_id = u.user_id
        LEFT JOIN services s ON c.car_id = s.car_id
        GROUP BY c.car_id, c.name, c.model, c.year, u.username;
        """
        return self.execute_query(query)

    def load_cars_by_vin(self, vin):
        query = "SELECT car_id, name, model, year FROM cars WHERE vin = %s"
        return self.fetch_one(query, (vin,))

    def add_car(self, name, model, year, vin, user_id):
        query = "INSERT INTO cars (name, model, year, vin, user_id) VALUES (%s, %s, %s, %s, %s)"
        self.execute_commit(query, (name, model, year, vin, user_id))

    def update_car(self, car_id, **kwargs):
        if not kwargs:
            raise ValueError("\nNo fields to update.\n")
        fields = [f"{key} = %s" for key in kwargs.keys()]
        values = list(kwargs.values())

        query = f"UPDATE cars SET {', '.join(fields)} WHERE car_id = %s"
        values.append(car_id)
        self.execute_commit(query, tuple(values))

    def delete_car(self, car_id):
        query_services = "DELETE FROM services WHERE car_id = %s"
        self.execute_commit(query_services, (car_id,))

        query_car = "DELETE FROM cars WHERE car_id = %s"
        self.execute_commit(query_car, (car_id,))

    def load_services(self):
        query = """
        SELECT 
            s.service_id, 
            c.name AS car_name,
            s.mileage,
            s.service_type, 
            s.service_date,
            s.next_service_date,
            s.cost,
            s.notes
        FROM services s
        LEFT JOIN cars c ON s.car_id = c.car_id
        ORDER BY s.service_date ASC, s.next_service_date ASC;
    """
        return self.execute_query(query)

    def load_services_by_car_id(self, car_id):
        query = "SELECT service_id, mileage, service_type, service_date, next_service_date, cost, notes FROM services WHERE car_id = %s"
        return self.execute_query(query, (car_id,))

    def add_service(
        self, service_mileage, service_type, service_date, cost, notes, car_id, next_service_date=None
    ):
        query = "INSERT INTO services (mileage, service_type, service_date, next_service_date, cost, notes, car_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.execute_commit(
            query, (service_mileage, service_type, service_date, next_service_date, cost, notes, car_id)
        )

    def update_service(self, service_id, **kwargs):
        if not kwargs:
            raise ValueError("\nNo fields to update.\n")

        fields = [f"{key} = %s" for key in kwargs.keys()]
        values = list(kwargs.values())

        query = f"UPDATE services SET {" , ".join(fields)} WHERE service_id = %s"
        values.append(service_id)
        self.execute_commit(query, tuple(values))

    def delete_service(self, service_id):
        query = "DELETE FROM services WHERE service_id = %s"
        self.execute_commit(query, (service_id,))
