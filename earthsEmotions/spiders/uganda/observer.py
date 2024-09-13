from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class ObserverSpider(CrawlSpider):
    name = "observer"
    allowed_domains = ["observer.ug"]
    start_urls = ["https://www.observer.ug"]
    rules = [
        Rule(LinkExtractor(allow=r'/index\.php/[a-z-]+$'), follow=True),
        Rule(LinkExtractor(
            allow=r'/index\.php/[a-z-]+/\d+-[a-z0-9-]+$'), callback='parse_items', follow=True)
    ]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'DOWNLOAD_DELAY': 2,
        'DOWNLOAD_TIMEOUT': 10,
        'CONCURRENT_REQUESTS': 10,
        'LOG_LEVEL': 'INFO',
        'LOG_FILE': 'observer.log',
        'FEED_URI': 'Outputs/observer.json',
        'FEED_FORMAT': 'json'
    }

    def parse_items(self, response):
        self.logger.debug(f"Parsing page:: {response.url}")
        title = response.css("h1[itemprop='name']::text").get()
        author = response.css("span[itemprop='name']::text").get()
        date = response.css("time[itemprop='datePublished']::text").get()
        body = response.css("span[itemprop='articleBody']").get()

        if title and date:
            return {
                "title": title,
                "author": author,
                "date": date
            }
        else:
            self.logger.debug(f"No article found on the page:: {response.url}")
