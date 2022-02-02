-- lists score and names where name is present
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
