# Write your MySQL query statement below
SELECT * 
FROM Users
WHERE email REGEXP "^[a-zA-Z0-9_]*@[a-z]+\+.com$"
ORDER BY user_id ASC;