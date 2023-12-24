from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

from pydantic import BaseModel

import sqlite3

from uuid import uuid4

from werkzeug.security import check_password_hash, generate_password_hash



class SessionData(BaseModel):
    userid: str

app = FastAPI()

db = sqlite3.connect("database.db")
cur = db.cursor()

templates = Jinja2Templates(directory="templates")



@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("layout.html", {"request": request,"word":"my word"})

@app.post("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("layout.html", {"request": request,"word":"my word"})



@app.get("/register", response_class=HTMLResponse)
def register(request:Request):
    return templates.TemplateResponse("register.html", {"request":request})

@app.post("/register", response_class=RedirectResponse)
def register(request:Request, name:str = Form(...), password:str = Form(...), type = Form(...)):

    return "/"



@app.post("/login/", response_class=HTMLResponse)
def login(request: Request, name:str, password:str, type:str):
    if type == "teacher":
        return templates.TemplateResponse("student/index.html", {"request":request})
    elif type == "student":
        ...
    else:
        ...

