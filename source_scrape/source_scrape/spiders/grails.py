import scrapy   
from scrapy import Spider

class GrailsSpider(Spider):
    name = 'grails'
    allowed_domains = ['stockx.com']
    start_urls = ['https://stockx.com/sneakers/most-popular']

    def parse(self, response):
        # Extracting the content using css selectors
        titles = response.css('.plugin-title a::text').extract()
        downloads = response.css('.plugin-downloads::text').extract()
        # Give the extracted content row wise
        for item in zip(titles,downloads):
            # create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'downloads' : item[1],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info