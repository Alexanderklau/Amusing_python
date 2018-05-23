# coding: utf-8
__author__ = 'lau.wenbo'

import requests

url = "http://b.jowong.com/login.do"

payload = "usid=scctkj&url=%2Fprovider%2Fticket%2Findex.do&random=8501&password=321654"

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    'Postman-Token': "53b9e040-9631-45bf-b73c-73b317e8ab7e"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)