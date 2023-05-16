-- computing of scores of all records
-- and adding them to average column
ALTER TABLE second_table
ADD COLUMN average float;
INSERT INT second_table (average)
SELECT AVG(score)
FROM second_table;
