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

# PSET 9 C$50 Finance

Web application via which users can “buy” and “sell” stocks, a la the below.

![Website](https://user-images.githubusercontent.com/69617120/135743243-d6b533af-cff9-46dc-a9b5-2b2a32812fb8.PNG)

This project included distribution code; features completed by me can be found below specification.

## **Background**

Full stack web application designed for buying and selling stocks. Giving users the ability to execute live quotes on stocks by utilizing an IEX API key, buy any stock of their choosing as well as sell stocks they are holding. 

Users also can retain their data by registering an account, registered accounts are stored inside an SQLite database (passwords are hashed for security) along with a transaction history which is visible for users on the front end. 

## **Tech Stack / Tools**

- HTML, CSS, Bootstrap
- Python, Flask, Jinja
- SQL, SQLite, phpLiteAdmin
- Public API key [IEX](https://iexcloud.io/console/tokens)

## **Specification**

### `register`

Complete the implementation of `register` in such a way that it allows a user to register for an account via a form.
- Require that a user input a username, implemented as a text field whose `name` is `username`. Render an apology if the user’s input is blank or the username already exists.
- Require that a user input a password, implemented as a text field whose `name` is `password`, and then that same password again, implemented as a text field whose `name` is `confirmation`. Render an apology if either input is blank or the passwords do not match.
- Submit the user’s input via `POST` to `/register`.
- `INSERT` the new `user` into users, storing a hash of the user’s password, not the password itself. Hash the user’s password with `generate_password_hash` Odds are you’ll want to create a new template (e.g., `register.html`) that’s quite similar to `login.html`.
- Once the user is registered, you may either automatically log in the user or bring the user to a page where they can log in themselves.

Once you’ve implemented `register` correctly, you should be able to register for an account and log in. And you should be able to see your rows via sqlite3 or phpLiteAdmin.

### `quote`

Complete the implementation of `quote` in such a way that it allows a user to look up a stock’s current price.
- Require that a user input a stock’s symbol, implemented as a text field whose `name` is `symbol`.
- Submit the user’s input via `POST` to `/quote`.
- Odds are you’ll want to create two new templates (e.g., `quote.html` and `quoted.html`). When a user visits `/quote` via GET, render one of those templates, inside of which should be an HTML form that submits to `/quote` via POST. In response to a POST, `quote` can render that second template, embedding within it one or more values from `lookup`.

### `buy`

Complete the implementation of `buy` in such a way that it enables a user to buy stocks.
- Require that a user input a stock’s symbol, implemented as a text field whose `name` is `symbol`. Render an apology if the input is blank or the symbol does not exist (as per the return value of `lookup`).
- Require that a user input a number of shares, implemented as a text field whose `name` is `shares`. Render an apology if the input is not a positive integer.
- Submit the user’s input via `POST` to `/buy`.
- Odds are you’ll want to call `lookup` to look up a stock’s current price.
- Odds are you’ll want to `SELECT` how much cash the user currently has in `users`.
- Add one or more new tables to `finance.db` via which to keep track of the purchase. Store enough information so that you know who bought what at what price and when.
  - Use appropriate SQLite types.
  - Define `UNIQUE` indexes on any fields that should be unique.
  - Define (non-`UNIQUE`) indexes on any fields via which you will search (as via `SELECT` with `WHERE`).
- Render an apology, without completing a purchase, if the user cannot afford the number of shares at the current price.
- When a purchase is complete, redirect the user back to the `index` page.
- You don’t need to worry about race conditions (or use transactions).

Once you’ve implemented `buy` correctly, you should be able to see users purchases in your new table(s) via `sqlite3` or phpLiteAdmin.

### `index`

Complete the implementation of `index` in such a way that it displays an HTML table summarizing, for the user currently logged in, which stocks the user owns, the numbers of shares owned, the current price of each stock, and the total value of each holding (i.e., shares times price). Also display the user’s current cash balance along with a grand total (i.e., stocks’ total value plus cash).
- Odds are you’ll want to execute multiple `SELECT`s. Depending on how you implement your table(s), you might find `GROUP BY` `HAVING` `SUM` and/or `WHERE` of interest.
- Odds are you’ll want to call `lookup` for each stock.

### `sell`

Complete the implementation of `sell` in such a way that it enables a user to sell shares of a stock (that he or she owns).
- Require that a user input a stock’s symbol, implemented as a `select` menu whose `name` is `symbol`. Render an apology if the user fails to select a stock or if (somehow, once submitted) the user does not own any shares of that stock.
- Require that a user input a number of shares, implemented as a text field whose `name` is `shares`. Render an apology if the input is not a positive integer or if the user does not own that many shares of the stock.
- Submit the user’s input via `POST` to `/sell`.
When a sale is complete, redirect the user back to the `index` page.
You don’t need to worry about race conditions (or use transactions).

### `history`

Complete the implementation of `history` in such a way that it displays an HTML table summarizing all of a user’s transactions ever, listing row by row each and every buy and every sell.
- For each row, make clear whether a stock was bought or sold and include the stock’s symbol, the (purchase or sale) price, the number of shares bought or sold, and the date and time at which the transaction occurred.
- You might need to alter the table you created for `buy` or supplement it with an additional table. Try to minimize redundancies.

### Extra feature

- Allow users to add additional cash to their account.
