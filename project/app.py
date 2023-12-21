from fastapi import FastAPI
import sqlite3

app = FastAPI()

db = mysql.connector.connect(database="database")
cursor = db.cursor()

@app.get("/")
def index():
    return "aa"
