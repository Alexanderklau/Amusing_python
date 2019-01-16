# coding: utf-8
__author__ = 'lau.wenbo'

from faker import Faker
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import datetime
from multiprocessing import Pool


fake = Faker(locale='zh_CN')
# name = fake.name()
# address = fake.city()

es = Elasticsearch(hosts="10.0.7.127",port=9200)

def work():
    actions = []

    # f = open('monlog.log')
    i = 1
    for line in range(1,10000):
        try:
            action = {
                "_index": "user",
                "_type": "message",
                "_source": {
                    "name":fake.name(),
                    "address":fake.city()
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

if __name__=='__main__':
    p = Pool(4)
    for i in range(10):
        p.apply_async(work(), args=(i,))
        print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

