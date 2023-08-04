import scrapy   
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pprint import pprint as ppr

class GrailsSpider(CrawlSpider):
    name = 'grails'
    allowed_domains = ['stockx.com']
    start_urls = ['https://stockx.com/new-balance-827-abzorb-aime-leon-dore']
    rules = (
        Rule(LinkExtractor(), callback='parse_items', process_links='keep_first_link', follow=True),
    )

    def keep_first_link(self, links):
        
        ppr(links)
        print(len(links))
        raise Exception()
        return links[0]

    def parse_items(self, response):
        url = response.url
        grail_name = response.css('h1::text').extract_first()
        last_sale_price = response.xpath('//*[@id="main-content"]/div/section/div/div[6]/div/div/div[1]/p').extract_first()
        print(grail_name)
        print(last_sale_price)
        print(url)
