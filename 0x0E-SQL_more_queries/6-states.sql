-- query creates database 'hbtn_0d_usa' and table 'states'
-- without fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL
);