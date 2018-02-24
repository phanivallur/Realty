# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup
from locality import Locality
import json
import operator


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
        soup=BeautifulSoup(response.text,'lxml')
        data=[]
        for table in soup.find_all("table",{"class":"prTble"}):
            rows=table.find_all("tr")
            for row in rows:
                cols=row.find_all("td")
                cols=[ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])

        resultant_objects=self.create_objects(data)
        sorted_data=sorted(resultant_objects,key=operator.attrgetter('area'))
        i=1
        for obj in sorted_data:
            yield {
                str(i):obj.__str__()
            }
            i=i+1


    def create_objects(self,input):
        obj_list=[]
        i=1
        for obj in input:
            if len(obj) != 0:
                locality=Locality(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])
                obj_list.append(locality)
            i=i+1
        return obj_list






















