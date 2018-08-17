# coding: utf-8


__author__ = "lau.wenbo"


import redis

r = redis.Redis(host="10.0.6.118", port=6379)
print(r)