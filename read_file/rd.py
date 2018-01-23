# coding:utf-8
import ctypes
import time
import os
import logging
import multiprocessing

Path = '/home/lau'
logging.basicConfig(filename='file.log', filemode="w", level=logging.DEBUG)

def read(filename):
    print 'Get %s from queue.' % filename
    f = open("file.txt", "a+")
    f.write(filename + "\n")
    f.close()
    ll = ctypes.cdll.LoadLibrary
    lib = ll("./libpycall.so")
    file = lib.rd(filename)
    if file < 0:
        logging.warning("%s 错误！原因：%s" % (filename))
    else:
        print(file)


def work(filename):
    p = multiprocessing.Pool(11)
    for i in filename:
        p.apply_async(read, args=(i,))
    p.close()
    p.join()

def check_file():
    if os.path.exists("file.txt"):
        logging.info("读取日志文件.......")
        f = open("file.txt")
        data = [line.strip() for line in f]
        data2 = [os.path.join(root,fn) for root,dirs,files in os.walk(Path) for fn in files]
        filename = list(set(data) ^ set(data2))
        work(filename)
    else:
        logging.info("日志文件不存在......")
        filename = [os.path.join(root, fn) for root, dirs, files in os.walk(Path) for fn in files]
        work(filename)

if __name__=='__main__':
    t1 = time.time()
    check_file()
    t2 = time.time()
    logging.info("所有文件都已经读完，用时：%d"%(int(t2-t1)))