from fastapi import FastAPI
import sqlite3

app = FastAPI()

db = sqlite3.connect("database.db")
cur = db.cursor()

cur.execute("INSERT INTO subjects VALUES (name,english),(name,math),(name,history);")
db.commit()

@app.get("/")
def index():
    return "aa"
