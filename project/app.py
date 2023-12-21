from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/")
def index():
    return "aa"
