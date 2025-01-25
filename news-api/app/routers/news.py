from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(
    prefix="/news",
    tags=["news"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_news(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    news_articles = crud.get_news_articles(db, skip=skip, limit=limit)
    return {"data": news_articles}

@router.post("/", response_model=schemas.NewsArticleResponse)
def create_news(news_article: schemas.NewsArticleCreate, db: Session = Depends(database.get_db)):
    return crud.create_news_article(db=db, news_article=news_article)
