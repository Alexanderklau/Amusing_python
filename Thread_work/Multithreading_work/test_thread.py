# coding: utf-8

__author__ = 'Yemilice_lau'

import thread
from time import sleep, ctime

loops = [4, 2]  # 等待时间


# 锁序号 等待时间 锁对象
def loop(nloop, nsec, lock):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()  # 解锁


def main():
    print 'starting at:', ctime()
    locks = []
    nloops = range(len(loops))  # 以loops数组创建列表并赋值给nloops

    for i in nloops:
        lock = thread.allocate_lock()  # 创建锁对象
        lock.acquire()  # 获取锁对象 加锁
        locks.append(lock)  # 追加到locks[]数组中

    # 执行多线程 (函数名,函数参数)
    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    # 循环等待顺序检查每个所都被解锁才停止
    for i in nloops:
        while locks[i].locked():
            pass

    print 'all end:', ctime()


if __name__ == '__main__':
    main()