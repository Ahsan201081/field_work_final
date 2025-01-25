from sqlalchemy.orm import Session
from . import models, schemas

def create_news_article(db: Session, news_article: schemas.NewsArticleCreate):
    db_article = models.NewsArticle(
        title=news_article.title,
        link_text=news_article.link_text,
        link_href=news_article.link_href
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def get_news_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.NewsArticle).offset(skip).limit(limit).all()

def get_news_article_by_id(db: Session, article_id: int):
    return db.query(models.NewsArticle).filter(models.NewsArticle.id == article_id).first()

def update_news_article(db: Session, article_id: int, updated_article: schemas.NewsArticleCreate):
    db_article = db.query(models.NewsArticle).filter(models.NewsArticle.id == article_id).first()
    if db_article:
        db_article.title = updated_article.title
        db_article.link_text = updated_article.link_text
        db_article.link_href = updated_article.link_href
        db.commit()
        db.refresh(db_article)
        return db_article

def delete_news_article(db: Session, article_id: int):
    db_article = db.query(models.NewsArticle).filter(models.NewsArticle.id == article_id).first()
    if db_article:
        db.delete(db_article)
        db.commit()
        return db_article
