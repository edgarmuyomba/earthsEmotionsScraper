from string import whitespace

class TheObserverPipeline:
    def process_item(self, article, spider):
        article['title'] = article['title'].strip()
        article['author'] = article['author'].strip()
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
