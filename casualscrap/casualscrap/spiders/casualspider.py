import scrapy


class CasualspiderSpider(scrapy.Spider):
    name = "casualspider"
    allowed_domains = ["www.batabd.com"]
    start_urls = ["https://www.batabd.com/collections/casual-shoes"]

    def parse(self, response):
        boxes = response.css("div.grid-item.col5.col-6.col-md-4.col-lg-3")

        for box in boxes:
            relative_url = box.css("div.product-bottom a.product-title ::attr(href)").get()
            shoe_url = 'https://www.batabd.com'+relative_url
            yield response.follow(shoe_url, callback=self.parse_shoepage)

        next_page =  response.css("li.text a ::attr(href)").getall()

        if next_page is not None:
            if len(next_page)>1:
                next_page_url = 'https://www.batabd.com'+next_page[1]
            else:
                next_page_url = 'https://www.batabd.com'+next_page[0]
            yield response.follow(next_page_url, callback=self.parse)    
    
    def parse_shoepage(self,response):
        yield {
            'URL'   : response.url,
            'Title' : response.css("h1.product-title span::text").get().strip(),
            'Brand' : response.css("div.vendor-product a::text").get().strip(),
            'SKU'   : response.css("div.sku-product span::text").get().strip(),
            'Inventory': response.css("div.product-inventory span::text").get().strip()
        }