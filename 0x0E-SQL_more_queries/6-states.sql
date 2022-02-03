-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create a new table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id		INT	PRIMARY KEY	UNIQUE	NOT NULL,
	name 	VARCHAR(256)	NOT NULL );
