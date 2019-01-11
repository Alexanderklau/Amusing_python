# coding: utf-8
__author__ = 'lau.wenbo'

import psutil
import os, datetime, time


def getMemCpu():
    data = psutil.virtual_memory()
    total = data.total  # 总内存,单位为byte
    free = data.available  # 可以内存
    memory = "Memory usage:%d" % (int(round(data.percent))) + "%" + "  "
    cpu = "CPU:%0.2f" % psutil.cpu_percent(interval=1) + "%"
    return memory + cpu


def main():
    while (True):
        info = getMemCpu()
        print info
        time.sleep(0.2)
        print info + "\b" * (len(info) + 1),


if __name__ == "__main__":
    main()