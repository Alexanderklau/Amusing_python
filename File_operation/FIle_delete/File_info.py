# coding: utf-8
__author__ = 'Yemilice_lau'

import os
import time
import datetime
import psutil


f_dir = os.path.abspath(os.path.dirname(__file__))


def delete_file(filePath):
    os.remove(filePath)


def get_dir_size(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size


def check_dir_info(dir):
    used_size = float(get_dir_size(dir) / 1024 / 1024)
    total_size = float(get_percent(dir) / 1024 / 1024)
    size = "%.2f" % (used_size/total_size*100)
    return size


def get_total(dir):
    total = psutil.disk_usage(dir).total
    return total


def get_percent(dir):
    percents = psutil.disk_usage(dir).percent
    return percents


def get_used(dir):
    used = psutil.disk_usage(dir).used
    return used


def get_delete_total(dir):
    if get_percent(dir) > 70:
        delete_precent = get_percent(dir) - 70
        delete_total = get_total(dir) * (delete_precent / 100)
        return delete_total


def get_file_list(file_path):
    dir_list = [os.path.join(root, fn) for root, dirs, files in os.walk(file_path)
                for fn in files]
    if not dir_list:
        return
    else:
        dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        return dir_list


def get_file_info(filr_path):
    info = os.path.getsize(filr_path)
    return info


def delete_volume_file(dir):
    z = 0
    for i in get_file_list(dir):
        if z >= get_delete_total(dir):
            break
        else:
            z = get_file_info(i) + z
            delete_file(i)


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


def delete_180_file(file_path):
    for i in iter_files(file_path):
        print i
        delete_file(i)



if __name__ == '__main__':
    file_path = 'G:\\baiduyundownload'
    delete_180_file(file_path)
    delete_volume_file(file_path)