from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from earthsEmotions.items import Article


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
        'CLOSESPIDER_ITEMCOUNT': 20,
        'LOG_LEVEL': 'INFO',
        'LOG_FILE': 'observer.log',
        'FEEDS': {
            'Outputs/observer.json': {
                'format': 'json'
            }
        },
        'ITEM_PIPELINES': {
            'earthsEmotions.pipelines.ugandaPipelines.ValidArticlePipeline': 200,
            'earthsEmotions.pipelines.ugandaPipelines.TheObserverPipeline': 300,
            'earthsEmotions.pipelines.aiPipelines.PolarityPipeline': 400,
            'earthsEmotions.pipelines.dbPipelines.PostgresPipeline': 500
        },
        'SPIDER_MIDDLEWARES': {
            'earthsEmotions.middlewares.ObserverSeleniumMiddleware': 543
        }
    }

    def parse_items(self, response):
        self.logger.debug(f"Parsing page:: {response.url}")
        article = Article()
        title = response.css("h1[itemprop='name']::text").get()
        author = response.css("span[itemprop='name']::text").get()
        datetime = response.css("time[itemprop='datePublished']").attrib.get('datetime')
        body = response.css("span[itemprop='articleBody'] > p::text").getall()

        if title and datetime:
            article['url'] = response.url
            article['title'] = title
            article['author'] = author
            article['datetime'] = datetime
            article['body'] = body

            yield article
        else:
            self.logger.debug(f"No article found on the page:: {response.url}")
