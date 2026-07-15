# MySQL query statement below
select email From Person
group by email
Having count(*) > 1;
