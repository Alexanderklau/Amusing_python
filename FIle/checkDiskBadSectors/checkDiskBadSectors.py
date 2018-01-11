#coding: utf-8
import os, time, random
import logging
import commands
from datetime import datetime
import multiprocessing


Path = r"/home/lau"


# 写数据进程执行的代码:
def write(q, lock):
 lock.acquire()
 for value in [os.path.join(root,fn) for root,dirs,files in os.walk(Path) for fn in files]:
     print 'Put %s to queue...' % value
     filename = value.replace(" ", "\\ ").replace("(", "\\(").replace(")", "\\)").\
         replace("<", "\\<").replace(">", "\\>")
     # 写入队列
     q.put(filename,block=True,timeout=10)
 lock.release()

# 读数据进程执行的代码:
def read(q):
    while True:
        #如果队列为空
        if not q.empty():
            filename = q.get(block=True,timeout=10)
            print 'Get %s from queue.' % filename
            logging.basicConfig(filename='file.log', filemode="w", level=logging.DEBUG)
            #if os.path.isdir(filename):
            #    print " %s It is a dictory!!" % (filename)
            #else:
            #    pass
            file, output = commands.getstatusoutput('dd if=' + filename)
                # 如果返回值=0，说明文件可以正常读取,反之则否
            if file == 0:
                pass
                #    #正确的文件可以不写入日志，可调整。
                #    # logging.info('%s This is helath file!' % (filename))
            else:
                logging.warning("%s:%s:%s" % (datetime.now(), filename, output))
        else:
            print("Queue is empty")
            break

if __name__=='__main__':
    t1 = time.time()
    manager = multiprocessing.Manager()
    # 父进程创建Queue，并传给各个子进程：
    # 队列长度100
    q = manager.Queue(1000)
    #锁
    lock = manager.Lock()
    # 进程池 = 10
    p = multiprocessing.Pool(10)
    #写入队列
    pw = p.apply_async(write, args=(q,lock))
    time.sleep(10)
    #从队列里读
    pr = p.apply_async(read, args=(q,))
    p.close()
    p.join()
    t2 = time.time()
    print '时间 %d' % (int(t2 - t1))
    print '所有数据都已经读完'
