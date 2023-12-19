import os

import datetime
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
    print(session)

    rows = db.execute("SELECT * FROM users_stocks WHERE user_id == ?", session["user_id"])
    users_cash = db.execute("SELECT cash FROM users WHERE id == ?", session["user_id"])

    return render_template("index.html",rows=rows,cash=users_cash[0])


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("please provide both symbol and shares")

        if not lookup(request.form.get("symbol")):
            return apology(f"cant find {request.form.get('symbol')} symbol.")

        if float(request.form.get("shares")) != int(request.form.get("shares")):
            return apology("invalid shares")

        if int(request.form.get("shares")) <= 0:
            return apology("please provide a positive shares")

        l = lookup(request.form.get("symbol"))

        name, price, symbol, total = l["name"], l["price"], l["symbol"], l["price"]*int(request.form.get("shares"))


        if db.execute("SELECT cash FROM users WHERE id == ?", session["user_id"])[0]["cash"] < total:
            return apology("you can't afford this stock")

        db.execute("UPDATE users SET cash = cash - ? WHERE id == ?", total, session["user_id"])

        current_user_stocks = db.execute("SELECT symbol FROM users_stocks WHERE user_id == ?", session["user_id"])

        current_user_stocks = [symbol_dict["symbol"] for symbol_dict in current_user_stocks]
        current_user_stocks = set(current_user_stocks)

        if len(current_user_stocks) == 0:
            db.execute("INSERT INTO users_stocks (user_id,symbol,name,shares,price,total) VALUES(?,?,?,?,?,?)",
                        session["user_id"][0]["id"],
                        symbol,
                        name,
                        request.form.get("shares"),
                        price,
                        total
                       )

        elif symbol in current_user_stocks:
            db.execute("UPDATE users_stocks SET shares = shares + ? WHERE user_id == ?", request.form.get("shares"), session["user_id"][0]["id"])

        else:
            db.execute("INSERT INTO users_stocks (user_id,symbol,name,shares,price,total) VALUES(?,?,?,?,?,?)",
                        session["user_id"][0]["id"],
                        symbol,
                        name,
                        request.form.get("shares"),
                        price,
                        total
                       )

        db.execute("INSERT INTO history(symbol,shares,price,transacted,user_id) VALUES (?,?,?,?,?)",
                   symbol,
                   request.form.get("shares"),
                   price,
                   datetime.datetime.now(),
                   session["user_id"][0]["id"]
                   )

        return redirect("/")

    else:
        return render_template("buy.html")




@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    rows = db.execute("SELECT * FROM history WHERE user_id == ?",session["user_id"][0]["id"])

    return render_template("history.html", rows=rows)


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
            return apology("no such symbol found",400)
        l = lookup(request.form.get("symbol"))

        name, price, symbol = l["name"], format(l["price"],".2f"), l["symbol"]

        return render_template("quoted.html", name=name,price=price,symbol=symbol)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        names = db.execute("SELECT username FROM users")
        names = [name["username"] for name in names]

        if not request.form.get("username"):
            return apology("insert your user name please")

        if not request.form.get("password"):
            return apology("insert your password please")

        if not request.form.get("confirmation"):
            return apology("confirm your passord please")

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("password and confirmation pasword don't match")

        if request.form.get("username") in names:
            return apology("your username is already taken")

        db.execute("INSERT INTO users (username,hash) VALUES (?,?)", request.form.get("username"),
                   generate_password_hash(request.form.get("password")))

        session["user_id"] = db.execute("SELECT id FROM users WHERE username = ?", request.form.get("username"))[0]["id"]

        return redirect("/")
    else:
        return render_template("register.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbols = db.execute("SELECT symbol FROM users_stocks WHERE user_id == ?", session["user_id"][0]["id"])
        symbols = [symboldict["symbol"] for symboldict in symbols]

        symbol_shares = db.execute("SELECT shares FROM users_stocks WHERE user_id == ? AND symbol == ?", session["user_id"][0]["id"], request.form.get("symbol"))

        if not symbol_shares:
            return apology("incorrect symbol", 403)

        if int(request.form.get("shares")) <= 0 or int(request.form.get("shares")) > symbol_shares[0]["shares"]:
            return apology("invalid shares", 403)

        l = lookup(request.form.get("symbol"))
        price  = l["price"]

        db.execute("UPDATE users SET cash = cash + ? WHERE id == ?", price, session["user_id"][0]["id"])

        if int(request.form.get("shares")) == int(symbol_shares[0]["shares"]):
            db.execute("DELETE FROM users_stocks WHERE user_id == ? AND symbol == ?",session["user_id"][0]["id"], request.form.get("symbol"))

        else:
            db.execute("UPDATE users_stocks SET shares = shares - ? WHERE user_id == ? AND symbol == ?", request.form.get("shares"), session["user_id"][0]["id"], request.form.get("symbol"))
            db.execute("UPDATE users_stocks SET total = shares * price WHERE user_id == ? AND symbol == ?", session["user_id"][0]["id"], request.form.get("symbol"))
        return redirect("/")

    else:

        symbols = db.execute("SELECT symbol FROM users_stocks WHERE user_id == ?", session["user_id"][0]["id"],)
        return render_template("sell.html",symbols=symbols)

