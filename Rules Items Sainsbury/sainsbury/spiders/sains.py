
## for whole website https://www.sainsburys.co.uk/shop/gb/groceries'
## scrapy crawl sains -o o.csv
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import SainsburyItem 
import scrapy



class SpiderSpider(CrawlSpider):
    name = 'sains'
    allowed_domains = ['www.sainsburys.co.uk']
    start_urls = ['https://www.sainsburys.co.uk/shop/gb/groceries']
    base_url = 'http://books.toscrape.com/'

    rules = [Rule(LinkExtractor(allow='groceries/'),
                  callback='parse_filter_book', follow=True)]

  
    def parse_filter_book(self, response):
        exists = response.xpath('//div[@class="pdp"]').extract_first()
        if exists:
            title = response.xpath('//div[@class="productTitleDescriptionContainer"]/h1/text()').extract_first()
            book = SainsburyItem() # New line
            book['title'] = title

            yield book
          
        else:
            print(response.url)    
            
            

