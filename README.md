Scraping batabd.com using scrapy
1. Create .gitignore file
2. Create Virtual Environment
python -m venv venv
3. Install Scrapy
pip install scrapy
4. Create scrapy project
scrapy startproject casualscrap
5. Install ipython
pip install ipython
6. Add ipython shell in scrapy.cfg file
shell = ipython
7. Go to project folder
cd .\casualscrap\
8. Create scrapy spider
scrapy genspider casualspider https://www.batabd.com/collections/casual-shoes
9. Run scrapy shell
10. 
    fetch('https://www.batabd.com/collections/casual-shoes')
    response
    boxes = response.css("div.grid-item.col5.col-6.col-md-4.col-lg-3")
    len(boxes)
    box = boxes[5]
    box.css("div.product-bottom a::text").get()
    box.css("div.product-bottom span::text").get().strip()
    box.css("span.old-price::text").get()
    box.css("span.special-price::text").get()
11. Now Transfer this to casualspider.py file
12. Find next page url
    response.css("li.text a ::attr(href)").getall()
13. Added pagination and scraped all pages