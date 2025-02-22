from app.database.database_handler import DatabaseHandler
import logging


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
        return result["COUNT(*)"] > 0

    def find_car_by_name_and_model(self, user_id, name, model):
        query = """
        SELECT COUNT(*)
        FROM cars
        WHERE user_id = %s AND LOWER(name) = %s AND LOWER(model) = %s
        """
        result = self.fetch_one(query, (user_id, name.lower(), model.lower()))
        return result["COUNT(*)"] > 0

    def load_cars(self, userid):
        query = """
        SELECT car_id, user_id, name, model, year, vin 
        FROM cars 
        WHERE user_id = %s
        """
        return self.execute_query(query, (userid,))

    def load_user_car_by_vin(self, user_id, vin):
        query = "SELECT car_id, name, model, year FROM cars WHERE vin = %s AND user_id = %s"
        return self.fetch_one(query, (vin, user_id))

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

    def delete_car_and_related_services(self, car_id):
        try:
            self.start_transaction()

            query_service = "DELETE FROM services WHERE car_id = %s"
            self.execute_commit(query_service, (car_id,))

            query_car = "DELETE FROM cars WHERE car_id = %s"
            self.execute_commit(query_car, (car_id,))

            self.commit_transaction()
            logging.info(f"Successfully deleted car {car_id} and related services.")
        except Exception as e:
            self.rollback_transaction()
            logging.error(
                f"Failed to delete car {car_id} and related services: {str(e)}"
            )
            raise e

    def load_services(self, car_id):
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
            WHERE s.car_id = %s
            ORDER BY s.service_date ASC, s.next_service_date ASC;
        """
        return self.execute_query(query, (car_id,))

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

        query = f"UPDATE services SET {', '.join(fields)} WHERE service_id = %s"
        values.append(service_id)
        self.execute_commit(query, tuple(values))

    def delete_service(self, service_id):
        query = "DELETE FROM services WHERE service_id = %s"
        self.execute_commit(query, (service_id,))
