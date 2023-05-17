-- query lists cities in hbtn_0d_usa
-- by cities.id cities.name states.name
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id;
