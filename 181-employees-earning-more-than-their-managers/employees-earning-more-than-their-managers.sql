# MySQL query statement below
select e.name as Employee
from employee e
join Employee m
on e.managerid = m.id
where e.salary > m.salary;
