import scrapy


class CasualspiderSpider(scrapy.Spider):
    name = "casualspider"
    allowed_domains = ["www.batabd.com"]
    start_urls = ["https://www.batabd.com/collections/casual-shoes"]

    def parse(self, response):
        pass
