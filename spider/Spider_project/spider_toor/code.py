# coding: utf-8
__author__ = "Yemilice_lau"


import requests
import time
import json

url = "http://b.jowong.com/createimage?Rgb=255|0|0"

login_url = "http://b.jowong.com/login.do"

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    'Postman-Token': "0d2098a0-6596-4e97-bec6-1488b3c65dcb"
    }

s = requests.session()

haha = s.get(url)

with open('code.jpg', 'wb') as f:
    f.write(haha.content)
print('请输入验证码:')
yanzhen = input()

data = "password=######&random={0}&url=%2Fprovider%2Fticket%2Findex.do&usid=######".format((yanzhen))

s.post(login_url, data=data, headers=headers)

while True:

    time.sleep(1)

    f = s.get("http://b.jowong.com/provider/ticket/ticketsearch.do?pdno=06001&rzti=2018-05-02&r=54")

    print(f.text)





