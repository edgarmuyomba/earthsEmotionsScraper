from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from earthsEmotions.models import ArticleModel
from sqlalchemy.exc import SQLAlchemyError

import os 
from dotenv import load_dotenv

load_dotenv()

class PostgresPipeline(object):
    def __init__(self):
        self.engine = create_engine(f'postgresql://{os.getenv('POSTGRES_USERNAME')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/earthsEmotions')
        self.Session = sessionmaker(bind=self.engine)

    def process_item(self, article, spider):
        session = self.Session()
        instance = ArticleModel(**article)
        
        try:
            session.add(instance)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            spider.logger.error(f"Error saving article: {str(e)}")
            raise
        finally:
            session.close()

        return article