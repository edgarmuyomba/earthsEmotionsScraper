from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from earthsEmotions.items import Article


class TheEastAfricanSpider(CrawlSpider):
    name = "theeastafrican"
    allowed_domains = ["theeastafrican.co.ke"]
    start_urls = ["https://www.theeastafrican.co.ke/"]
    rules = [
        Rule(LinkExtractor(allow=r"/tea/.*", restrict_css="ul.nav a"), follow=True),
        Rule(LinkExtractor(allow=r"/tea/[\w\-]+/[\w\-]+\-\d+$", deny=r"/tea/author-profiles/.*"), follow=True, callback="parse_items"),
    ]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'DOWNLOAD_DELAY': 2,
        'DOWNLOAD_TIMEOUT': 5,
        'CLOSESPIDER_ITEMCOUNT': 20,
        'LOG_LEVEL': 'INFO',
        'LOG_FILE': 'theeastafrican.log',
        'FEEDS': {
            'Outputs/theeastafrican.json': {
                'format': 'json'
            }
        },
        'ITEM_PIPELINES': {
            'earthsEmotions.pipelines.ugandaPipelines.TheEastAfricanPipeline': 300,
            'earthsEmotions.pipelines.dbPipelines.PostgresPipeline': 400
        }
    }

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css("header > h2::text").get()
        article['author'] = response.css("section.author strong::text").get()
        article['datetime'] = response.css("header > h6::text").get()
        article['body'] = response.css("section.body-copy > p::text").getall()

        yield article
