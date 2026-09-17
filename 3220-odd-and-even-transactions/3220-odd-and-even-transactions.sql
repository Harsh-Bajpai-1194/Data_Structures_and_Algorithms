# Write your MySQL query statement below
SELECT transaction_date
    , SUM(IF(amount % 2 = 1, amount, 0)) as odd_sum
    , SUM(IF(amount % 2 = 0, amount, 0)) as even_sum
FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date;

/*
with even_odd_transformed as
(

select transaction_date
, if(amount % 2 = 1, amount, 0) as odd_amounts
, if(amount % 2 = 0, amount, 0) as even_amounts
from transactions
select transaction_date;
*/