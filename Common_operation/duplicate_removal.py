# coding:utf-8
"""
去重操作，列表，字典，字典嵌套，列表嵌套
"""

# 去除列表内重复的字典，并且输出新列表
a = [{"id":0,"name":"kkk"},{"id":0,"name":"kkk"},{"id":1,"name":"kkk2"},{"id":1,"name":"kkk2"}]
new_a = [dict(t) for t in set([tuple(d.items()) for d in a])]

# 列表去重：并且排序
ids = [1,4,3,3,4,2,3,4,5,6,1]
news_ids = list(set(ids))
news_ids.sort()
# print(news_ids)

# 字典去重，并且按key值排序
t1 = [{'a':1}, {'a':2}, {'a':2}]
# dict([d.items()[0] for d in t1]).items()之外的部分纯粹是把列表内还原成一个字典
t2 = [{value:key} for key, value in dict([d.items()[0] for d in t1]).items()]

# 去重字典内嵌套的列表，输出
t3 = {"a":[1,2,3,4,5,6,2,3,4,2,1,2]}
print({"a":list(set(t3["a"]))})