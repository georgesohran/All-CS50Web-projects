from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from functions import login_required

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
Session(app)

db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    grades = db.relationship("Grades",backref="student")

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    grades = db.relationship("Teachers",backref="subject")

class Grades(db.Model):
    value = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))


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
    if request.method == "POST":
        ...
    else:
        return render_template("register.html")

@app.route("/login", method=["POST","GET"])
def login():
    session["user_id"] = 0

