from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from earthsEmotions.items import Article


class CampusBeeSpider(CrawlSpider):
    name = 'campusbee'
    allowed_domains = ['campusbee.ug']
    start_urls = ['https://campusbee.ug/']
    rules = [
        Rule(LinkExtractor(allow=r"/category/[a-zA-Z0-9-_]+/$"), follow=True),
        Rule(LinkExtractor(allow=r".*", restrict_css="h3.jeg_post_title a"),
             follow=True, callback="parse_items")
    ]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'DOWNLOAD_DELAY': 2,
        'DOWNLOAD_TIMEOUT': 5,
        'CLOSESPIDER_ITEMCOUNT': 20,
        'LOG_LEVEL': 'INFO',
        'LOG_FILE': 'campusbee.log',
        'FEEDS': {
            'Outputs/campusbee.json': {
                'format': 'json'
            }
        },
        'ITEM_PIPELINES': {
            'earthsEmotions.pipelines.ugandaPipelines.ValidArticlePipeline': 200,
            'earthsEmotions.pipelines.ugandaPipelines.CampusBeePipeline': 300,
            'earthsEmotions.pipelines.dbPipelines.PostgresPipeline': 400
        },
        # 'SPIDER_MIDDLEWARES': {
        #     'earthsEmotions.middlewares.ObserverSeleniumMiddleware': 543
        # }
    }

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css("h1.jeg_post_title::text").get()
        article['author'] = response.css("div.jeg_meta_author a::text").get()
        article['datetime'] = response.css("div.jeg_meta_date a::text").get()
        article['body'] = response.css("div.content-inner > p::text").getall()

        yield article
