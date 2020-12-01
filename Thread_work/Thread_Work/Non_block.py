# coding: utf-8

__author__ = 'Yemilice_lau'

"""
一个带锁的框架
"""

import threading
import time

count = 0


# 做一个累加的函数
def add_num():
    global count
    if lock.acquire():  # 获得锁，并返回True
        tmp = count
        time.sleep(0.001)
        count = tmp + 1
        lock.release()  # 执行完释放锁


def run(add_fun):
    global count
    thread_list = []

    # 累加100次
    for i in range(100):
        t = threading.Thread(target=add_fun)
        t.start()
        thread_list.append(t)

    for j in thread_list:
        j.join()

    print(count)


if __name__ == '__main__':
    lock = threading.Lock()
    run(add_num)