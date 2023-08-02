from fastapi import FastAPI
from pymongo import MongoClient
from routes.articles_route import router as articles_router
import os

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(os.environ.get('MONGODB_CONNECTION'))
    app.database = app.mongodb_client['guardian-data']

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(articles_router, tags=["articles"], prefix="/articles")