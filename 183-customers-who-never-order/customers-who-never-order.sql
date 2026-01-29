# Write your MySQL query statement below
# Write your MySQL query statement below
select c.name as Customers 
from Customers as c 
left join Orders as o 
on c.Id = o.customerId 
where o.id is null;