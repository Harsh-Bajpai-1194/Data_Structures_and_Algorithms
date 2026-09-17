# Write your MySQL query statement below
/*
SELECT transaction_date
    , SUM(IF(amount % 2 = 1, amount, 0)) as odd_sum
    , SUM(IF(amount % 2 = 0, amount, 0)) as even_sum
FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date;
*/

WITH even_odd_transformed AS
(
SELECT transaction_date
, if(amount % 2 = 1, amount, 0) AS odd_amounts
, if(amount % 2 = 0, amount, 0) AS even_amounts
FROM transactions
)
SELECT transaction_date
, sum(odd_amounts) AS odd_sum
, sum(even_amounts) AS even_sum
FROM even_odd_transformed
GROUP BY transaction_date
ORDER BY transaction_date;