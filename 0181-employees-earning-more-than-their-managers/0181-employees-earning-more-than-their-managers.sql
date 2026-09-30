# Write your MySQL query statement below
SELECT emp.name AS Employee
FROM employee emp
INNER JOIN employee mgr 
ON emp.managerId = mgr.id
WHERE emp.salary > mgr.salary;