# coding: utf-8

__author__ = 'lau.wenbo'


from pymongo import MongoClient


conn = MongoClient("192.168.1.4", 27017)

db = conn.mydb

my_set = db.test_set

my_set.insert({"name":"zhangsan","age":18})

for i in my_set.find():
    print(i)