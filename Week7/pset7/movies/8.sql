-- In 8.sql, write a SQL query to list the names of all people who starred in Toy Story

SELECT people.name
FROM people
JOIN stars ON stars.person_id = people.id
JOIN movies ON movies.id = stars.movie_id
WHERE movies.title = "Toy Story";