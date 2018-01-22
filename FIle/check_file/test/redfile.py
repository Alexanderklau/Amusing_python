#coding: utf-8
__author__ = 'lau.wenbo'
# import ctypes
# ll = ctypes.cdll.LoadLibrary
# lib = ll("./libpycall.so")
# lib.rd("/home/lau/下载/2000W/200W-400W.csv")
# print '***finish***'
#coding: utf-8
import ctypes
import os, time
import logging
import commands
import multiprocessing

lib = ctypes.cdll.LoadLibrary("./libpycall.so")
Path = r"/home/lau/下载"
logging.basicConfig(filename='file.log', filemode="w", level=logging.DEBUG)


#读文件
def read(filename):
    print 'Get %s from queue.' % filename
    f = open("file.txt", "a+")
    f.write(filename + "\n")
    f.close()
    filenames = filename.replace(" ", "\\ ").replace("(", "\\(").replace(")", "\\)"). \
        replace("<", "\\<").replace(">", "\\>")
    file, output = lib.rd(Path)
    # file, output = commands.getstatusoutput('dd if=' + filenames)
        # 如果返回值=0，说明文件可以正常读取,反之则否
    if file == 0:
        pass
    else:
        logging.warning("%s 错误！原因" %(filenames))

#进程操作
def work(filename):
    p = multiprocessing.Pool(11)
    for i in filename:
        p.apply_async(read, args=(i,))
    p.close()
    p.join()

#检查日志，如果不存在就从头开始，如果存在就从上次断掉的地方开始
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