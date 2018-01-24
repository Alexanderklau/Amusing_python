#!/usr/bin/env python  
# coding=utf-8
import os, os.path
import commands
import logging
import time
from datetime import datetime
from functools import wraps
from multiprocessing import Process
import multiprocessing

Path = r"/home"

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



def read_file(filename):
    logging.basicConfig(filename='file.log', filemode="w", level=logging.DEBUG)
    filenames = filename.replace(" ", "\\ ").replace("(", "\\("). \
        replace(")", "\\)").replace("<", "\\<").replace(">", "\\>")
    if os.path.isdir(filenames):
        print " %s It is a dictory!!" %(filenames)
    else:
        file, output = commands.getstatusoutput('dd if=' + filenames)
        #如果返回值=0，说明文件可以正常读取,反之则否
        if file == 0:
            logging.info('%s This is helath file!' %(filenames))
        else:
            logging.warning("%s:%s:%s" %(datetime.now(),filenames,output))

if __name__=='__main__':
    e1 = time.time()
    print "开始"
    print 'concurrent:'  # 创建多个进程，并行执行
    pool = multiprocessing.Pool(40)
    file = scan_files(Path)
    # print(file)
    pool.map(read_file,file)
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    e2 = time.time()
    print "并行执行时间：", int(e2 - e1)
