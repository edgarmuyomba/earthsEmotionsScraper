from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule 
from scrapy.linkextractors import LinkExtractor
from earthsEmotions.items import Article

class RedPepperSpider(CrawlSpider):
    name = "redpepper"
    allowed_domains = ["redpepper.co.ug"]
    start_urls = ["https://redpepper.co.ug/"]
    rules = [
        Rule(LinkExtractor(allow=r"/category/.*", restrict_css="li.menu-item > a"), follow=True),
        Rule(LinkExtractor(deny=r"/category/hyenas-tale/.*"), follow=False),
        Rule(LinkExtractor(allow=r"/[\w\-]+/\d+/$"), follow=True, callback="parse_items")
    ]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'DOWNLOAD_DELAY': 2,
        'DOWNLOAD_TIMEOUT': 5,
        'CLOSESPIDER_ITEMCOUNT': 5,
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
        }
    }

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url 
        article['title'] = response.css("h1.entry-title::text").get()
        article['author'] = response.css("span.posts-author").get()
        article['datetime'] = response.css("span.posts-date").get()
        article['body'] = response.css("div.entry-content > p::text").getall()
        
        return article