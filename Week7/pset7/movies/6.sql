-- In 6.sql, write a SQL query to determine the average rating of all movies released in 2012

SELECT AVG(rating) AS average_2012 FROM movies INNER JOIN ratings ON movies.id = ratings.movie_id WHERE year=2012;