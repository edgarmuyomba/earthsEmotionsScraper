from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class NewVisionSpider(CrawlSpider):
    name = "newvision"
    allowed_domains = ["newvision.co.ug"]
    start_urls = ["https://www.newvision.co.ug/category/news"]
    rules = [
        Rule(LinkExtractor(deny=r".*undefined.*")),
        Rule(LinkExtractor(allow=r"/category/[0-9a-zA-Z\-_]/"), callback="parse_items", follow=True),
        Rule(LinkExtractor(allow=r"/category/[0-9a-zA-Z]"), follow=True),
    ]
    custom_settings = {
        'USER_AGENT': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        'DOWNLOAD_DELAY': 2,
        'DOWNLOAD_TIMEOUT': 10,
        'CONCURRENT_REQUESTS': 10,
        'LOG_LEVEL': 'DEBUG',
        'LOG_FILE': 'newvision.log',
        'FEED_URI': 'Outputs/newvision.json',
        'FEED_FORMAT': 'json'
    }

    def parse_items(self, response):
        title = response.css("h1.main_heading::text").get()
        subtitle = response.css("h3.sub_title::text").get()
        date = response.css("p.time_formatting_line").get()
        
        return {
            "title": title,
            "subtitle": subtitle,
            "date": date
        }
