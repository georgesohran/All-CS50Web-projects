from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse

from pydantic import BaseModel

from functools import wraps



class SessionData(BaseModel):
    user_id:int

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if SessionData.user_id is None:
            return RedirectResponse("/login")
        return f(*args, **kwargs)
    return decorated_function
