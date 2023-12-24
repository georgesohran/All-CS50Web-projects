from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse

from pydantic import BaseModel

class SessionData(BaseModel):
    userid: str
