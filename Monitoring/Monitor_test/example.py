# coding: utf-8
__author__ = 'lau.wenbo'

#coding=utf-8
import psutil
import sys
import time
def get_cpu_info(PID):
    cpucount = psutil.cpu_count(logical=True)
#传入进程PID，实现监测功能
    process = psutil.Process(int(PID))
    cpupercent = process.cpu_percent(interval=0.01)
#得到进程CPU占用，同资源检测管理器的数据
    cpu = int(cpupercent / cpucount)
    print(cpu)

get_cpu_info(19720)