from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from functions import login_required

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
Session(app)

db = SQLAlchemy(app)

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


@app.route("/register", method=["POST","GET"])
def register():
    ...

@app.route("/login", method=["POST","GET"])
def login():
    session["user_id"] = 0

