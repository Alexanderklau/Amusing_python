# coding: utf-8
__author__ = "Yemilice_lau"


import scrapy
from homecrawl.items import HomecrawlItem
import re

class Home(scrapy.Spider):
    name = 'home'

    allowed_domains = ['fang.com']
    # 爬取的地址
    start_urls = ['http://zu.cd.fang.com/house/i3100/']

    def parse(self, response):
        item = HomecrawlItem()
        for box in response.xpath('//html/body/div[5]/div[6]/div[1]/div[2]/dl'):
            print('+++++++++++++++++++')
            try:
                item['name'] = box.xpath(".//dd/p[1]/a/text()")[0].extract().strip()
                item['type'] = box.xpath(".//dd/p[2]/text()")[0].extract().strip()
            except:
                continue
            yield item