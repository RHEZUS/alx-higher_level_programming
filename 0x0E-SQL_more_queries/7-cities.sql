--  creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (`id` int NOT NULL AUTO_INCREMENT, `state_id` int NOT NULL, `name` VARCHAR(256) NOT NULL, PRIMARY KEY(`id`), FOREIGN KEY(`state_id`) REFERENCES states(`id`));