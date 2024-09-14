from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from earthsEmotions.models import ArticleModel
from sqlalchemy.exc import SQLAlchemyError

class PostgresPipeline(object):
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:muyomba@localhost:5432/earthsEmotions')
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