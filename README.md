# USED SCRAPY FOR PYTHON WEB SCRAPING

# Used Parse Method Fantasy_19
> For website http://books.toscrape.com/catalogue/category/books/fantasy_19/

```sh
scrapy crawl fant -o o.csv
```

# Used Parse Method Sequential-art_5
> For website http://books.toscrape.com/catalogue/category/books/sequential-art_5/

```sh
scrapy crawl sart -o o.csv
```

# Used Parse Method Thriller_37
> For website http://books.toscrape.com/catalogue/category/books/thriller_37/index.html

```sh
scrapy crawl spider -o o.csv
```

# Used Rules And Dictionary
> for whole website http://books.toscrape.com/
```sh
scrapy crawl crawl -o o.csv
```

# Used Rules And Items
> for whole website https://www.sainsburys.co.uk/shop/gb/groceries'
```sh
scrapy crawl sains -o o.csv
```
# Code For Rules
```sh 
rules = [Rule(LinkExtractor(allow='groceries/'),
                  callback='parse_filter_book', follow=True)]
```
# Code For Items
```sh  
    def parse_filter_book(self, response):
        exists = response.xpath('//div[@class="pdp"]').extract_first()
        if exists:
            title = response.xpath('//div[@class="productTitleDescriptionContainer"]/h1/text()').extract_first()
            book = SainsburyItem() # New line
            book['title'] = title

            yield book
          
        else:
            print(response.url)    
```            
