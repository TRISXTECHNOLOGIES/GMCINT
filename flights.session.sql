-- Active: 1723464042356@@127.0.0.1@3306@flight_database
CREATE DATABASE flight_database;
USE flight_database;
CREATE TABLE flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    leaving_from VARCHAR(100),
    destination VARCHAR(100),
    connecting_flights ENUM('yes', 'no'),
    flight_date DATE,
    flight_name VARCHAR(100),
    flight_disruption VARCHAR(255),
    hours_late INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
SELECT * FROM flights;

ALTER TABLE flights
ADD COLUMN departure_date DATE AFTER connecting_flights,
ADD COLUMN arrival_date DATE AFTER departure_date;

SELECT * FROM flights;
ALTER TABLE flights
DROP COLUMN flight_date;

DESCRIBE flights;

select * from flights;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
select * from users;
select * from flights;

ALTER TABLE users
ADD COLUMN first_name VARCHAR(100) NOT NULL AFTER id,
ADD COLUMN last_name VARCHAR(100) NOT NULL AFTER first_name,
ADD COLUMN username VARCHAR(100) NOT NULL AFTER last_name;

ALTER TABLE users
ADD COLUMN first_name VARCHAR(100) NOT NULL AFTER id,
ADD COLUMN last_name VARCHAR(100) NOT NULL AFTER first_name;

select * from users;
describe users;


ALTER TABLE users
DROP COLUMN first_name,
DROP COLUMN last_name,
DROP COLUMN username;

ALTER TABLE users
ADD COLUMN first_name VARCHAR(100) NOT NULL AFTER id,
ADD COLUMN last_name VARCHAR(100) NOT NULL AFTER first_name,
ADD COLUMN username VARCHAR(100) NOT NULL AFTER last_name;

USE flight_database;
DESCRIBE users;
SELECT * FROM users WHERE email = 'example@example.com';

    CREATE TABLE claims (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    claim_type VARCHAR(100),
    claim_description TEXT,
    claim_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
SELECT * FROM users WHERE email = 'user@example.com';

ALTER TABLE users ADD COLUMN role ENUM('user', 'admin') DEFAULT 'user';
SELECT * FROM users;
SELECT id, first_name, last_name, email, role FROM users;


select * from users;

DESCRIBE users;
ALTER TABLE users MODIFY password VARCHAR(255);
desc users;

select * from Users;

ALTER TABLE flights ADD COLUMN boarding_pass VARCHAR(255);
select * from flights;

SELECT id, email, role FROM users WHERE email = 'admin@example.com';
INSERT INTO users (first_name, last_name, email, password, role)
VALUES ('Admin', 'User', 'admin@example.com', '<hashed_password>', 'admin');
INSERT INTO users (first_name, last_name, email, password, role)
VALUES ('Admin', 'User', 'admin1@example.com', '<hashed1_password>', 'admin');
SELECT * FROM users WHERE email = 'admin@example.com';
UPDATE users SET password = '1234' WHERE email = 'admin1@example.com';
SELECT email, password FROM users WHERE email = 'admin@example.com';
SELECT email, password FROM users WHERE email = 'admin1@example.com';
SELECT email, password from users where email = 'xyz@gmail.com';

select * from users;

INSERT INTO users (first_name, last_name, email, role)
VALUES ('John1', 'Doe', 'john1.doe@example.com', 'user');


select * from users;
desc users;
select * from users;


select * from users;

SELECT claims.id, claims.claim_type, claims.claim_description, claims.claim_date, 
       users.first_name, users.last_name, users.email
FROM claims
JOIN users ON claims.user_id = users.id
ORDER BY claims.claim_date DESC;
SELECT * FROM flights WHERE id = some_flight_id;
SELECT * FROM flights WHERE id = flight_id;

select * from users;
desc users;
select * from users;

select * from claims;

ALTER TABLE users ADD COLUMN status VARCHAR(255) DEFAULT 'open';
ALTER TABLE flights ADD COLUMN user_id INT;
delete from flights;
select * from flights;
ALTER TABLE flights ADD COLUMN status VARCHAR(255) DEFAULT 'Pending';

INSERT INTO users (first_name, last_name, email, password, role) 
VALUES ('Super', 'Admin', 'superadmin@example.com', 'superpassword', 'super_admin');

select * from users;

SELECT id, first_name, last_name, email, role FROM users WHERE email = 'superadmin@gmail.com';
SHOW COLUMNS FROM users LIKE 'role';

ALTER TABLE users MODIFY role ENUM('user', 'admin', 'super_admin') NOT NULL DEFAULT 'user';

select * from users;
SELECT role FROM users WHERE email = 'superadmin@example.com';
select role from users where email = 'super@gmail.com';
ALTER TABLE users MODIFY role ENUM('user', 'admin', 'super_admin') NOT NULL;
SELECT id, first_name, last_name, email, role FROM users;
UPDATE users SET role = 'super_admin' WHERE email = 'superadmin@example.com';
SHOW COLUMNS FROM users LIKE 'role';
UPDATE users SET role = 'super_admin' WHERE email = 'superadmin@example.com';
SELECT id, first_name, last_name, email, role FROM users WHERE email = 'superadmin@example.com';
select * from users;
ALTER TABLE users ADD assigned_admin_id INT NULL;
ALTER TABLE users ADD COLUMN assigned_admin_id INT NULL;    
SELECT * FROM users WHERE assigned_admin_id = %s;
select * from users;
SELECT * FROM flights;
INSERT INTO flights (scheduled_time, arrival_time, flight_number, first_name, last_name)


DROP TABLE IF EXISTS flights;
CREATE TABLE flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    boarding_pass LONGBLOB,                   -- For storing image data (e.g., a scanned boarding pass)
    destination VARCHAR(255),
    leaving_from VARCHAR(255),
    connecting_flights ENUM('yes', 'no'),
    date DATE,
    flight_name VARCHAR(255),
    scheduled_time TIME,
    arrival_time TIME,
    flight_number VARCHAR(100),
    flight_disruption TEXT,
    hours_of_delay DECIMAL(5, 2),             -- e.g., 1.5 hours
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    travelling_with_group ENUM('yes', 'no'),
    extra_passengers JSON,                    -- For storing multiple passengers' details
    address_line_1 VARCHAR(255),
    address_line_2 VARCHAR(255),
    city VARCHAR(100),
    postal_code VARCHAR(20),
    state VARCHAR(100),
    country VARCHAR(100),
    phone_number VARCHAR(20),
    booking_number VARCHAR(100),
    signature LONGBLOB,                       -- For storing image data (e.g., a digital signature)
    contacted_airline ENUM('yes', 'no'),
    incident_description TEXT
);

select * from flights;
DESCRIBE flights;

ALTER TABLE flights ADD COLUMN user_id INT;\

select * from flights;

DESCRIBE flights;
ALTER TABLE flights ADD COLUMN status VARCHAR(255);

DESCRIBE flights;
delete id from flights;
DESCRIBE flights;

select * from flights;
DESCRIBE flights;

CREATE TABLE comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    text TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS flights;

CREATE TABLE flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    leaving_from VARCHAR(128),
    destination VARCHAR(128),
    flight_name VARCHAR(128),
    date DATE,
    connecting_flights VARCHAR(5),
    scheduled_time VARCHAR(20),
    arrival_time VARCHAR(20),
    flight_number VARCHAR(20),
    flight_disruption VARCHAR(20),
    hours_of_delay VARCHAR(20),
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    traveling_with_group VARCHAR(5),
    passenger_first_name VARCHAR(128),
    passenger_last_name VARCHAR(128),
    passenger_email VARCHAR(128),
    address_line1 VARCHAR(128),
    address_line2 VARCHAR(128),
    city VARCHAR(128),
    postal_code VARCHAR(20),
    state VARCHAR(128),
    country VARCHAR(128),
    phone_number VARCHAR(20),
    booking_number VARCHAR(20),
    signature LONGBLOB,
    contacted_airline VARCHAR(128),
    incident_description TEXT,
    boarding_pass VARCHAR(255)
);


select * from flights;
