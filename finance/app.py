import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol") or not request.form.get("share"):
            return apology("please provide both symbol and share", 403)

        if not lookup(request.form.get("symbol")):
            return apology(f"cant find {request.form.get('symbol')} symbol.")

        l = lookup(request.form.get("symbol"))

        name, price, symbol, total = l["name"], l["price"], l["symbol"], l["price"]*int(request.form.get("share"))

        current_user_stocks = db.execute("SELECT symbol FROM users_stocks WHERE user_id == ?", session["user_id"][0]["id"])
        current_user_stocks = [symbol for symbol in current_user]

        if len(current_user_stocks) == 0:
            db.execute("INSERT INTO users_stocks (user_id,symbol,name,shares,price,total) VALUES(?,?,?,?,?,?)",
                        session["user_id"][0]["id"],
                        symbol,
                        name,
                        request.form.get("share"),
                        price,
                        total
                       )
            return redirect("/")


        elif request.form.get("symbol") in:


        return redirect("/")
    else:
        return render_template("buy.html")




@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
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
    """Get stock quote."""
    if request.method == "POST":
        if not lookup(request.form.get("symbol")):
            return redirect("/")
        l = lookup(request.form.get("symbol"))

        name, price, symbol = l["name"], l["price"], l["symbol"]

        return render_template("quoted.html", name=name,price=price,symbol=symbol)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("insert your user name please", 403)

        elif not request.form.get("password"):
            return apology("insert your password please", 403)

        elif not request.form.get("conf_password"):
            return apology("confirm your passord please", 403)

        elif request.form.get("password") != request.form.get("conf_password"):
            return apology("password and confirmation pasword don't match", 403)

        elif request.form.get("username") in db.execute("SELECT username FROM users"):
            return apology("your username is already taken")

        db.execute("INSERT INTO users (username,hash) VALUES (?,?)", request.form.get("username"),
                   generate_password_hash(request.form.get("password")))

        session["user_id"] = db.execute("SELECT id FROM users WHERE username = ?", request.form.get("username"))

        return redirect("/")
    else:
        return render_template("register.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
