# Write your MySQL query statement below
SELECT
    "[0-5>" AS bin,
    COUNT(*) AS total
FROM
    Sessions
WHERE
    duration between 0 and 299

UNION

SELECT
    "[5-10>" AS bin,
    COUNT(*) AS total
FROM
    Sessions
WHERE
    duration between 300 and 599

UNION

SELECT
    "[10-15>" AS bin,
    COUNT(*) AS total
FROM
    Sessions
WHERE
    duration between 600 and 899


UNION

SELECT
    "15 or more" AS bin,
    COUNT(*) AS total
FROM
    Sessions
WHERE
    duration >= 900