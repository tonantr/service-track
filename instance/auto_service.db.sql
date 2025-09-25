BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "cars" (
	"car_id"	INTEGER NOT NULL,
	"user_id"	INTEGER NOT NULL,
	"name"	VARCHAR(50) NOT NULL,
	"model"	VARCHAR(50) NOT NULL,
	"year"	INTEGER NOT NULL,
	"vin"	VARCHAR(17) NOT NULL,
	PRIMARY KEY("car_id"),
	FOREIGN KEY("user_id") REFERENCES "users"("user_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "login_logs" (
	"log_id"	INTEGER,
	"user_id"	INTEGER NOT NULL,
	"login_time"	DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"logout_time"	DATETIME,
	"ip_address"	TEXT,
	PRIMARY KEY("log_id"),
	FOREIGN KEY("user_id") REFERENCES "users"("user_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "services" (
	"service_id"	INTEGER NOT NULL,
	"car_id"	INTEGER NOT NULL,
	"mileage"	INTEGER NOT NULL,
	"service_type"	TEXT NOT NULL,
	"service_date"	DATE NOT NULL,
	"next_service_date"	DATE,
	"cost"	NUMERIC(10, 2) NOT NULL,
	"notes"	TEXT,
	PRIMARY KEY("service_id"),
	FOREIGN KEY("car_id") REFERENCES "cars"("car_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "users" (
	"user_id"	INTEGER NOT NULL,
	"username"	VARCHAR(50) NOT NULL,
	"role"	VARCHAR(5) NOT NULL,
	"email"	VARCHAR(100) NOT NULL,
	"password"	VARCHAR(255) NOT NULL,
	UNIQUE("email"),
	PRIMARY KEY("user_id")
);
INSERT INTO "cars" VALUES (6,2,'Hyundai','Elantra',2018,'2HGCM82633A123456');
INSERT INTO "cars" VALUES (7,2,'Mazda','Mazda3',2021,'2HGCM82633A654321');
INSERT INTO "cars" VALUES (8,2,'Volkswagen','Jetta',2019,'2HGCM82633A789012');
INSERT INTO "cars" VALUES (9,2,'Subaru','Impreza',2020,'2HGCM82633A345678');
INSERT INTO "cars" VALUES (10,2,'Kia','Forte',2022,'2HGCM82633A567890');
INSERT INTO "cars" VALUES (11,4,'BMW','3 Series',2020,'3HGCM82633A123456');
INSERT INTO "cars" VALUES (13,4,'Audi','A4',2019,'3HGCM82633A789012');
INSERT INTO "cars" VALUES (14,4,'Lexus','IS',2022,'3HGCM82633A345678');
INSERT INTO "cars" VALUES (15,4,'Tesla','Model 3',2023,'3HGCM82633A567890');
INSERT INTO "cars" VALUES (16,5,'Toyota','Corolla',2020,'1HGCM82633A123456');
INSERT INTO "cars" VALUES (17,5,'Honda','Civic',2021,'1HGCM82633A654321');
INSERT INTO "cars" VALUES (18,5,'Ford','Focus',2019,'1HGCM82633A789012');
INSERT INTO "cars" VALUES (19,5,'Chevrolet','Malibu02',2022,'1HGCM82633A345699');
INSERT INTO "cars" VALUES (20,5,'Nissan','Sentra',2020,'1HGCM82633A567890');
INSERT INTO "cars" VALUES (21,6,'Hyundai','Elantra',2018,'2HGCM82633A123456');
INSERT INTO "cars" VALUES (22,6,'Mazda','Mazda3',2021,'2HGCM82633A654321');
INSERT INTO "cars" VALUES (23,6,'Volkswagen','Jetta',2019,'2HGCM82633A789012');
INSERT INTO "cars" VALUES (24,6,'Subaru','Impreza',2020,'2HGCM82633A345678');
INSERT INTO "cars" VALUES (25,6,'Kia','Forte',2022,'2HGCM82633A567890');
INSERT INTO "cars" VALUES (26,11,'testcar','xx1',2023,'2HGCM82633A123456');
INSERT INTO "cars" VALUES (27,11,'Carabc','testabc',2023,'2HGCM82633A003456');
INSERT INTO "login_logs" VALUES (3,6,'2025-03-11 15:41:14.794732','2025-03-11 19:41:14','127.0.0.1');
INSERT INTO "login_logs" VALUES (4,6,'2025-03-11 15:45:03.724634','2025-03-11 19:45:03','127.0.0.1');
INSERT INTO "login_logs" VALUES (5,6,'2025-03-11 16:21:36.129913','2025-03-11 20:21:36','127.0.0.1');
INSERT INTO "login_logs" VALUES (6,6,'2025-03-11 16:33:00.950570','2025-03-11 20:33:00','127.0.0.1');
INSERT INTO "login_logs" VALUES (7,6,'2025-03-11 16:37:51.981619','2025-03-11 20:37:51','127.0.0.1');
INSERT INTO "login_logs" VALUES (8,6,'2025-03-11 16:41:26.548232','2025-03-11 20:41:26','127.0.0.1');
INSERT INTO "login_logs" VALUES (9,6,'2025-03-11 17:41:13.002639','2025-03-11 21:41:13','127.0.0.1');
INSERT INTO "login_logs" VALUES (10,6,'2025-03-11 17:43:51.697989','2025-03-11 21:43:51','127.0.0.1');
INSERT INTO "login_logs" VALUES (11,6,'2025-03-11 18:08:22.687489','2025-03-11 22:08:22','127.0.0.1');
INSERT INTO "login_logs" VALUES (12,6,'2025-03-11 18:13:05.432161','2025-03-11 22:13:05','127.0.0.1');
INSERT INTO "login_logs" VALUES (13,6,'2025-03-11 18:52:27.489364','2025-03-11 22:52:27','127.0.0.1');
INSERT INTO "login_logs" VALUES (15,6,'2025-03-11 19:08:42.391216','2025-03-12 03:23:01.616633','127.0.0.1');
INSERT INTO "login_logs" VALUES (16,6,'2025-03-11 21:31:54.921809','2025-03-12 03:23:01.418612','127.0.0.1');
INSERT INTO "login_logs" VALUES (17,6,'2025-03-11 21:32:15.368372','2025-03-12 03:23:00.583891','127.0.0.1');
INSERT INTO "login_logs" VALUES (18,6,'2025-03-11 21:34:55.077457','2025-03-12 03:22:56.246030','127.0.0.1');
INSERT INTO "login_logs" VALUES (19,6,'2025-03-11 21:59:56.972749','2025-03-12 03:22:56.050117','127.0.0.1');
INSERT INTO "login_logs" VALUES (20,6,'2025-03-11 22:19:44.081817','2025-03-12 03:22:55.828661','127.0.0.1');
INSERT INTO "login_logs" VALUES (21,6,'2025-03-11 22:22:26.729422','2025-03-12 03:22:55.630483','127.0.0.1');
INSERT INTO "login_logs" VALUES (22,6,'2025-03-11 22:23:19.048043','2025-03-12 03:22:55.146930','127.0.0.1');
INSERT INTO "login_logs" VALUES (23,6,'2025-03-11 22:27:01.103793','2025-03-12 03:22:37.929190','127.0.0.1');
INSERT INTO "login_logs" VALUES (24,6,'2025-03-12 03:16:19.849257','2025-03-12 03:22:32.380108','127.0.0.1');
INSERT INTO "login_logs" VALUES (25,6,'2025-03-12 03:59:12.124414','2025-03-12 03:59:33.505803','127.0.0.1');
INSERT INTO "login_logs" VALUES (26,4,'2025-03-12 03:59:40.218273','2025-03-12 04:00:01.557278','127.0.0.1');
INSERT INTO "login_logs" VALUES (27,6,'2025-03-12 04:00:07.650624',NULL,'127.0.0.1');
INSERT INTO "login_logs" VALUES (28,6,'2025-03-12 13:34:19.794019',NULL,'127.0.0.1');
INSERT INTO "login_logs" VALUES (29,4,'2025-03-12 22:52:28.536938','2025-03-12 22:53:00.223075','127.0.0.1');
INSERT INTO "login_logs" VALUES (30,6,'2025-03-12 22:53:06.345312','2025-03-12 22:53:26.351959','127.0.0.1');
INSERT INTO "login_logs" VALUES (31,6,'2025-03-21 16:58:16.938106',NULL,'127.0.0.1');
INSERT INTO "login_logs" VALUES (32,6,'2025-03-21 16:58:18.522954',NULL,'127.0.0.1');
INSERT INTO "login_logs" VALUES (33,6,'2025-03-21 16:58:20.987368',NULL,'127.0.0.1');
INSERT INTO "login_logs" VALUES (34,6,'2025-03-21 16:58:21.135931',NULL,'127.0.0.1');
INSERT INTO "login_logs" VALUES (35,6,'2025-03-21 16:58:21.364605',NULL,'127.0.0.1');
INSERT INTO "login_logs" VALUES (36,6,'2025-03-21 17:08:43.696704',NULL,'127.0.0.1');
INSERT INTO "login_logs" VALUES (37,6,'2025-03-21 17:28:07.442325',NULL,'127.0.0.1');
INSERT INTO "login_logs" VALUES (38,6,'2025-03-21 17:30:00.711686',NULL,'127.0.0.1');
INSERT INTO "login_logs" VALUES (39,6,'2025-03-21 17:51:45.112071',NULL,'127.0.0.1');
INSERT INTO "login_logs" VALUES (40,6,'2025-03-21 17:52:04.454531',NULL,'127.0.0.1');
INSERT INTO "login_logs" VALUES (41,6,'2025-03-21 17:53:31.152563',NULL,'127.0.0.1');
INSERT INTO "services" VALUES (1,6,12000,'Oil Change','2024-02-10','2024-08-10',55,'Synthetic oil change');
INSERT INTO "services" VALUES (2,6,25000,'Tire Rotation','2024-09-15',NULL,40,'Checked alignment');
INSERT INTO "services" VALUES (3,6,40000,'Brake Pad Replacement','2025-03-20','2026-03-20',200,'Front brake pads replaced');
INSERT INTO "services" VALUES (4,6,52000,'Battery Replacement','2025-07-05',NULL,150,'Installed new battery');
INSERT INTO "services" VALUES (5,6,68000,'Transmission Fluid Change','2026-01-10','2031-01-10',100,'Full transmission flush');
INSERT INTO "services" VALUES (6,7,15000,'Oil Change','2024-03-01','2024-09-01',58,'Changed synthetic oil');
INSERT INTO "services" VALUES (7,7,32000,'Brake Inspection','2024-10-10',NULL,35,'Brake pads checked, no replacement needed');
INSERT INTO "services" VALUES (8,7,46000,'Tire Rotation','2025-04-25','2025-10-25',45,'Rotated tires and adjusted pressure');
INSERT INTO "services" VALUES (9,7,58000,'Coolant Flush','2025-11-05',NULL,90,'Replaced coolant fluid');
INSERT INTO "services" VALUES (10,7,73000,'Spark Plug Replacement','2026-06-15','2031-06-15',120,'Replaced all spark plugs');
INSERT INTO "services" VALUES (11,8,17000,'Brake Fluid Flush','2024-04-05',NULL,85,'Brake fluid changed');
INSERT INTO "services" VALUES (12,8,30000,'Oil Change','2024-10-20','2025-04-20',60,'Full synthetic oil change');
INSERT INTO "services" VALUES (13,8,47000,'Battery Replacement','2025-06-15',NULL,155,'Installed new battery');
INSERT INTO "services" VALUES (14,8,59000,'Transmission Fluid Change','2026-01-05','2031-01-05',110,'Full transmission flush');
INSERT INTO "services" VALUES (15,8,76000,'Tire Rotation','2026-06-30','2026-12-30',38,'Tires rotated');
INSERT INTO "services" VALUES (16,9,14000,'Brake Pad Replacement','2024-05-10','2025-05-10',210,'Rear brake pads replaced');
INSERT INTO "services" VALUES (17,9,31000,'Oil Change','2024-11-15',NULL,55,'Changed synthetic oil');
INSERT INTO "services" VALUES (18,9,48000,'Tire Rotation','2025-06-25','2025-12-25',40,'Rotated tires');
INSERT INTO "services" VALUES (19,9,61000,'Battery Replacement','2026-02-05',NULL,160,'High-performance battery installed');
INSERT INTO "services" VALUES (20,9,78000,'Coolant Flush','2026-08-20','2031-08-20',95,'Replaced coolant fluid');
INSERT INTO "services" VALUES (21,10,14000,'Brake Pad Replacement','2024-05-10','2025-05-10',210,'Rear brake pads replaced');
INSERT INTO "services" VALUES (22,10,31000,'Oil Change','2024-11-15',NULL,55,'Changed synthetic oil');
INSERT INTO "services" VALUES (23,10,48000,'Tire Rotation','2025-06-25','2025-12-25',40,'Rotated tires');
INSERT INTO "services" VALUES (24,10,61000,'Battery Replacement','2026-02-05',NULL,160,'High-performance battery installed');
INSERT INTO "services" VALUES (25,10,78000,'Coolant Flush','2026-08-20','2031-08-20',95,'Replaced coolant fluid');
INSERT INTO "services" VALUES (26,11,12000,'Oil Change','2024-02-10','2024-08-10',55,'Synthetic oil change');
INSERT INTO "services" VALUES (27,11,25000,'Tire Rotation','2024-09-15',NULL,40,'Checked alignment');
INSERT INTO "services" VALUES (28,11,40000,'Brake Pad Replacement','2025-03-20','2026-03-20',200,'Front brake pads replaced');
INSERT INTO "services" VALUES (29,11,52000,'Battery Replacement','2025-07-05',NULL,150,'Installed new battery');
INSERT INTO "services" VALUES (30,11,68000,'Transmission Fluid Change','2026-01-10','2031-01-10',100,'Full transmission flush');
INSERT INTO "services" VALUES (31,26,12333,'Engine Diagnostics & Tune-up','2025-03-04','2025-07-04',123,'testefhg.');
INSERT INTO "services" VALUES (34,26,58000,'Spark Plug Replacement','2025-02-24',NULL,777,'test.');
INSERT INTO "services" VALUES (35,13,12000,'Oil Change','2024-02-10','2024-08-10',55,'Synthetic oil change');
INSERT INTO "services" VALUES (36,13,25000,'Tire Rotation','2024-09-15',NULL,40,'Checked alignment');
INSERT INTO "services" VALUES (37,13,40000,'Brake Pad Replacement','2025-03-20','2026-03-20',200,'Front brake pads replaced');
INSERT INTO "services" VALUES (38,13,52000,'Battery Replacement','2025-07-05',NULL,150,'Installed new battery');
INSERT INTO "services" VALUES (40,14,15000,'Oil Change','2024-03-01','2024-09-01',58,'Changed synthetic oil');
INSERT INTO "services" VALUES (41,14,32000,'Brake Inspection','2024-10-10',NULL,35,'Brake pads checked, no replacement needed');
INSERT INTO "services" VALUES (42,14,46000,'Tire Rotation','2025-04-25','2025-10-25',45,'Rotated tires and adjusted pressure');
INSERT INTO "services" VALUES (43,14,58000,'Coolant Flush','2025-11-05',NULL,90,'Replaced coolant fluid');
INSERT INTO "services" VALUES (44,14,73000,'Spark Plug Replacement','2026-06-15','2031-06-15',120,'Replaced all spark plugs');
INSERT INTO "services" VALUES (45,15,12000,'Oil Change','2024-02-10','2024-08-10',55,'Synthetic oil change');
INSERT INTO "services" VALUES (46,15,25000,'Tire Rotation','2024-09-15',NULL,40,'Checked alignment');
INSERT INTO "services" VALUES (47,15,40000,'Brake Pad Replacement','2025-03-20','2026-03-20',200,'Front brake pads replaced');
INSERT INTO "services" VALUES (48,15,52000,'Battery Replacement','2025-07-05',NULL,150,'Installed new battery');
INSERT INTO "services" VALUES (49,15,68000,'Transmission Fluid Change','2026-01-10','2031-01-10',100,'Full transmission flush');
INSERT INTO "services" VALUES (50,15,100000,'Engine Diagnostics & Tune-up','2025-03-07',NULL,0,NULL);
INSERT INTO "services" VALUES (52,14,200000,'Exhaust System Repair','2025-02-23',NULL,300,NULL);
INSERT INTO "services" VALUES (53,27,70000,'Headlight/Taillight Replacement','2025-03-03',NULL,2000,NULL);
INSERT INTO "users" VALUES (2,'jayden','user','jane@example.com','$2b$12$9jkhUFqksqBxGHukwufSEObSavbUPz1r6OLnkg4FV9LLg0DwL513C');
INSERT INTO "users" VALUES (4,'user','user','bob@example.com.ca','$2b$12$6XNcb4qZBkG8jMAFEs0A/ONvkdsSFZZL2dFGthp9UYUzd9gZlcNKe');
INSERT INTO "users" VALUES (5,'admintest','admin','admintest@yahoo.com','$2b$12$r8YyAj7i85knacjoz5/TDeDPb2BTsQGQP7SNTYAKhwL3gvUOqH6PC');
INSERT INTO "users" VALUES (6,'tonan','admin','tonan@hotmail.com','$2b$12$b9QIcrMfdtmJ/7jWoG5NOu/in8SabzTXQkHSor7vG37rjfdrWqHNm');
INSERT INTO "users" VALUES (7,'admintest2','admin','test2@yahoo.ca','$2b$12$5EYJtsoTuB74udIQT3heT.iLRnS0sIf1fz5E5FqBrnzv2EXo6mKVy');
INSERT INTO "users" VALUES (9,'testuser02','admin','jane003@example.com','$2b$12$DcuXdvLDFF3shiCP6VkK/OZ6a6y346PIrwGSUjCZnmT3YWwqiV9jK');
INSERT INTO "users" VALUES (11,'testuser04','user','jane005@example.com.ca','$2b$12$hU/CV7/p9UV5OfnfdBMjVudliaifjoOfJyjk.6AC4YrDXv8p7iHg.');
INSERT INTO "users" VALUES (12,'test','user','123@test.ca','$2b$12$cYjIUAoP6/xyV.E793G7sOaKnJhRJMgt2B8vMenGAt532kd5WeLh6');
COMMIT;
