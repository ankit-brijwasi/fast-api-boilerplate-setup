from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.internal.config import STATIC_DIR
from app.routers.urls import routers


app = FastAPI(title="Fast API project")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

for router in routers:
    app.include_router(router)