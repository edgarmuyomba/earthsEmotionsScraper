# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from string import whitespace


class TheObserverPipeline:
    def process_item(self, article, spider):
        article['title'] = article['title'].strip()
        article['author'] = article['author'].strip()
        dateDiv = article['datetime']
        datetime = dateDiv.split(" ")[1].split("=")[1][1:-1]
        article['datetime'] = datetime
        body = " ".join(
            text for text in article['body'] if text not in whitespace)
        article['body'] = body
        return article


class CampusBeePipeline:
    def process_item(self, article, spider):
        article['title'] = article['title'].strip()
        article['datetime'] = article['datetime'].strip()
        article['author'] = article['author'].strip()
        body = " ".join(
            text for text in article['body'] if text not in whitespace)
        article['body'] = body

        return article


class DailyMonitorPipeline:
    def process_item(self, article, spider):
        article['title'] = article['title'].strip()
        article['datetime'] = article['datetime'][2:-1]
        article['author'] = article['author'].strip()
        body = " ".join(
            text for text in article['body'] if text not in whitespace)
        article['body'] = body

        return article

class RedPepperPipeline:
    def process_item(self, article, spider):
        article['title'] = article['title'].strip()
        article['author'] = article['author'].strip()
        article['datetime'] = article['datetime'].strip()
        body = " ".join(
            text for text in article['body'] if text not in whitespace)
        article['body'] = body

        return article