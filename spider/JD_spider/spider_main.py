#coding: utf-8
__author__ = "Yemilice_lau"

"""
京东手机界面爬虫
"""
import requests
import re
import time
from urllib2 import urlopen


def craw_spider(url):
    html = requests.get(url)


url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&page=7"
print craw_spider(url)