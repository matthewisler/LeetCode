# Write your MySQL query statement below
SELECT
    e1.employee_id,
    COUNT(e2.employee_id) as team_size
FROM
    Employee e1
JOIN
    Employee e2
ON 
    e1.team_id = e2.team_id
GROUP BY
    employee_id