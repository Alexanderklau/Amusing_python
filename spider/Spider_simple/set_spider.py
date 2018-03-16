#coding: utf-8
__author__ = "Yemilice_lau"


import requests
from bs4 import BeautifulSoup
import re


pages = set()
def getLinks(pageUrl):
    global pages
    html = requests.get("http://en.wikipedia.org" + pageUrl).content
    bsObj = BeautifulSoup(html, 'lxml')
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            print (newPage)
            pages.add(newPage)
            getLinks(newPage)

getLinks("ls")