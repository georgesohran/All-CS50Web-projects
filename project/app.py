from fastapi import FastAPI
import sqlite3

app = FastAPI()

db = sqlite3.connect("database.db")
cur = db.cursor()


@app.get("/")
def index():
    return "aa"


@app.post("/login/")
def login(name:str, password:str, type:str):
    if type == "teacher":
        ...
    elif type == "student":
        ...
    else:
        ...

