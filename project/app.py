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
def index(request: Request):
    return templates.TemplateResponse("layout.html", {"request": request,"word":"my word"})

@app.post("/register", response_class=HTMLResponse)
def regester(request:Request,type:str,name:str,password:str):
    ...

@app.post("/login/", response_class=HTMLResponse)
def login(request: Request, name:str, password:str, type:str):
    if type == "teacher":
        return templates.TemplateResponse("student/index.html", {"request":request})
    elif type == "student":
        ...
    else:
        ...

