from fastapi import FastAPI
import sqlite3

app = FastAPI()

db = sqlite3.connect(database="database")
cur = db.cursor()

cur.execute("INSERT INTO subjects name VALUES (1,ENGLISH)")

@app.get("/")
def index():
    return "aa"
