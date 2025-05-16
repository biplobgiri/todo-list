from fastapi import FastAPI,HTTPException
from app.routes import router
from dotenv import load_dotenv
import os

load_dotenv()

app=FastAPI(title=os.getenv("APP_NAME","TODO"))

app.include_router(router)


