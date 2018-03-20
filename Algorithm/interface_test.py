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
    r = requests.post(url="http://10.0.20.77:9898/filesystem/quota/dir/get", data=data)
    a = r.json()
    d1 = json.dumps(a)
    return d1


def dir_set():
    data = {'dirpath':'infinityfs1,1,123,1',
            'quotavalue':'-1',
            'quotaunit':'B'}
    r = requests.post(url="http://10.0.20.77:9898/filesystem/quota/dir/set", data=data)
    a = r.json()
    d1 = json.dumps(a)
    return d1


def t1(func):
    for i in range(1000):
        starttime = datetime.datetime.now()
        s = dir_set()
        a = dir_get()
        endtime = datetime.datetime.now()
        print "round:%s, tread number:%s, tread number:%s, returnValue:%s,time:%f" % (
            i, func, a, s, (endtime - starttime).microseconds / 1000)
        sleep(1)


if __name__ == '__main__':
    threads = []
    for i in range(1000):
        name = "t%s" % (i)
        name = threading.Thread(target=t1, args=(i,))
        threads.append(name)

    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
