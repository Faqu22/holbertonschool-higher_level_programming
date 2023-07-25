-- This script that lists all records of the table second_table.
SELECT name, Sum(score)
FROM second_table
Group By name
Order By Sum(score) Desc;