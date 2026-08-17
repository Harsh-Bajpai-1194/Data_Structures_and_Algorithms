# Write your MySQL query statement below
-- SELECT 
-- (SELECT DISTINCT salary 
-- FROM Employee 
-- ORDER BY salary DESC 
-- LIMIT 1 
-- OFFSET 1)
-- AS SecondHighestSalary;

SELECT MAX(salary) AS SecondHighestSalary
FROM employee
WHERE SALARY < ( SELECT MAX(salary) FROM Employee )