# CS50 Week 7

https://cs50.harvard.edu/x/2021/weeks/7/

# Lab 7 Song SQL Queries

Includes eight different SQL queries to answer a variety of different questions using a database of songs (dataset from [Kaggle](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018)).

### ***Implementation Details***

For each of the following problems, you should write a single SQL query that outputs the results specified by each problem. Your response must take the form of a single SQL query, though you may nest other queries inside of your query. You should not assume anything about the ids of any particular songs or artists: your queries should be accurate even if the id of any particular song or person were different. Finally, each query should return only the data necessary to answer the question: if the problem only asks you to output the names of songs, for example, then your query should not also output each song’s tempo. 

1. In 1.sql, write a SQL query to list the names of all songs in the database. 
    - Your query should output a table with a single column for the name of each song. 

2. In 2.sql, write a SQL query to list the names of all songs in increasing order of tempo. 
    - Your query should output a table with a single column for the name of each song. 

3. In 3.sql, write a SQL query to list the names of the top 5 longest songs, in descending order of length. 
    - Your query should output a table with a single column for the name of each song. 

4. In 4.sql, write a SQL query that lists the names of any songs that have danceability, energy, and valence greater than 0.75. 
    - Your query should output a table with a single column for the name of each song. 

5. In 5.sql, write a SQL query that returns the average energy of all the songs. 
    - Your query should output a table with a single column and a single row containing the average energy. 

6. In 6.sql, write a SQL query that lists the names of songs that are by Post Malone. 
    - Your query should output a table with a single column for the name of each song. 
    - You should not make any assumptions about what Post Malone’s artist_id is. 

7. In 7.sql, write a SQL query that returns the average energy of songs that are by Drake. 
    - Your query should output a table with a single column and a single row containing the average energy. 
    - You should not make any assumptions about what Drake’s artist_id is. 

8. In 8.sql, write a SQL query that lists the names of the songs that feature other artists. 
    - Songs that feature other artists will include “feat.” in the name of the song. 
    - Your query should output a table with a single column for the name of each song. 

# PSET 7

# Movie SQL Queries

Includes thirteen different SQL queries to answer a variety of different questions using a database of movies (information courtesy of [IMDb](http://www.imdb.com/) used with permission).

### ***Specification***

For each of the following problems, you should write a single SQL query that outputs the results specified by each problem. Your response must take the form of a single SQL query, though you may nest other queries inside of your query. You should not assume anything about the ids of any particular movies or people: your queries should be accurate even if the id of any particular movie or person were different. Finally, each query should return only the data necessary to answer the question: if the problem only asks you to output the names of movies, for example, then your query should not also output each movie’s release year. 

You’re welcome to check your queries’ results against IMDb itself, but realize that ratings on the website might differ from those in movies.db, as more votes might have been cast since we downloaded the data! 

1. In 1.sql, write a SQL query to list the titles of all movies released in 2008. 
    - Your query should output a table with a single column for the title of each movie. 

2. In 2.sql, write a SQL query to determine the birth year of Emma Stone. 
    - Your query should output a table with a single column and a single row (not including the header) containing Emma Stone’s birth year. 
    - You may assume that there is only one person in the database with the name Emma Stone. 

3. In 3.sql, write a SQL query to list the titles of all movies with a release date on or after 2018, in alphabetical order. 
    - Your query should output a table with a single column for the title of each movie. 
    - Movies released in 2018 should be included, as should movies with release dates in the future. 

4. In 4.sql, write a SQL query to determine the number of movies with an IMDb rating of 10.0. 
    - Your query should output a table with a single column and a single row (not including the header) containing the number of movies with a 10.0 rating. 

5. In 5.sql, write a SQL query to list the titles and release years of all Harry Potter movies, in chronological order. 
    - Your query should output a table with two columns, one for the title of each movie and one for the release year of each movie. 
    - You may assume that the title of all Harry Potter movies will begin with the words “Harry Potter”, and that if a movie title begins with the words “Harry Potter”, it is a Harry Potter movie. 

6. In 6.sql, write a SQL query to determine the average rating of all movies released in 2012. 
    - Your query should output a table with a single column and a single row (not including the header) containing the average rating. 

7. In 7.sql, write a SQL query to list all movies released in 2010 and their ratings, in descending order by rating. For movies with the same rating, order them alphabetically by title. 
    - Your query should output a table with two columns, one for the title of each movie and one for the rating of each movie. 
    - Movies that do not have ratings should not be included in the result. 

8. In 8.sql, write a SQL query to list the names of all people who starred in Toy Story. 
    - Your query should output a table with a single column for the name of each person. 
    - You may assume that there is only one movie in the database with the title Toy Story. 

9. In 9.sql, write a SQL query to list the names of all people who starred in a movie released in 2004, ordered by birth year. 
    - Your query should output a table with a single column for the name of each person. 
    - People with the same birth year may be listed in any order. 
    - No need to worry about people who have no birth year listed, so long as those who do have a birth year are listed in order. 
    - If a person appeared in more than one movie in 2004, they should only appear in your results once. 

10. In 10.sql, write a SQL query to list the names of all people who have directed a movie that received a rating of at least 9.0. 
    - Your query should output a table with a single column for the name of each person. 
    - If a person directed more than one movie that received a rating of at least 9.0, they should only appear in your results once. 

11. In 11.sql, write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated. 
    - Your query should output a table with a single column for the title of each movie. 
    - You may assume that there is only one person in the database with the name Chadwick Boseman. 

12. In 12.sql, write a SQL query to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred. 
    - Your query should output a table with a single column for the title of each movie. 
    - You may assume that there is only one person in the database with the name Johnny Depp. 
    - You may assume that there is only one person in the database with the name Helena Bonham Carter. 

13. In 13.sql, write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred. 
    - Your query should output a table with a single column for the name of each person. 
    - There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958. 
    - Kevin Bacon himself should not be included in the resulting list. 

# Fiftyville SQL Queries

SQL queries on an SQLite database in order to identify who committed a robbery, what city the thief escaped to, and who the thief’s accomplice is who helped them escape. 

### ***Background** 

The CS50 Duck has been stolen! The town of Fiftyville has called upon you to solve the mystery of the stolen duck. Authorities believe that the thief stole the duck and then, shortly afterwards, took a flight out of town with the help of an accomplice. Your goal is to identify: 

- Who the thief is, 
- What city the thief escaped to, and 
- Who the thief’s accomplice is who helped them escape 

All you know is that the theft took place on July 28, 2020 and that it took place on Chamberlin Street. 

How will you go about solving this mystery? The Fiftyville authorities have taken some of the town’s records from around the time of the theft and prepared a SQLite database for you, fiftyville.db, which contains tables of data from around the town. You can query that table using SQL SELECT queries to access the data of interest to you. Using just the information in the database, your task is to solve the mystery. 
