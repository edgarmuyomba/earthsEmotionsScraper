import logging
import dateparser

class ValidArticlePipeline:
    def process_item(self, article, spider):
        if not article['url']:
            article['url'] = "No url"
        if not article['title']:
            article['title'] = "No title"
        if not article['author']:
            article['author'] = "No author"
        if not article['datetime']:
            article['datetime'] = "No datetime"
        if not article['body']:
            article['body'] = ["No body"]

        return article

class StandardDatePipeline:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def process_item(self, article, spider):
        
        datetime = article['datetime']

        if datetime != "No datetime":

            try:

                parsed_date = dateparser.parse(datetime)
            
            except:

                self.logger.critical(f"Failed to standardize datetime value - {datetime}")

            else:
                
                article['datetime'] = parsed_date.strftime('%Y-%m-%d %H:%M:%S')

        return article