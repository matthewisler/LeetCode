# Write your MySQL query statement below

SELECT
    name
FROM
    Candidate c
JOIN
    (
        SELECT
            candidateId
        FROM
            Vote
        GROUP BY
            candidateId
        ORDER BY
            COUNT(candidateId) DESC
        LIMIT 1
    ) v
ON c.id = v.candidateId
