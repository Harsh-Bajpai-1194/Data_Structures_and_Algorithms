# Write your MySQL query statement below
/*
SELECT class
    , COUNT(student) as strength
    FROM Courses
    GROUP BY class) AS class_wise_strength
WHERE strength >= 5;
*/
SELECT class
    FROM Courses
    GROUP BY class
HAVING COUNT(student) >= 5;