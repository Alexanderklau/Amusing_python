# coding: utf-8
__author__ = "Yemilice_lau"


import requests


files = requests.get("http://www.baidu.com").content
fhandle = open("1.html", "wb")
fhandle.write(files)
fhandle.close()