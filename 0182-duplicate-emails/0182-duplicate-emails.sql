# Write your MySQL query statement below
/*
select email
from (
select email
, count(id) as occurences
from person
group by email) as ABC
where ABC.occurences > 1;
*/
select email
from person
group by email
having count(id) > 1