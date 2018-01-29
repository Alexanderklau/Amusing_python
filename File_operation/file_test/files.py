# -*- coding:utf8 -*-
import os, os.path
import commands
import logging
import time
from datetime import datetime
from functools import wraps

Path = r"/home/lau/下载"


#函数递归遍历目录
def visitDir(arg, dirname, names):
    t1 = time.time()
    for filepath in names:     
        filename = os.path.join(dirname, filepath)
        #文件名处理
        filenames = filename_processing(filename)
        #读文件操作
        read_file(filenames)


#文件名的处理，文件名内含有空格，括号，书名号等，不能直接调用dd，在对文件名处理后进行调用
def filename_processing(filename):
    filename = filename.replace(" ", "\\ ").replace("(", "\\(").\
    replace(")", "\\)").replace("<", "\\<").replace(">", "\\>")
    return filename

#读文件
def read_file(filename):
    logging.basicConfig(filename='file.log', filemode="w", level=logging.DEBUG)
    if os.path.isdir(filename):
        print " %s It is a dictory!!" %(filename)
    else:
        file, output = commands.getstatusoutput('dd if=' + filename)
        #如果返回值=0，说明文件可以正常读取,反之则否
        if file == 0:
            logging.info('%s This is helath file!' %(filename))
        else:
            logging.warning("%s:%s:%s" %(datetime.now(),filename,output))


if __name__ == "__main__":
    os.path.walk(Path, visitDir, ())
