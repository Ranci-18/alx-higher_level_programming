-- query creates table force_name on SQL server
-- database name passed as argument of mysql command
-- name cannot be NULL
CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL
);
