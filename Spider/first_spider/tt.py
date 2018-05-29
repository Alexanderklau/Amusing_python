# coding: utf-8
__author__ = 'lau.wenbo'

import requests

url = "http://b.jowong.com/login.do"

payload = "usid=scctkj&url=%2Fprovider%2Fticket%2Findex.do&random=1555&password=321654"

headers = {
    'Content-Type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)