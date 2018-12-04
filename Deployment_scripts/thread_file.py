# coding: utf-8
__author__ = 'lau.wenbo'

import csv
from multiprocessing import Pool  # 导入进程池
import datetime
import random


def mycallback(x):
    print(x)
    csv_write.writerow(x)


"""
2018-11-28T14:35:59.904281+08:00 node1 journal: system cpu WARNING cpu load is overloaded
"""
def sayHi(num):
    node_list = ["node1", "node2", "node3"]
    times = str(datetime.datetime.now()).replace(" ", "T")
    level = ["WARNING", "ERROR", "NOTICE"]
    cluster = ["cpu", "cluster", "memeory", "disk"]
    message = "journal: system {cluster} {level} {clusters} load is overloaded".format(
        cluster=random.choice(cluster), level=random.choice(level),clusters=random.choice(cluster))
    w = [times + " " + random.choice(node_list) + " " +  message]
    return w


if __name__ == '__main__':
    e1 = datetime.datetime.now()
    csv_file = open('test.log', 'w')
    csv_write = csv.writer(csv_file)
    p = Pool(10)

    for i in range(100000000):
        p.apply_async(sayHi, (i,), callback=mycallback)
    p.close()
    p.join()
    e2 = datetime.datetime.now()
    print((e2 - e1))
    csv_file.close()