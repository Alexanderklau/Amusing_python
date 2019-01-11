# coding: utf-8
__author__ = 'lau.wenbo'

import os.path
import datetime
import time
import shutil

now_time = datetime.datetime.now()

def get_file():
    Path = "/infinityfs1"
    data = [os.path.join(root,fn) for root,dirs,files in os.walk(Path)
                     for fn in files]

    return data

def check_file_time():
    file_list = []
    for i in get_file():
        statinfo = os.stat(i)
        timestamp = statinfo.st_ctime
        time_local = time.localtime(timestamp)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        a = datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
        if now_time - a > datetime.timedelta(days=14):
            file_list.append(i)
        else:
            continue
    return file_list

def opertion_file():
    for i in check_file_time():
        os.remove(i)