CREATE DATABASE lux_cars;
USE lux_cars;

CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    user_mail VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    color VARCHAR(50),
    rented_by INT,
    image_path VARCHAR(255),
    price DECIMAL(15, 2),
    FOREIGN KEY (rented_by) REFERENCES users(user_id)
);


CREATE TABLE IF NOT EXISTS borrows (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    car_id INT NOT NULL,          
    borrow_date DATE NOT NULL,
    return_date DATE DEFAULT NULL, 
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (car_id) REFERENCES cars(id)
);

CREATE TABLE available_cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    image_path VARCHAR(255),
    price DECIMAL(10, 2) NOT NULL 
);

-- Inserting Users
INSERT INTO users (user_id, name, address, user_mail) VALUES
(1, 'Alice Johnson', '123 Elm Street', 'alice@gmail.com'),
(2, 'Bob Smith', '456 Maple Avenue', 'bob@gmail.com'),
(3, 'Charlie Brown', '789 Pine Lane', 'charlie@yahoo.com'),
(4, 'Diana Prince', '101 Oak Boulevard', 'diana@hotmail.com'),
(5, 'Ethan Hunt', '202 Cedar Road', 'ethan@gmail.com'),
(6, 'Fiona Apple', '303 Birch Street', 'fiona@yahoo.com');

-- Inserting Cars
INSERT INTO cars (make, model, year, color, rented_by, image_path, price) VALUES
('Aston Martin', 'DB11', 2021, 'Silver', NULL, 'D:/CS Project/Car Rental/AstonMartinDB11.jpg', 950000.00),
('Bentley', 'Continental GT', 2022, 'Black', NULL, 'D:/CS Project/Car Rental/BentleyContinentalGT.jpg', 900000.00),
('Ferrari', '488 GTB', 2020, 'Red', NULL, 'D:/CS Project/Car Rental/Ferrari488GTB.jpg', 980000.00),
('Lamborghini', 'Huracán', 2021, 'Yellow', NULL, 'D:/CS Project/Car Rental/LamborghiniHuracan.jpg', 1000000.00),
('Porsche', '911 Turbo S', 2022, 'White', NULL, 'D:/CS Project/Car Rental/Porsche911TurboS.jpg', 850000.00),
('Rolls-Royce', 'Phantom', 2023, 'Gray', NULL, 'D:/CS Project/Car Rental/RollsRoycePhantom.jpg', 990000.00),
('Maserati', 'GranTurismo', 2021, 'Blue', NULL, 'D:/CS Project/Car Rental/MaseratiGranTurismo.jpg', 870000.00),
('Mercedes-Benz', 'S-Class', 2022, 'Dark Green', NULL, 'D:/CS Project/Car Rental/MercedesBenzSClass.jpg', 860000.00),
('McLaren', '720S', 2021, 'Orange', NULL, 'D:/CS Project/Car Rental/McLaren720S.jpg', 970000.00),
('Bugatti', 'Chiron', 2023, 'Light Blue', NULL, 'D:/CS Project/Car Rental/BugattiChiron.jpg', 1000000.00),
('Jaguar', 'F-Type', 2021, 'Black', NULL, 'D:/CS Project/Car Rental/JaguarFType.jpg', 860000.00),
('Tesla', 'Model S', 2022, 'White', NULL, 'D:/CS Project/Car Rental/TeslaModelS.jpg', 850000.00),
('BMW', 'M8', 2021, 'Dark Red', NULL, 'D:/CS Project/Car Rental/BMWM8.jpg', 890000.00),
('Audi', 'R8', 2022, 'Silver', NULL, 'D:/CS Project/Car Rental/AudiR8.jpg', 880000.00),
('Lexus', 'LC 500', 2022, 'Purple', NULL, 'D:/CS Project/Car Rental/LexusLC500.jpg', 870000.00);


drop database lux_cars;
select*from cars;