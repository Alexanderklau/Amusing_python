#coding: utf-8
__author__ = "Yemilice_lau"


import requests
import bs4
import re
import datetime
import random



html = requests.get("http://en.wikipedia.org/wiki/Kevin_Bacon").content
bsObj = bs4.BeautifulSoup(html, "lxml")
for link in bsObj.find("div",
     {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!::).)*$")):
    if 'href' in link.attrs:
        print (link.attrs['href'])

