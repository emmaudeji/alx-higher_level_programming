-- script that shows scores in descending order
SELECT 
    score, 
    COUNT(score) AS number
FROM
    second_table
GROUP BY score
ORDER BY score DESC;

