# coding: utf-8


'''
ES-python的诸多用法，封装为接口
'''

__author__ = 'lau.wenbo'


from elasticsearch import Elasticsearch


class ElasticSearchUtil:
    def __init__(self, port, host):
        self.host = host
        self.port = port
        self.conn = Elasticsearch([self.host, self.port])

    def __del__(self):
        self.close()

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
        return self

    def insertDocument(self, index, type, body, id=None):
        '''
        插入一条数据body到指定的index、指定的type下;可指定Id,若不指定,ES会自动生成
        :param index: 待插入的index值
        :param type: 待插入的type值
        :param body: 待插入的数据 -> dict型
        :param id: 自定义Id值
        :return:
        '''
        return self.conn.index(index=index, doc_type=type, body=body, id=id)

    def insertDataFrame(self, index, type, dataFrame):
        '''
        批量插入接口;
        bulk接口所要求的数据列表结构为:[{{optionType}: {Condition}}, {data}]
        其中optionType可为index、delete、update
        Condition可设置每条数据所对应的index值和type值
        data为具体要插入/更新的单条数据
        :param index: 默认插入的index值
        :param type: 默认插入的type值
        :param dataFrame: 待插入数据集
        :return:
        '''
        dataList = dataFrame.to_dict(orient='records')
        insertHeadInfoList = [{"index": {}} for i in range(len(dataList))]
        temp = [dict] * (len(dataList) * 2)
        temp[::2] = insertHeadInfoList
        temp[1::2] = dataList
        try:
            return self.conn.bulk(index=index, doc_type=type, body=temp)
        except Exception, e:
            return str(e)

    def deleteDocById(self, index, type, id):
        '''
        删除指定index、type、id对应的数据
        :param index:
        :param type:
        :param id:
        :return:
        '''
        return self.conn.delete(index=index, doc_type=type, id=id)

    def deleteDocByQuery(self, index, query, type=None):
        '''
        删除idnex下符合条件query的所有数据
        :param index:
        :param query: 满足DSL语法格式
        :param type:
        :return:
        '''
        return self.conn.delete_by_query(index=index, body=query, doc_type=type)

    def deleteAllDocByIndex(self, index, type=None):
        '''
        删除指定index下的所有数据
        :param index:
        :return:
        '''
        try:
            query = {'query': {'match_all': {}}}
            return self.conn.delete_by_query(index=index, body=query, doc_type=type)
        except Exception, e:
            return str(e) + ' -> ' + index

    def searchDoc(self, index=None, type=None, body=None):
        '''
        查找index下所有符合条件的数据
        :param index:
        :param type:
        :param body: 筛选语句,符合DSL语法格式
        :return:
        '''
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

    def search_all(self, index=None, type=None):
        # 查询所有的日志
        query = {'query': {'match_all': {}}}
        message = self.searchDoc(index, type, query)
        return message


    def getDocById(self, index, type, id):
        '''
        获取指定index、type、id对应的数据
        :param index:
        :param type:
        :param id:
        :return:
        '''
        return self.conn.get(index=index, doc_type=type, id=id)

    def updateDocByIGd(self, index, type, id, body=None):
        '''
        更新指定index、type、id所对应的数据
        :param index:
        :param type:
        :param id:
        :param body: 待更新的值
        :return:
        '''
        return self.conn.update(index=index, doc_type=type, id=id, body=body)


    def close(self):
     if self.conn is not None:
        try:
            self.conn.close()
        except Exception, e:
            pass
        finally:
            self.conn = None

if __name__ == '__main__':
    host = "10.0.6.118"
    port = "9200"
    esAction = ElasticSearchUtil(port, host)
    # print(esAction)
    # print esAction.check()

    # Index API
    # body = {"name": 'lucy2', 'sex': 'female', 'age': 10}
    # print esAction.insertDocument('demo', 'test', body)


    # Search API
    query2 = {
        'query': {
        'match': {
        'message': 'node'
        }
        }
    }
    # query = {'query': {'match_all': {}}}
    a =  esAction.searchDoc('monlog', 'mon', query2)["hits"]["hits"]
    print(a)
    # print(a)
    # query = {'query': {'term': {'name': 'jackaaa'}}}
    # print esAction.searchDoc('_index', '_type', query)
    # query = {'query': {'range': {'age': {'gt': 11}}}}
    # query = {'query': {'range': {'age': {'lt': 11}}}}
    # query = {'query': {'match': {'age': 1000}}}
    # print esAction.searchDoc('physique_city', 'physique', query)
    # print(esAction.searchDoc())

    # 批量插入接口
    # doc = [
    #     {"index": {}},
    #     {'name': 'jackaaa', 'age': 2000, 'sex': 'female', 'address': u'西安'},
    #     {"index": {}},
    #     {'name': 'jackbbb', 'age': 3000, 'sex': 'male', 'address': u'合肥'},
    #     {"index": {}},
    #     {'name': 'jackccc', 'age': 4000, 'sex': 'female', 'address': u'安徽'},
    #     {"index": {}},
    #     {'name': 'jackddd', 'age': 1000, 'sex': 'male', 'address': u'阜阳'},
    # ]
    # file_name = "monlog.log"
    # wbfile = open(file_name, 'r')
    # actions = []
    #
    # for line in wbfile:
    #     v_items = line.split(' ', 6)
    #     fields = line.split('\t')
    #     action = {
    #             "time": line.split("T")[0],
    #             "hostname": v_items[1],
    #             "user": v_items[3],
    #             "module": v_items[4],
    #             "level": v_items[5],
    #             "message": v_items[6].split('\n')[0]
    #         }
    #     print(action)
    #     print esAction.insertDocument('monlog', 'mon', body=action)
        # actions.append(action)
        # if len(actions) > 50:
        #     print esAction.insertDocument('demo', 'test', )
            # print(actions)
            # print(Elasticsearch([host]).bulk(index="monlog", doc_type="mon", body=actions))

    # Get API
    # print esAction.getDocById('demo', 'test', '6gsqT2ABSm0tVgi2UWls')

    # Update API
    # body = {'script': "ctx._source.remove('age')"}#删除字段
    # body = {'script': "ctx._source.address = '合肥'"}#增加字段
    # body = {"doc": {"name": 'jackaaa'}}#修改部分字段
    # print esAction.updateDocById('demo', 'test', '6gsqT2ABSm0tVgi2UWls', body)

    # Delete API
    # body = {"query": {"name": 'jackbbb', 'sex': 'male'}}
    # print esAction.deleteDocById('demo', 'test', 'grULY2ABJus46JkUMEH1')

    # Delete_By_Query API
    # query = {'query': {'match': {'sex': 'famale'}}}
    # query = {'query': {'range': {'age': {'lt': 11}}}}
    # print esAction.deleteDocByQuery(_index, query=query, type=_type)
    # print(esAction.deleteDocByQuery('physique_school', {'query': {'match_all': {}}}))
    # print(esAction.deleteAllDocByIndex('demo', 'test'))

    # _index = 'demo'
    # _type = 'test_df'
    # import pandas as pd
    # frame = pd.DataFrame({'name': ['tomaaa', 'tombbb', 'tomccc'],
    #                       'sex': ['male', 'famale', 'famale'],
    #                       'age': [3, 6, 9],
    #                       'address': [u'合肥', u'芜湖', u'安徽']})
    #
    # print esAction.insertDataFrame(_index, _type, frame)

    # Index DataFrame
    # esAction.insertDataFrame(_index, _type, frame)