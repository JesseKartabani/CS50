-- In 4.sql, write a SQL query to determine the number of movies with an IMDb rating of 10.0

SELECT COUNT(rating) AS counter FROM ratings WHERE rating = 10;