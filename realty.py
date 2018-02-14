# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class RealtySpider(scrapy.Spider):
    name = 'realty'
    allowed_domains = ['99acres.com']
    #start_urls = ['https://www.99acres.com/property-rates-and-price-trends-in-hyderabad']

    def start_requests(self):
        yield SplashRequest(
            url='https://www.99acres.com/property-rates-and-price-trends-in-hyderabad',
            callback=self.parse,
        )

    def parse(self, response):
        for tbody in response.css('div > table.prTble'):
            yield {
                'locality':tbody.css('tr > td.tl::text').extract(),

            }

