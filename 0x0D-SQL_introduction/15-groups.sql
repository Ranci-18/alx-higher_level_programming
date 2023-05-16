-- listing number of records with same score in second_table
-- ordered by count
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
