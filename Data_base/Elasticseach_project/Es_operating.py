# coding: utf-8
__author__ = 'lau.wenbo'


from elasticsearch import Elasticsearch
from elasticsearch import helpers


class Es:
    def __init__(self):
        self.conn = Elasticsearch(hosts="10.0.6.214",port=9200)


    def check(self):
        '''
        输出当前系统的ES信息
        '''
        return self.conn.info()

    def check_health(self):
        '''
        检查集群的健康状态
        :return:
        '''
        status = self.conn.transport.perform_request('GET', '/_cluster/health', params=None)["status"]
        return status

    def searchDoc(self, index=None, type=None, body=None):

        return self.conn.search(index=index, doc_type=type, body=body)


    def search_specify(self, index=None, type=None, keywords=None):
        # 查询包含的关键字的日志
        query = {
            'query': {
                'match': {
                    'message': keywords
                }
            }
        }
        message = self.searchDoc(index, type, query)
        return message

    def search_all(self, client=None, index=None, type=None):
        # 查询所有的日志
        query = {"query" : {"match_all" : {}}}
        scanResp = helpers.scan(client, query, scroll="10m", index=index, doc_type=type, timeout="10m")
        return scanResp



if __name__ == '__main__':
    z = Es()
    a = z.search_specify(index="monlog", type="doc", keywords="cpu")
    print(a)
    a = z.search_all(client=z.conn, index="monlog", type="doc")
    for i in a:
        print(i["_source"]["message"])
# a = search_all(client=es, index="monlog", type="doc")
# for i in a:
#     print(i["_source"]["message"])
#
