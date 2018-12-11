# coding: utf-8
__author__ = 'lau.wenbo'

import datetime
import random

from multiprocessing import Pool
import time


def mycallback(x):
    with open('/media/lau/datas/home/lau/Code/Go-project/Log_collector/monlog.log', 'a+') as f:
        f.writelines(str(x) + '\n')


def sayHi(num):
    node_list = ["node1", "node2", "node3"]
    times = str(datetime.datetime.now()).replace(" ", "T")
    level = ["WARNING", "ERROR", "NOTICE"]
    cluster = ["cpu", "cluster", "memeory", "disk"]
    message = "journal: system {cluster} {level} {clusters} load is overloaded".format(
        cluster=random.choice(cluster), level=random.choice(level),clusters=random.choice(cluster))
    w = times + " " + message
    return w


if __name__ == '__main__':
    e1 = time.time()
    pool = Pool()

    for i in range(10):
        pool.apply_async(sayHi, (i,), callback=mycallback)

    pool.close()
    pool.join()
    e2 = time.time()
    print float(e2 - e1)