from fastapi import FastAPI
import mysql.connector

app = FastAPI()

database = mysql.connector.connect("database.db")

@app.get("/")
def index():
    return "aa"
