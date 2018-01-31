# coding: utf-8
# 找到infinsty下所有的目录，写入到某文件和log中，然后再依次去读。
import os, time
import logging
import commands
from datetime import datetime
import multiprocessing

filename = "Directory.txt"
logging.basicConfig(filename='Directory.log', filemode="w", level=logging.DEBUG)


def create_dir():
    dir = []
    directory = os.path.expanduser("/home/lau/下载")
    for f in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, f)):
            ff = "/home/lau/下载/" + f
            files = file(filename, "a+")
            files.write(f)
            files.close()
            dir.append(ff)
    return dir


Path = create_dir()


# 写数据进程执行的代码:
def write(q, lock):
    lock.acquire()
    for i in Path:
        print(i)
        for value in [os.path.join(root, fn) for root, dirs, files in os.walk(i) for fn in files]:
            print 'Put %s to queue...' % value
            filename = value.replace(" ", "\\ ").replace("(", "\\(").replace(")", "\\)"). \
                replace("<", "\\<").replace(">", "\\>")
            # 写入队列
            q.put(filename, block=True, timeout=10)
    lock.release()


# 读数据进程执行的代码:
def read(q):
    while True:
        # 如果队列为空
        if not q.empty():
            filename = q.get(block=True, timeout=10)
            print 'Get %s from queue.' % filename
            logging.basicConfig(filename='file.log', filemode="w", level=logging.DEBUG)
            file, output = commands.getstatusoutput('dd if=' + filename)
            # 如果返回值=0，说明文件可以正常读取,反之则否
            if file == 0:
                pass
                # 正确的文件可以不写入日志，可调整。
                # logging.info('%s This is helath file!' % (filename))
            else:
                logging.warning("%s:%s:%s" % (datetime.now(), filename, output))
        else:
            print("Queue is empty")
            break


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    # 父进程创建Queue，并传给各个子进程：
    # 队列长度100
    q = manager.Queue(1000)
    # 锁
    lock = manager.Lock()
    # 进程池 = 10
    p = multiprocessing.Pool(10)
    # 写入队列
    pw = p.apply_async(write, args=(q, lock))
    time.sleep(5)
    # 从队列里读
    pr = p.apply_async(read, args=(q,))
    p.close()
    p.join()
    print '所有数据都已经读完'
