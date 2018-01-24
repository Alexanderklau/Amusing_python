#coding:utf-8
from multiprocessing import Process,Queue,Pool
import multiprocessing
import os, time, random

Path = r"/home/lau/下载/"
# 写数据进程执行的代码:
def write(q, lock):
    lock.acquire()
    for i in range(1, 10):
        print 'Put %s to queue...' %i
        os.path.walk(Path, visitDir, ())
        q.put(i)
    lock.release()

def visitDir(arg, dirname, names):
    for filepath in names:
        filename = os.path.join(dirname, filepath)
        print filename
# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print 'Get %s from queue.' % value
            time.sleep(random.random())
        else:
            break

if __name__=='__main__':
    manager = multiprocessing.Manager()
    # 父进程创建Queue，并传给各个子进程：
    q = manager.Queue()
    lock = manager.Lock()  # 初始化一把锁
    p = Pool()
    pw = p.apply_async(write, args=(q, lock))
    pr = p.apply_async(read, args=(q,))
    p.close()
    p.join()

    print
    print u'所有数据都写入并且读完'