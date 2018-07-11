# coding: utf-8
__author__ = "Yemilice_lau"


import requests

a = requests.get('http://zu.cd.fang.com/house/i3100/')
print(a.text)