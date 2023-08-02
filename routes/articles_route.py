from fastapi import APIRouter, Request
from typing import List

router = APIRouter()


@router.get("/", response_description="List all articles", response_model=List[dict])
def list_articles(request: Request):
    articles = list(request.app.database["news"].find(limit=100))
    return articles

@router.get("/search/{query}", response_description="Search articles by keywords", response_model=List[dict])
def search_articles(query: str, request: Request):
    articles = list(request.app.database["news"].aggregate([
  {
    "$search": {
      "index": "content",
      "text": {
        "query": query,
        "path": {
          "wildcard": "*"
        }
      }
    }
  }
]))
    return articles




