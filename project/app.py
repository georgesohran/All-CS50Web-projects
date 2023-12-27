from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from functions import login_required,sort_grades

from werkzeug.security import check_password_hash, generate_password_hash

import os.path
import sqlite3

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")




@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/register", methods=["POST","GET"])
def register():
    session.clear()

    db = sqlite3.connect(db_path, check_same_thread=False)
    cur = db.cursor()
    if request.method == "POST":
        password = request.form.get("password")
        password2 = request.form.get("password2")
        name = request.form.get("name")
        type = request.form.get("type")
        if type == "teacher":
            subject = request.form.get("subject")
            if subject not in ["math", "history", "english","computer sceince"]:
                return render_template("register.html", messege="invalid subject")

        if not password or not password2 or not name or not type:
            return render_template("register.html", messege="missing password or name or type")
        if type not in ["teacher", "student"]:
            return render_template("register.html", messege="invalid type")
        if password != password2:
            return render_template("register.html", messege="invalid repeat password")


        if type == "teacher":
            subject_id = db.execute("SELECT id FROM subjects WHERE name == ?", (subject,)).fetchall()
            subject_id = subject_id[0]
            subject_id = [i for i in subject_id][0]

            if (subject,) not in db.execute("SELECT name FROM subjects").fetchall():
                return render_template("register.html",messege="invalid subject")

            cur.execute("INSERT INTO teachers (name,password_hash,subject_id) VALUES(?,?,?)",(name, generate_password_hash(password), subject_id))
            db.commit()

        elif type == "student":
            cur.execute("INSERT INTO students (name,password_hash) VALUES(?,?)", (name, generate_password_hash(password)))
            db.commit()

        session["user_id"] = cur.execute(f"SELECT id FROM {type}s WHERE name == ?", (name,)).fetchall()

        session["user_type"] = type

        db.close()

        return redirect("/")

    else:
        db.close()

        return render_template("register.html", messege="OK")

@app.route("/login", methods=["POST","GET"])
def login():
    session.clear()

    db = sqlite3.connect(db_path, check_same_thread=False)
    cur = db.cursor()
    if request.method == "POST":
        name = request.form.get("name")
        type = request.form.get("type")
        password = request.form.get("password")

        if not name or not type or not password:
            return render_template("login.html" ,messege="missing name, type or password")

        if type not in ["teacher", "student"]:
            return render_template("login.html", messege="invalid type")

        all_names = cur.execute(f"SELECT name FROM {type}s")
        all_names = [i[0] for i in all_names]

        if name not in all_names:
            return render_template("login.html", messege="the name is not registrated")

        act_password = cur.execute(f"SELECT password_hash FROM {type}s WHERE name == ?", (name,)).fetchall()[0]
        if check_password_hash(act_password[0], password):
            return render_template("login.html", messege="invalid password")


        session["user_id"] = cur.execute(f"SELECT id FROM {type}s WHERE name == ?", (name,)).fetchall()

        session["user_type"] = type

        db.close()

        return redirect("/")
    else:
        db.close()
        return render_template("login.html", messege="OK")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")



@app.route("/")
@login_required
def main_page():
    db = sqlite3.connect(db_path, check_same_thread=False)
    cur = db.cursor()
    if session["user_type"] == "teacher":

        return render_template("teacher/index.html")

    elif session["user_type"] == "student":
        schedule = db.execute("SELECT * FROM schedule").fetchall()
        db.close()
        return render_template("student/index.html", schedule=schedule)



@app.route("/grades")
@login_required
def students():
    db = sqlite3.connect(db_path, check_same_thread=False)
    cur = db.cursor()

    grades = db.execute("SELECT students_grades.grade, students_grades.time, subjects.name FROM students_grades INNER JOIN subjects ON students_grades.subject_id = subjects.id WHERE student_id = ?", (session["user_id"],)).fetchall()
    subjects = db.execute("SELECT name FROM subjects").fetchall()

    db.close()
    return render_template("student/grades.html",grades=grades, subjects=subjects)
