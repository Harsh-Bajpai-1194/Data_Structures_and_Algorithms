# Write your MySQL query statement below
SELECT * FROM Cinema
WHERE id % 2 = 1
and (description IS NOT NULL AND description != "boring")
ORDER BY rating DESC;