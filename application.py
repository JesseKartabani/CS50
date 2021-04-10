import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
 # Query infos from database
    rows = db.execute("SELECT * FROM stocks WHERE user_id = :user",
                          user=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])[0]['cash']

    # Pass a list of lists to the template page, template is going to iterate it to extract the data into a table
    total = cash
    stocks = []
    for index, row in enumerate(rows):
        stock_info = lookup(row['symbol'])

        # Create a list with all the info about the stock and append it to a list of every stock owned by the user
        stocks.append(list((stock_info['symbol'], stock_info['name'], row['amount'], stock_info['price'], round(stock_info['price'] * row['amount'], 2))))
        total += stocks[index][4]

    return render_template("index.html", stocks=stocks, cash=round(cash, 2), total=round(total, 2))

    """Show portfolio of stocks"""


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
  # ensure a symbol and quantity were submited
        if not request.form.get("symbol") or not request.form.get("quantity") or int(request.form.get("quantity")) < 1:
            return render_template("buy.html")
        
        symbol = request.form.get("symbol").upper()
        quantity = request.form.get("quantity")
        user_id = session["user_id"]
        
        # lookup the stock
        stock = lookup(symbol)

        # ensure symbol exists
        if not stock:
            return apology("symbol not found")

        # calculate total price
        total_price = float(stock["price"]) * float(quantity)
        
        user = db.execute("SELECT * FROM users WHERE id = :id", id=user_id)
        funds = float(user[0]["cash"])
        
        # check if user has enough funds
        if funds < total_price:
            return apology(top="not enough funds", bottom="available: " + str("%.2f"%funds))
        
        funds_left = funds - total_price
        
        # check if symbol is already owned
        stock_db = db.execute("SELECT * FROM stocks WHERE user_id = :user_id AND symbol = :symbol",
                            user_id=user_id, symbol=symbol)
        
        # update with new price if already owned   
        if len(stock_db) == 1:
            
            new_quantity = int(stock_db[0]["quantity"]) + int(quantity)
            new_total = float(stock_db[0]["total"]) + total_price
            new_pps = "%.2f"%(new_total / float(new_quantity))
            
            db.execute("UPDATE stocks SET quantity = :quantity, total = :total, pps = :pps WHERE user_id = :user_id AND symbol = :symbol",
                        quantity=new_quantity, total=new_total, pps=new_pps, user_id=user_id, symbol=symbol)
            
        # else create a new entry in db
        else:
            
            db.execute("INSERT INTO stocks (user_id, symbol, quantity, total, pps) VALUES (:user_id, :symbol, :quantity, :total, :pps)",
                        user_id=user_id, symbol=symbol, quantity=quantity, total=total_price, pps=stock["price"])
                        
        # modify available funds
        db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash=funds_left, id=user_id)
        
        # commit to history
        db.execute("INSERT INTO history (user_id, action, symbol, quantity, pps) VALUES (:user_id, :action, :symbol, :quantity, :pps)",
                    user_id=user_id, action=1, symbol=symbol, quantity=quantity, pps=stock["price"])
        
        # send a success message
        return render_template("success.html", action="bought", quantity=quantity,
                                name=stock["name"], total=usd(total_price), funds=usd(funds_left))
        
    else:
        return render_template("buy.html")
    """Buy amount of stock"""


@app.route("/history")
@login_required
def history():
 # Query database with the transactions history
    rows = db.execute("SELECT * FROM transactions WHERE user_id = :user",
                            user=session["user_id"])

    # Pass a list of lists to the template page, template is going to iterate it to extract the data into a table
    transactions = []
    for row in rows:
        stock_info = lookup(row['symbol'])

        # Create a list with all the info about the transaction and append it to a list of every stock transaction
        transactions.append(list((stock_info['symbol'], stock_info['name'], row['amount'], row['value'], row['date'])))

    return render_template("history.html", transactions=transactions)

    """Show history of transactions"""


def is_provided(field):
    if not request.form.get(field):
        return apology(f"must provide {field}", 403)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide stock symbol")

        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("Stock symbol not valid, please try again")

        else:
            return render_template("quoted.html", stockName={
                'name': quote['name'],
                'symbol': quote['symbol'],
                'price': usd(quote['price'])
            })

    else:
        return render_template("quote.html")
    """Get stock quote."""


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure confirm password is correct
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("The passwords don't match", 400)

        # Query database for username if already exists
        elif db.execute("SELECT * FROM users WHERE username = :username",
            username=request.form.get("username")):
            return apology("Username already taken", 400)

        # Insert user and hash of the password into the table
        db.execute("INSERT INTO users(username, hash) VALUES (:username, :hash)",
            username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
            username=request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")

    """Register user"""


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        amount=int(request.form.get("amount"))
        symbol=request.form.get("symbol")
        price=lookup(symbol)["price"]
        value=round(price*float(amount))

        # Update stocks table
        amount_before = db.execute("SELECT amount FROM stocks WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"])[0]['amount']
        amount_after = amount_before - amount

        # Delete stock from table if we sold every unit we had
        if amount_after == 0:
            db.execute("DELETE FROM stocks WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"])

        # Stop the transaction if the user does not have enough stocks
        elif amount_after < 0:
            return apology("That's more than the stocks you own")

        # Otherwise update with new value
        else:
            db.execute("UPDATE stocks SET amount = :amount WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"], amount=amount_after)

        # Update user's cash
        cash = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])[0]['cash']
        cash_after = cash + price * float(amount)

        db.execute("UPDATE users SET cash = :cash WHERE id = :user",
                          cash=cash_after, user=session["user_id"])

        # Update history table
        db.execute("INSERT INTO transactions(user_id, symbol, amount, value) VALUES (:user, :symbol, :amount, :value)",
                user=session["user_id"], symbol=symbol, amount=-amount, value=value)

        # Redirect user to home page with success message
        flash("Sold!")
        return redirect("/")
    else:
        # Query database with the transactions history
        rows = db.execute("SELECT symbol, amount FROM stocks WHERE user_id = :user",
                            user=session["user_id"])

        # Create a dictionary with the availability of the stocks
        stocks = {}
        for row in rows:
            stocks[row['symbol']] = row['amount']

        return render_template("sell.html", stocks=stocks)

    """Sell amount of stock"""


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
