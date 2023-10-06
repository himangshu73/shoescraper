import scrapy


class CasualspiderSpider(scrapy.Spider):
    name = "casualspider"
    allowed_domains = ["www.batabd.com"]
    start_urls = ["https://www.batabd.com/collections/casual-shoes"]

    def parse(self, response):
        boxes = response.css("div.grid-item.col5.col-6.col-md-4.col-lg-3")

        for box in boxes:
            yield{
                'vendor'        : box.css("div.product-bottom a::text").get(),
                'name'          : box.css("div.product-bottom span::text").get().strip(),
                'old-price'     : box.css("span.old-price::text").get(),
                'special-price' : box.css("span.special-price::text").get(),
            }

        next_page =  response.css("li.text a ::attr(href)").getall()

        if next_page is not None:
            if len(next_page)>1:
                next_page_url = 'https://www.batabd.com'+next_page[1]
            else:
                next_page_url = 'https://www.batabd.com'+next_page[0]
            yield response.follow(next_page_url, callback=self.parse)