# coding: utf-8


__author__ = "lau.wenbo"


from redis import StrictRedis,ConnectionPool

# 使用默认方式连接到数据库
pool = ConnectionPool(host='10.0.6.95', port=6379, db=0,decode_responses=True)
r = StrictRedis(connection_pool=pool)
r.set('one', 'first')
r.set('two', 'second')
print r.get('one')
print r.get('two')
r.sadd("set1", 33, 44, 55, 66)  # 往集合中添加元素
print(r.scard("set1"))  # 集合的长度是4
print(r.smembers("set1"))