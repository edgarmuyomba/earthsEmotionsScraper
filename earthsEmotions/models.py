from sqlalchemy import create_engine, Column, Integer, String, Text, DOUBLE_PRECISION, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ArticleModel(Base):
    __tablename__='uganda'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255))
    datetime = Column(TIMESTAMP) 
    title = Column(String) 
    author = Column(String) 
    body = Column(Text) 
    polarity = Column(DOUBLE_PRECISION)
    