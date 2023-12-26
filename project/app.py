from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from functions import login_required

import sqlite3

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = sqlite3.connect("tutorial.db")
cur = db.cursor()

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
    return render_template("index.html")


@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        password = request.form.get("password")
        password2 = request.form.get("password2")
        name = request.form.get("name")
        type = request.form.get("type")
        if type == "teacher":
            subject = request.form.get("subject")

        if not password or not password2 or not name or not type:
            return redirect("/register")

    else:
        return render_template("register.html")

@app.route("/login", methods=["POST","GET"])
def login():
    session.clear()
    if request.method == "POST":
        ...
    else:
        return render_template("login.html")


