#coding: utf-8
__author__ = "Yemilice_lau"

"""
京东手机界面爬虫
"""
import requests
import re
import time
from lxml import etree


headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Host":"search.jd.com",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:59.0) Gecko/20100101 Firefox/59.0",
    "Upgrade-Insecure-Requests":"1",
    "Connection":"keep-alive",
    "Cache-Control":"max-age=0"
 }

def craw_spider(url):
    html = requests.get(url, headers=headers).content
    selector = etree.HTML(html, parser=None, base_url=None)
    context = selector.xpath('//*[@id="J_goodsList"]/ul/li[@class="gl-item"]/div/div[4]/a/@href')
    return context


url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&page=7"

for i in craw_spider(url):
    print i

a = "//item.jd.com/15103750807.html"
