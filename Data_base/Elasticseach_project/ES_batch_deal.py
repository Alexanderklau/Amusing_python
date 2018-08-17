# coding: utf-8
__author__ = 'lau.wenbo'

'''
batch deal data for es
'''

from elasticsearch import Elasticsearch
from elasticsearch import helpers
import datetime

es = Elasticsearch(hosts="10.0.6.118",port=9200)

actions = []

f = open('monlog.log')
i = 1
for line in f:
    v_items = line.split(' ', 6)
    fields = line.split('\t')
    try:
        action = {
            "_index": "monlog",
            "_type": "monlog",
            "_id": i,
            "_source": {
                "time":line.split("T")[0],
                "hostname": v_items[1],
                "user": v_items[3],
                "module": v_items[4],
                "level": v_items[5],
                "message": v_items[6].split('\n')[0]
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
