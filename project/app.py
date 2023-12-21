from fastapi import FastAPI
import mysql.connector

app = FastAPI()

db = mysql.connector.connect("database.db")
cursor = db.cursor()

@app.get("/")
def index():
    return "aa"
