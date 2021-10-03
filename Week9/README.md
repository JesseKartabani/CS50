# CS50 Week 9

https://cs50.harvard.edu/x/2021/weeks/9/

# Lab 9 Birthdays

Web application to keep track of birthdays; Built using HTML, CSS, Python, Flask, SQL, and a SQLite database.

![Website](https://user-images.githubusercontent.com/69617120/135736846-b7b6067d-50be-40d4-928e-d5ea58046055.PNG)

This project included distribution code; features completed by me can be found below implementation details. 

### ***Implementation Details*** 

Complete the implementation of a web application to let users store and keep track of birthdays. 

- When the `/` route is requested via `GET`, your web application should display, in a table, all of the people in your database along with their birthdays. 
  - First, in `application.py`, add logic in your `GET` request handling to query the `birthdays.db` database for all birthdays. Pass all of that data to your `index.html` template. 
  - Then, in `index.html`, add logic to render each birthday as a row in the table. Each row should have two columns: one column for the person’s name and another column for the person’s birthday. 

- When the `/` route is requested via `POST`, your web application should add a new birthday to your database and then re-render the index page. 
  - First, in `index.html`, add an HTML form. The form should let users type in a name, a birthday month, and a birthday day. Be sure the form submits to `/` (its “action”) with a method of `post`. 
  - Then, in `application.py`, add logic in your `POST` request handling to `INSERT` a new row into the `birthdays` table based on the data supplied by the user. 
