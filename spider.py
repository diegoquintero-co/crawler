import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)

import scrapy
class spider1(scrapy.Spider):
    name = 'Uscreen'
    #url of the website to be scrapped
    start_urls = ['https://help.uscreen.tv/en/']
    def parse(self, response):
        #CSS selector for the parent element
        for e in response.css('div.collection_meta'):
            yield {
                #CSS selectors for the child elements
                'title': ''.join(e.css('h2.t__h3.c__primary::text').extract()).strip(),
                'short_description': ''.join(e.css('p.paper__preview::text').extract()).strip(),
            }
        print("The page has been scrapped")
        pass