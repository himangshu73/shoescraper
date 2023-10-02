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

