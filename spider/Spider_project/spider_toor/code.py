# coding: utf-8
__author__ = "Yemilice_lau"


import requests
import time
import json
from lxml import etree

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

data = "password=321654&random={0}&url=%2Fprovider%2Fticket%2Findex.do&usid=scctkj".format((yanzhen))

s.post(login_url, data=data, headers=headers)

while True:

    time.sleep(5)

    f = s.get("http://b.jowong.com/provider/ticket/index.do")

    root = etree.HTML(f.content)

    bznote = root.xpath('/html/body/div[5]/form/div/input//@value')

    print(bznote[0])

    # if len(bznote) == 0:
    #     continue
    # else:
    #     bznote1 = bznote[0]
    #
    x = s.get("http://b.jowong.com/provider/ticket/ticketsearch.do?pdno=06001&rzti=2018-05-03")
    #
    add_message_url = "http://b.jowong.com/team/addTourist.do?" \
                      "bznote={0}&" \
                      "credentialstype=01&credentials=650404399405968403&mobile=13288495869".format(bznote[0])
    #
    print(add_message_url)
    #
    # k = s.get(add_message_url)
    #
    # print(k.text)






