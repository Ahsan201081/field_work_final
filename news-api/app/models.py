from sqlalchemy import Column, Integer, String, Text
from .database import Base

class NewsArticle(Base):
    __tablename__ = 'scraped_data'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    link_text = Column(String(255))
    link_href = Column(Text)
