
## for whole website http://books.toscrape.com/
## scrapy crawl crawl -o o.csv
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SpiderSpider(CrawlSpider):
    name = 'crawl'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    base_url = 'http://books.toscrape.com/'

    rules = [Rule(LinkExtractor(allow='catalogue/'),
                  callback='parse_filter_book', follow=True)]

  
    def parse_filter_book(self, response):
        exists = response.xpath('//div[@id="product_gallery"]').extract_first()
        if exists:
            title = response.xpath('//div/h1/text()').extract_first()
            relative_image = response.xpath('//div[@class="item active"]/img/@src').extract_first()
            final_image = self.base_url + relative_image.replace('../..', '')
            price = response.xpath('//div[@class="product_price"]/p[@class="price_color" and 1]/text()').extract_first()
            stock = response.xpath('//p[@class="instock availability"]/text()').extract()[1].strip()
            stars = response.xpath('//div/p[contains(@class, "star-rating")]/@class').extract_first().replace('star-rating ', '')
            description = response.xpath('//div[@id="product_description"]/following-sibling::p/text()').extract_first()
            upc = response.xpath('//table[@class="table table-striped"]/tr[1]/td/text()').extract_first()
            price_excl_tax = response.xpath('//table[@class="table table-striped"]/tr[3]/td/text()').extract_first()
            price_inc_tax = response.xpath('//table[@class="table table-striped"]/tr[4]/td/text()').extract_first()
            tax = response.xpath('//table[@class="table table-striped"]/tr[5]/td/text()').extract_first()
            yield {
                'Title': title,
                'Image': final_image,
                'Price': price,
                'Stock': stock,
                'Stars': stars,
                'Description': description,
                'Upc': upc,
                'Price excl tax': price_excl_tax,
                'Price incl tax': price_inc_tax,
                'Tax': tax,
            }
        else:
            print(response.url)    
            
            

