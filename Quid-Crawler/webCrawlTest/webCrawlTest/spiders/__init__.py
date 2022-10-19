import scrapy


# def parseAmazon(response):



class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        amazonUrl = f'https://www.amazon.com/s?k={self.searchTerm}'
        yield scrapy.Request(url=amazonUrl, callback=self.parse)

    def parse(self, response):
        products = response.css('div.s-result-item')
        for product in products:
            yield {
                "name": product.css('span.a-text-normal::text').get(),
                "price": product.css('span.a-offscreen::text').get(),
                "img": product.xpath('//img//@src').get(),
            }

