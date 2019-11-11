# coding: utf-8

__author__ = 'lau.wenbo'

from faker import Faker
import datetime
import random
import chardet


fake = Faker(locale='zh_CN')

def work():
    actions = []

    # f = open('monlog.log')
    i = 1
    for line in range(1,2):
        size = random.randint(150000000, 159198796)
        length = random.randint(12, 20)
        beizhu02 = random.randint(10, 99)
        zhongyaoshijian = random.randint(10, 99)
        city = fake.city().encode('utf-8')
        name = fake.name().encode('utf-8')
        action = {
            "_index": "nj",
            "_type": "message",
            "_source": {
                      "Name" : "191029/17034304/1028_{city}新闻复播版_A2.wav".format(city=city),
                      "Bucket" : "u-9bq6ytjl9r6936q3",
                      "User" : "p-4517920181115172156",
                      "Time" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                      "Size" : size,
                      "Type" : "object",
                      "metadata" : {
                        "description" : "【标题】1028（男声+全文抠字） {name}分别对全市脱贫攻坚工作作出批示".format(name = name),
                        "title" : "20191028  媒资  南京新闻复播版",
                        "column" : "默认栏目",
                        "createdate" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "length" : "00:{time}:38:08".format(time = str(length)),
                        "privilege" : "公开",
                        "channel" : "融媒体新闻中心",
                        "beizhu02": "备注beizhu{baizhu}".format(baizhu = beizhu02),
                        "zhongyaorenwu": "{name}".format(name = name),
                        "zhongyaoshijian": "ert测试{zhongyaoshijian}".format(zhongyaoshijian=zhongyaoshijian)
                      }
            }
        }
        return action


z = work()
print z["_source"]