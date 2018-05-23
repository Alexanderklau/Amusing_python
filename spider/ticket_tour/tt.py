# coding: utf-8
__author__ = 'lau.wenbo'

import requests
from lxml import etree

url = "http://b.jowong.com/login.do"



payload = "usid=scctkj&url=%2Fprovider%2Fticket%2Findex.do&random=5947&password=321654"
headers = {
    'Content-Type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

# html = etree.HTML(response.text)
#
# while html.xpath('/html/head/title')[0] != "门票预订-阿坝旅游网":
#     random = raw_input("请输入验证码: ")
#
