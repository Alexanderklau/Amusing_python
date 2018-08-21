# coding: utf-8
__author__ = 'lau.wenbo'

from faker import Faker
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import datetime


fake = Faker()
name = fake.name()
address = fake.city()

es = Elasticsearch(hosts="10.0.6.118",port=9200)

actions = []

f = open('monlog.log')
i = 1
for line in range(1,30000):
    try:
        action = {
            "_index": "user",
            "_type": "message",
            "_id": i,
            "_source": {
                "name":name,
                "address":address
            }
        }
    except:
        continue
    i += 1
    actions.append(action)


data = len(actions)
print("开始导入{data}条数据.........".format(data=data))
starttime = datetime.datetime.now()
helpers.bulk(es, actions,request_timeout=100,raise_on_error=True)
endtime = datetime.datetime.now()
print("导入{data}数据的时间是{times}".format(data = data, times=(endtime - starttime).seconds))


