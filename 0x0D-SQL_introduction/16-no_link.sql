-- listing records of second_table
-- where name value is present by order of score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
