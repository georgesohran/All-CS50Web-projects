from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from functions import login_required

from werkzeug.security import check_password_hash, generate_password_hash

import os.path
import sqlite3

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")
db = sqlite3.connect(db_path, check_same_thread=False)
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
        if type not in ["teacher", "student"]:
            return redirect("/register")
        if password != password2:
            return redirect("/register")

        names = cur.execute(f"SELECT name FROM {type}s")
        names.fetchall()
        print(names)
        if name in names:
            return redirect("/register")

        if type == "teacher":
            subject_id = db.execute("SELECT id FROM subjects WHERE name == ?", (subject,))
            if subject not in db.execute("SELECT name FROM subjects"):
                return redirect("/register")
            cur.execute("INSERT INTO teachers (name,password_hash,subject_id) VALUES(?,?,?)",name, generate_password_hash(password), subject_id)
            cur.commit()
        elif type == "student":
            cur.execute("INSERT INTO students (name,password_hash) VALUES(?,?)", name, generate_password_hash(password))
            cur.commit()

        id = db.execute("SELECT id FROM students WHERE name == ? AND password_hash == ?", name, generate_password_hash(password))
        id.fetchall()

        session["user_id"] = id
    else:
        return render_template("register.html")

@app.route("/login", methods=["POST","GET"])
def login():
    session.clear()
    if request.method == "POST":
        ...
    else:
        return render_template("login.html")


