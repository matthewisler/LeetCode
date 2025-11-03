# Write your MySQL query statement below

SELECT
    id,
    name
FROM
    Students
WHERE
    department_id NOT IN (
        SELECT DISTINCT s.department_id
        FROM Students s
        JOIN Departments d
        ON s.department_id = d.id
    );


