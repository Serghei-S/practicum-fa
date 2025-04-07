from fastapi import FastAPI
from app.api import users, tsp

app = FastAPI()

app.include_router(users.router)
app.include_router(tsp.router)
