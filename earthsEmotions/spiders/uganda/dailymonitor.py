from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from earthsEmotions.items import Article


class DailyMonitorSpider(CrawlSpider):
    name = 'dailymonitor'
    allowed_domains = ['monitor.co.ug']
    start_urls = ['https://www.monitor.co.ug/uganda']
    rules = [
        Rule(LinkExtractor(allow=r"/uganda/.*"), follow=True),
        Rule(LinkExtractor(
            allow=r"/uganda/[0-9a-zA-Z\-_]+/.*"), follow=True, callback="parse_items")
    ]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'DOWNLOAD_DELAY': 2,
        'DOWNLOAD_TIMEOUT': 5,
        'CLOSESPIDER_ITEMCOUNT': 5,
        'LOG_LEVEL': 'INFO',
        'LOG_FILE': 'dailymonitor.log',
        'FEEDS': {
            'Outputs/dailymonitor.json': {
                'format': 'json'
            }
        },
        # 'ITEM_PIPELINES': {
        #     'earthsEmotions.pipelines.CampusBeePipeline': 300
        # },
        'SPIDER_MIDDLEWARES': {
            'earthsEmotions.middlewares.DailyMonitorSeleniumMiddleware': 543
        }
    }

    def parse(self, response):
        self.logger.info(f"Crawling:: {response.url}")
        return super().parse(response)

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css("h1.title-large::text").get()
        article['datetime'] = response.css("time.date").get()
        article['author'] = response.css(
            "p.article-authors_authors clearfix > a::text").get()
        article['body'] = response.css(
            "div.paragraph-wrapper > p::text").getall()
        yield article
