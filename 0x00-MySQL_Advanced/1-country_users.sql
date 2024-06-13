-- SQL script that creates a table users following these requirements
-- id: integer, never null, auto increment and primary key
-- email: string(255 characters), never null and unique
-- name: string(255 characters)
-- country: enumerations of countries: US, CO and TN, never null (= default will
-- the first element of the enumeration, here is US)

CREATE TABLE IF NOT EXISTS `users` (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
