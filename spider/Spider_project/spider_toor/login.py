# coding: utf-8
__author__ = "Yemilice_lau"

import requests

url = "http://b.jowong.com/login.do"

payload = "password=321654&random=7366&url=%2Fprovider%2Fticket%2Findex.do&usid=scctkj"

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    'Postman-Token': "0d2098a0-6596-4e97-bec6-1488b3c65dcb"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)