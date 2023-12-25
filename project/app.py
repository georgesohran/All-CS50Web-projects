from flask import Flask, flash, redirect, render_template, request, session
from functions import login_required


app = Flask(__name__)


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/register", method=["POST","GET"])
def register():
    ...

@app.route("/login", method=["POST","GET"])
def register():
    ...

