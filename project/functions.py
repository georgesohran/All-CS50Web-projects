from flask import redirect, render_template, session
from functools import wraps



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def sort_grades(grades):
    sorted_grades = []
    subjects = set()
    for item in grades:
        subjects.sdd(grades[2])

    subject_dict = {}

