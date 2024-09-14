from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from earthsEmotions.items import Article
import logging

class DailyMonitorSpider(CrawlSpider):
    name = 'dailymonitor'
    allowed_domains = ['monitor.co.ug']
    start_urls = ['https://www.monitor.co.ug/uganda']
    rules = [
        Rule(LinkExtractor(allow=r"/uganda/.*",
             restrict_css="a.categories-nav_link"), follow=True),
        Rule(LinkExtractor(
            allow=r"/uganda/[a-z]+/[a-z]+/[\w\-]+$"), follow=True, callback="parse_items")
    ]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'DOWNLOAD_DELAY': 2,
        'DOWNLOAD_TIMEOUT': 5,
        'CLOSESPIDER_ITEMCOUNT': 50,
        'LOG_LEVEL': 'INFO',
        'LOG_FILE': 'dailymonitor.log',
        'DEPTH_PRIORITY': 1,
        'FEEDS': {
            'Outputs/dailymonitor.json': {
                'format': 'json'
            }
        },
        'ITEM_PIPELINES': {
            'earthsEmotions.pipelines.ugandaPipelines.ValidArticlePipeline': 200,
            'earthsEmotions.pipelines.ugandaPipelines.DailyMonitorPipeline': 300,
            'earthsEmotions.pipelines.dbPipelines.PostgresPipeline': 400
        },
        # 'DOWNLOADER_MIDDLEWARES': {
        #     'earthsEmotions.middlewares.DailyMonitorSeleniumMiddleware': 543
        # }
    }

    def parse(self, response):
        logging.info(f"Crawling:: {response.url}")
        return super().parse(response)

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        title = response.css("h1.title-large::text").get()
        if not title:
            title = response.css("h1.title-medium::text").get()
        article['title'] = title
        article['datetime'] = response.css("time.date").attrib.get('datetime')
        article['author'] = response.css(
            "p.article-authors_authors.clearfix > a::text").get()
        article['body'] = response.css(
            "div.paragraph-wrapper > p::text").getall()
        yield article
