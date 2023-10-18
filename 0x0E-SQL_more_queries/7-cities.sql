-- Script that creates the database hbtn_0d_usa and the table cities
-- in the database
-- not fail if exists
CREATE database IF NOT EXISTS hbtn_0d_usa;
CONNECT hbtn_0d_usa;
CREATE table IF NOT EXISTS cities(id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	state_id INT NOT NULL, name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id));
