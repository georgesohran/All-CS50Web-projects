from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse

from pydantic import BaseModel

class SessionData(BaseModel):
    userid: str

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return RedirectResponse("/login")
        return f(*args, **kwargs)
    return decorated_function
