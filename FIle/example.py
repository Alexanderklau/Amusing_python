#!/usr/bin/env python  
# coding=utf-8
import os, os.path
import commands
import logging
import time
from datetime import datetime
from functools import wraps

Path = r"/home/lau/下载/"

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
    if os.path.isdir(filename):
        print " %s It is a dictory!!" %(filename)
    else:
        file, output = commands.getstatusoutput('dd if=' + filename)
        #如果返回值=0，说明文件可以正常读取,反之则否
        if file == 0:
            logging.info('%s This is helath file!' %(filename))
        else:
            logging.warning("%s:%s:%s" %(datetime.now(),filename,output))