# coding: utf-8
__author__ = 'Yemilice_lau'

'''
设定为半年（180天）或空间使用率超过70%；
1、超过180天的数据自动删除。
2、超过70%的空间使用率的数据，按照时间顺序删除超过70%的数据
'''

'''
基础逻辑：
遍历文件夹，找出最后使用时间为180天以前的数据 或者 当所有的数据超过了70%，先排序，按照最后使用时间，从旧到新，依次删除
'''

import os
import time
import datetime
import psutil


def iter_files(rootDir):
    file_path = []
    now_time = datetime.datetime.today()
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            file_name = os.path.join(root, file)
            file_time = datetime.datetime.strptime(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.stat(file_name).st_mtime)), "%Y-%m-%d %H:%M:%S")
            if (now_time - file_time).days >= 180:
                file_path.append(file_name)
            else:
                continue
        for dirname in dirs:
            iter_files(dirname)
    return file_path


# delete
def delete_file(filePath):
    os.remove(filePath)


# 70%
def check_volume_info(rootDir):
    percents = psutil.disk_usage(rootDir).percent
    return percents


def get_file_list(file_path):
    dir_list = [os.path.join(root, fn) for root, dirs, files in os.walk(file_path)
                for fn in files]
    if not dir_list:
        return
    else:
        dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        return dir_list


def delete_volume_file(file_path):
    for i in get_file_list(file_path):
        print check_volume_info(file_path)
        if check_volume_info(file_path) < 70:
            break
        else:
            delete_file(i)


def delete_180_file(file_path):
    for i in iter_files(file_path):
        print i
        delete_file(i)


if __name__ == '__main__':
    file_path = ""
    delete_180_file(file_path)
    delete_volume_file(file_path)
