from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule 
from scrapy.linkextractors import LinkExtractor
from earthsEmotions.items import Article

class RedPepperSpider(CrawlSpider):
    name = "redpepper"
    allowed_domains = ["redpepper.co.ug"]
    start_urls = ["https://redpepper.co.ug/"]
    rules = [
        # Rule(LinkExtractor(deny=r"hyena"), follow=False),
        Rule(LinkExtractor(allow=r"/category/.*", restrict_css="li.menu-item > a"), follow=True),
        Rule(LinkExtractor(allow=r"/[a-zA-Z0-9\-]+/[0-9]+/$"), follow=True, callback="parse_items")
    ]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'DOWNLOAD_DELAY': 2,
        'DOWNLOAD_TIMEOUT': 10,
        'CLOSESPIDER_ITEMCOUNT': 20,
        'LOG_LEVEL': 'INFO',
        'LOG_FILE': 'redpper.log',
        'DEPTH_PRIORITY': 1,
        'FEEDS': {
            'Outputs/redpepper.json' : {
                'format': 'json'
            }
        },
        'DOWNLOADER_MIDDLEWARES': {
            "earthsEmotions.middlewares.RedPepperSeleniumMiddleware": 543
        },
        'ITEM_PIPELINES': {
            'earthsEmotions.pipelines.dataFormattingPipelines.ValidArticlePipeline': 200,
            'earthsEmotions.pipelines.ugandaPipelines.RedPepperPipeline': 300,
            'earthsEmotions.pipelines.dataFormattingPipelines.StandardDatePipeline': 400,
            'earthsEmotions.pipelines.aiPipelines.PolarityPipeline': 500,
            'earthsEmotions.pipelines.dbPipelines.PostgresPipeline': 600
        }
    }

    def parse_items(self, response):
        self.logger.info(f"Parsing:: {response.url}")
        article = Article()
        article['url'] = response.url 
        article['title'] = response.css("h1.entry-title::text").get()
        article['author'] = response.css("span.posts-author > a::text").get()
        article['datetime'] = response.css("span.posts-date > a::text").get()
        article['body'] = response.css("div.entry-content > p::text").getall()
        
        yield article