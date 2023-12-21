from fastapi import FastAPI
import mysql.connector

app = FastAPI()

database = mysql.connector.connect("")

@app.get("/")
def index():
    return "aa"
