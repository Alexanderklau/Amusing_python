# coding: utf-8
__author__ = 'lau.wenbo'


from elasticsearch import Elasticsearch
from elasticsearch import helpers



es = Elasticsearch(hosts="10.0.20.19",port=9200)


def searchDoc(index=None, type=None, body=None):

    return es.search(index=index, doc_type=type, body=body)


def search_specify(index=None, type=None, keywords=None):
    # 查询包含的关键字的日志
    query = {
        'query': {
            'match': {
                'message': keywords
            }
        }
    }
    message = searchDoc(index, type, query)
    return message

def search_all(client=None, index=None, type=None):
    # 查询所有的日志
    query = {"query" : {"match_all" : {}}}
    scanResp = helpers.scan(client, query, scroll="10m", index=index, doc_type=type, timeout="10m")
    return scanResp



# a = search_all(client=es, index="user", type="message")
# for i in a:
#     print(i)