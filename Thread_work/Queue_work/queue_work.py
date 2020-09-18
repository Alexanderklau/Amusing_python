# coding: utf-8

__author__ = "lau.wenbo"


from queue import Queue
import random
import threading
import time

class Producer(threading.Thread):
    """
    Producer thread 制作线程
    """
    def __init__(self, t_name, queue):  # 传入线程名、实例化队列
        threading.Thread.__init__(self, name=t_name)  # t_name即是threadName
        self.data = queue

    """
    run方法 和start方法:
    它们都是从Thread继承而来的，run()方法将在线程开启后执行，
    可以把相关的逻辑写到run方法中（通常把run方法称为活动[Activity]）；
    start()方法用于启动线程。
    """

    def run(self):
        for i in range(5):  # 生成0-4五条队列
            print("%s: %s is producing %d to the queue!" % (time.ctime(), self.getName(), i))  # 当前时间t生成编号d并加入队列
            self.data.put(i)  # 写入队列编号
            time.sleep(random.randrange(10) / 5)  # 随机休息一会
        print("%s: %s producing finished!" % (time.ctime(), self.getName))  # 编号d队列完成制作


class Consumer(threading.Thread):
    """
    Consumer thread 消费线程，感觉来源于COOKBOOK
    """
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print("%s: %s is consuming. %d in the queue is consumed!" % (time.ctime(), self.getName(), val))  # 编号d队列已经被消费
            time.sleep(random.randrange(10))
        print("%s: %s consuming finished!" % (time.ctime(), self.getName()))  # 编号d队列完成消费


def main():
    """
    Main thread 主线程
    """
    queue = Queue()  # 队列实例化
    producer = Producer('Pro.', queue)  # 调用对象，并传如参数线程名、实例化队列
    consumer = Consumer('Con.', queue)  # 同上，在制造的同时进行消费
    producer.start()  # 开始制造
    consumer.start()  # 开始消费
    """
    join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
　　join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。
    """
    producer.join()
    consumer.join()
    print('All threads terminate!')


if __name__ == '__main__':
    main()