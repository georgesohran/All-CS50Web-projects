from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import sqlite3

app = FastAPI()

db = sqlite3.connect("database.db")
cur = db.cursor()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("layout.html", {"request": request,"word":"my word"})


@app.post("/login/", response_class=HTMLResponse)
def login(name:str, password:str, type:str):
    if type == "teacher":
        ...
    elif type == "student":
        ...
    else:
        ...

