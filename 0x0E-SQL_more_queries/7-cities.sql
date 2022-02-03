-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the database
USE hbtn_0d_usa;
-- create a new table
CREATE TABLE IF NOT EXISTS cities (
	PRIMARY KEY(id),
	id			INT	NOT NULL AUTO_INCREMENT,
	state_id 	INT REFERENCES states(id),
	name 		VARCHAR(256)	NOT NULL );
