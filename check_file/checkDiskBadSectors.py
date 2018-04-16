# coding:utf-8
import ctypes
import time
import os
import logging
import multiprocessing


# 规定目录
Path = "/infinityfs1"
# 日志文件
logging.basicConfig(filename="file.log", filemode="a+", level=logging.DEBUG)
# 断点文件
file_name = "file.tmp"
# 成功文件
success_file = "success.tmp"
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
        logging.warning("%s Error!" % (filename))
    else:
        success_files = open(success_file, "a+")
        success_files.write(filename + "\n")
        success_files.close()


def work(filename):
    # 开启10个进程
    p = multiprocessing.Pool(11)
    try:
       for i in filename:
           p.apply_async(read, args=(i,)).get(600)
       p.close()
       p.join()
    except KeyboardInterrupt:
       print "Caught KeyboardInterrupt, terminating workers"
       p.terminate()
       p.join()

def check_file():
    # 读取文件
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if os.path.exists(file_name):
        logging.info("Reload file log.....Now time: {0}".format(now_time))
        f = open(file_name)
        data = [line.strip() for line in f]
        data2 = [os.path.join(root,fn) for root,dirs,files in os.walk(Path)
                 for fn in files]
        # 这里用到了列表比较，对比file.txt和目录文件，剔除相同的文件，生成新的列表跑文件
        filename = list(set(data) ^ set(data2))
        work(filename)
    else:
        logging.info("File log Not found....Now time:{0}".format(now_time))
        filename = [os.path.join(root, fn) for root, dirs, files in os.walk(Path) for fn in files]
        work(filename)

if __name__=='__main__':
    t1 = time.time()
    check_file()
    t2 = time.time()
    # 删除txt文件
    if os.path.exists(file_name):
        os.remove(file_name)
    logging.info("ReadFile end! time：%d"%(int(t2-t1)))
