-- In 12.sql, write a SQL query to list the titles of all movies 
-- in which both Johnny Depp and Helena Bonham Carter starred

SELECT title FROM movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON people.id = stars.person_id
JOIN ratings ON ratings.movie_id = stars.movie_id
WHERE people.name = "Johnny Depp"
INTERSECT
SELECT title FROM movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON people.id = stars.person_id
JOIN ratings ON ratings.movie_id = stars.movie_id
WHERE people.name = "Helena Bonham Carter";