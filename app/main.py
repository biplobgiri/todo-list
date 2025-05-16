from fastapi import FastAPI
from app.routes import router
from dotenv import load_dotenv
import os

load_dotenv()

app=FastAPI(title=os.getenv("APP_NAME","Todo App"))

app.include_router(router)

#adding some changes in the file