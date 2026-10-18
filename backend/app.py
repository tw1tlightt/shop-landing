from fastapi import FastAPI
from backend.db import create_db
from backend.models import t

app = FastAPI()

# @app.on_event("startup")
# def start():
#     create_db()