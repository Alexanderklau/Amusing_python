#coding: utf-8
__author__ = "Yemilice_lau"


import requests
from bs4 import BeautifulSoup
html = requests.get("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.content,"lxml")
namelist = bsObj.find_all("span", {"class":"green"})
for name in namelist:
    print (name.get_text())