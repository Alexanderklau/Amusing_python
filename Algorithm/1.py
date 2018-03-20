# coding: utf-8
__author__ = 'lau.wenbo'

import urllib2
import requests
import json
import datetime
from time import ctime,sleep
import threading


def dir_get():
    data = {'dirpath':'infinityfs1,1,123,1'}
    r = requests.post(url="http://10.0.20.240:9898/filesystem/quota/dir/get", data=data)
    a = r.json()
    d1 = json.dumps(a)
    return d1


def dir_set():
    data = {'dirpath':'infinityfs1,1,123,1',
            'quotavalue':'-1',
            'quotaunit':'B'}
    r = requests.post(url="http://10.0.20.240:9898/filesystem/quota/dir/set", data=data)
    a = r.json()
    d1 = json.dumps(a)
    return d1

for i in range(10000):
    print(dir_set())