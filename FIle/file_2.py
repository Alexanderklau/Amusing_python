#!/usr/bin/env python
# coding=utf-8

import os, os.path
from datetime import datetime
import logging
import commands
import time
from multiprocessing import Pool
import multiprocessing
import Queue

def scan_files(directory, prefix=None, postfix=None):
    files_list = []

    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))

    return files_list

def filename_processing(filename):
    filename = filename.replace(" ", "\\ ").replace("(", "\\(").\
    replace(")", "\\)").replace("<", "\\<").replace(">", "\\>")
    return filename

#读文件
def read_file(lock, filename):
    logging.basicConfig(filename='file.log', filemode="w", level=logging.DEBUG)
    with lock:
        if os.path.isdir(filename):
            print " %s It is a dictory!!" %(filename)
        else:
            file, output = commands.getstatusoutput('dd if=' + filename)
        #如果返回值=0，说明文件可以正常读取,反之则否
            if file == 0:
                print 'sss'
            # logging.info('%s This is helath file!' %(filename))
            else:
                print 'xxx'
            # logging.warning("%s:%s:%s" %(datetime.now(),filename,output))

def prints(i):
    return i

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    s = time.time()
    for i in (scan_files("/Users")):
        prints(i)
    e1 = time.time()
    print "顺序执行时间：", int(e1 - s)
    print 'concurrent:'  # 创建多个进程，并行执行
    pool = multiprocessing.Pool(multiprocessing.cpu_count())  # 创建拥有5个进程数量的进程池
    # testFL:要处理的数据列表，run：处理testFL列表中数据的函数
    rl = pool.apply_async(prints, scan_files("/Users"))
    pool.close()  # 关闭进程池，不再接受新的进
    pool.join()  # 主进程阻塞等待子进程的退出
    e2 = time.time()
    print "并行执行时间：", int(e2 - e1)
#print len(scan_files("/Users"))