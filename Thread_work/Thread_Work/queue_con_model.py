# coding: utf-8

__author__ = 'Yemilice_lau'

import threading
import time
from queue import Queue


queue = Queue(20)


# 生产者
def Producer():
    i = 0
    print("开始线程")
    while True:
        i = i + 1
        print("生产数据", i, "现有数据", queue.qsize())
        time.sleep(1)
        queue.put(i)

# 消费者
def Consumer(m):
    while True:
        i = queue.get()
        time.sleep(0.5)
        print("消费数据", i)


if __name__ == "__main__":
    Th1 = threading.Thread(target=Producer, )

    Th2 = threading.Thread(target=Consumer, args=(2, ))

    Th2.start()
    Th1.start()

    Th1.join()
    Th2.join()