# Write your MySQL query statement below
WITH students_per_class(class,students_count) AS
(
    SELECT class
         , count(student) AS students_count
    FROM Courses
    GROUP BY class
)
SELECT class
FROM students_per_class
WHERE students_count >= 5;

/*
SELECT class
    , COUNT(student) as strength
    FROM Courses
    GROUP BY class) AS class_wise_strength
WHERE strength >= 5;
*/

/*
SELECT class
    FROM Courses
    GROUP BY class
HAVING COUNT(student) >= 5;
*/