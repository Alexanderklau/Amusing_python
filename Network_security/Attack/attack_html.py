# coding: utf-8
__author__ = 'lau.wenbo'

import requests
import random, string, time, _thread
import json


def doSomething(threadName, times):
    print(threadName, "\t", "第{0}次".format(times), "开始")
    qqnumber = random.randrange(12345678, 999999999)
    qqpasslen = random.randrange(8, 14)
    t = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz.', qqpasslen)
    qqpass = ''.join(t)
    data = {
        "name": '{0}'.format(qqnumber),
        "pass": qqpass,
        "code": "emil",
        "uid": 111,
        "tempId": 143
    }
    header = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Proxy-Connection": "keep-alive",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",

    }
    r = requests.post("url", data=data, headers=header)
    text1 = r.text
    r_data = json.loads(r.text)
    if r_data["Status"] == "ERROR":
        time.sleep(random.randrange(4, 10))
        r = requests.post("url", data=data, headers=header)
        text2 = r.text
        print(threadName, "\t", "第{0}次".format(times), "\t", data, "\t", text1, "\t", text2)
    else:
        print(threadName, "\t", "第{0}次".format(times), "\t", data, "\t", text1)


def do100times(threadName):
    for i in range(0, 10000):
        doSomething(threadName, i)


for i in range(0, 10):
    try:
        _thread.start_new_thread(do100times, ("线程：{0}".format(i),))
    except:
        print("创建线程失败")

while 1:
    pass