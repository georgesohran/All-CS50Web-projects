from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from functions import login_required

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQLAlchemy(app)


class Students(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String)


class Teachers(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String)
     subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))


class Subjects(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String)


class StudentsGrades(db.Model):
     subject_id = db.Column(db.Integer, db.ForeignKey("subject"))
     grade = db.Column(db.Integer)
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


@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        ...
    else:
        return render_template("register.html")

@app.route("/login", methods=["POST","GET"])
def login():
    session.clear()
    if request.method == "POST":
        ...
    else:
        return render_template("login.html")


