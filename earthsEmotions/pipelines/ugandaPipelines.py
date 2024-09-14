from string import whitespace


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


class TheEastAfricanPipeline:
    def process_item(self, article, spider):
        article['title'] = article['title'].strip()
        article['author'] = article['author'].strip()
        article['datetime'] = article['datetime'].strip()
        body = " ".join(
            text for text in article['body'] if text not in whitespace)
        article['body'] = body

        return article
