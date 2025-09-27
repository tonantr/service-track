CREATE DATABASE service_track;

USE service_track;

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    role ENUM('admin','user') NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS cars (
    car_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    vin VARCHAR(17) NOT NULL UNIQUE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS login_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    login_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    logout_time DATETIME,
    ip_address VARCHAR(45),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    car_id INT NOT NULL,
    mileage INT NOT NULL,
    service_type VARCHAR(100) NOT NULL,
    service_date DATE NOT NULL,
    next_service_date DATE,
    cost DECIMAL(10,2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (car_id) REFERENCES cars(car_id) ON DELETE CASCADE
);

-- USERS
INSERT INTO users VALUES (2,'jayden','user','jane@example.com','1234');
INSERT INTO users VALUES (4,'user','user','bob@example.com.ca','1234');
INSERT INTO users VALUES (5,'admintest','admin','admintest@yahoo.com','1234');
INSERT INTO users VALUES (6,'tonan','admin','tonan@hotmail.com','1234');
INSERT INTO users VALUES (7,'admintest2','admin','test2@yahoo.ca','1234');
INSERT INTO users VALUES (9,'testuser02','admin','jane003@example.com','1234');
INSERT INTO users VALUES (11,'testuser04','user','jane005@example.com.ca','1234');
INSERT INTO users VALUES (12,'test','user','123@test.ca','1234');

-- CARS
INSERT INTO cars VALUES (6,2,'Hyundai','Elantra',2018,'2HGCM82633A123456');
INSERT INTO cars VALUES (7,2,'Mazda','Mazda3',2021,'2HGCM82633A654321');
INSERT INTO cars VALUES (8,2,'Volkswagen','Jetta',2019,'2HGCM82633A789012');
INSERT INTO cars VALUES (9,2,'Subaru','Impreza',2020,'2HGCM82633A345678');
INSERT INTO cars VALUES (10,2,'Kia','Forte',2022,'2HGCM82633A567890');
INSERT INTO cars VALUES (11,4,'BMW','3 Series',2020,'3HGCM82633A123456');
INSERT INTO cars VALUES (13,4,'Audi','A4',2019,'3HGCM82633A789012');
INSERT INTO cars VALUES (14,4,'Lexus','IS',2022,'3HGCM82633A345678');
INSERT INTO cars VALUES (15,4,'Tesla','Model 3',2023,'3HGCM82633A567890');
INSERT INTO cars VALUES (16,5,'Toyota','Corolla',2020,'1HGCM82633A123456');
INSERT INTO cars VALUES (17,5,'Honda','Civic',2021,'1HGCM82633A654321');
INSERT INTO cars VALUES (18,5,'Ford','Focus',2019,'1HGCM82633A789012');
INSERT INTO cars VALUES (19,5,'Chevrolet','Malibu02',2022,'1HGCM82633A345699');
INSERT INTO cars VALUES (20,5,'Nissan','Sentra',2020,'1HGCM82633A567890');
INSERT INTO cars VALUES (21,6,'Hyundai','Elantra',2018,'2HGCM82633A123456');
INSERT INTO cars VALUES (22,6,'Mazda','Mazda3',2021,'2HGCM82633A654321');
INSERT INTO cars VALUES (23,6,'Volkswagen','Jetta',2019,'2HGCM82633A789012');
INSERT INTO cars VALUES (24,6,'Subaru','Impreza',2020,'2HGCM82633A345678');
INSERT INTO cars VALUES (25,6,'Kia','Forte',2022,'2HGCM82633A567890');
INSERT INTO cars VALUES (26,11,'testcar','xx1',2023,'2HGCM82633A123456');
INSERT INTO cars VALUES (27,11,'Carabc','testabc',2023,'2HGCM82633A003456');

-- LOGIN_LOGS
INSERT INTO login_logs VALUES (3,6,'2025-03-11 15:41:14.794732','2025-03-11 19:41:14','127.0.0.1');
INSERT INTO login_logs VALUES (4,6,'2025-03-11 15:45:03.724634','2025-03-11 19:45:03','127.0.0.1');
INSERT INTO login_logs VALUES (5,6,'2025-03-11 16:21:36.129913','2025-03-11 20:21:36','127.0.0.1');


-- SERVICES
INSERT INTO services VALUES (1,6,12000,'Oil Change','2024-02-10','2024-08-10',55,'Synthetic oil change');
INSERT INTO services VALUES (2,6,25000,'Tire Rotation','2024-09-15',NULL,40,'Checked alignment');



