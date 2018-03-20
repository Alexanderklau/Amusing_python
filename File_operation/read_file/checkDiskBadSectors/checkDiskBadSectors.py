# coding:utf-8
import ctypes
import time
import os
import logging
import multiprocessing


# 规定目录
Path = "/infinity"
# 日志文件
logging.basicConfig(filename="file.log", filemode="w", level=logging.DEBUG)
# 断点文件
file_name = "file.tmp"
# 读文件函数，调取C语言写的动态库
def read(filename):
    print 'Get %s from queue.' % filename
    # 将已经读取过的文件写入到file.txt文件中，方便断点续跑
    f = open(file_name, "a+")
    f.write(filename + "\n")
    f.close()
    # ctypes加载c的dll文件
    ll = ctypes.cdll.LoadLibrary
    lib = ll("./libpycall.so")
    file = lib.rd(filename)
    # 如果文件损坏 or 不存在
    if file < 0:
        logging.warning("%s 错误!" % (filename))
    else:
        print(file)


def work(filename):
    # 开启10个进程
    p = multiprocessing.Pool(11)
    for i in filename:
        p.apply_async(read, args=(i,))
    p.close()
    p.join()

def check_file():
    # 读取文件
    if os.path.exists(file_name):
        logging.info("读取日志文件.......")
        f = open(file_name)
        data = [line.strip() for line in f]
        data2 = [os.path.join(root,fn) for root,dirs,files in os.walk(Path)
                 for fn in files]
        # 这里用到了列表比较，对比file.txt和目录文件，剔除相同的文件，生成新的列表跑文件
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
    # 删除txt文件
    if os.path.exists(file_name):
        os.remove(file_name)
    logging.info("所有文件都已经读完，用时：%d"%(int(t2-t1)))