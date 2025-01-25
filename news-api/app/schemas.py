from pydantic import BaseModel

class NewsArticleBase(BaseModel):
    title: str
    link_text: str
    link_href: str

class NewsArticleCreate(NewsArticleBase):
    pass

class NewsArticleResponse(NewsArticleBase):
    id: int

    class Config:
        orm_mode = True
