# coding: utf-8
__author__ = 'lau.wenbo'

import requests
from lxml import etree


a = requests.get("http://b.jowong.com/provider/ticket/index.do")

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding":"gzip,deflate",
    "Accept-Language":"zh-CN,en-US;q=0.7,en;q=0.3",
    "Connection":"Keep-alive",
    "Content-Length":"75",
    "Content-Type":	"application/x-www-form-urlencoded",
    "Host":"b.jowong.com",
    "Referer":"http://b.jowong.com/provider/ticket/index.do",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/59.0",
    # "Cookie":"JSESSIONID=0001662QL0VKQMNXRuUbrjKkHB-:3UD7VVV8CU"
}


def get_code():
    url = "http://b.jowong.com/createimage?Rgb=255|0|0"
    ir = requests.get(url)
    sz = open('../easy_img/logo.jpeg', 'wb').write(ir.content)
    print('../easy_img/logo.jpeg', sz, 'bytes')


if __name__=='__main__':
    get_code()
    # random = input("请输入验证码: ")

    data = {
        "usid": "scctkjw",
        "url": "/provider/ticket/index.do",
        "random": "1555",
        "password":"321654"
    }

    s = requests.Session()
    a = s.post("http://b.jowong.com/login.do",headers=headers, data=data)
    print(a.text)