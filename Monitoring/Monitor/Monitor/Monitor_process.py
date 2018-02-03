# coding: utf-8
__author__ = 'lau.wenbo'

"""
监控分为持续监控和自定义监控
持续监控会每60s统计出占比前十的进程，不停的将其打入日志
自定义监控可以自定监控的频率，监控指定进程，打印所需要的数据
例如固定进程的CPU，内存，线程占用等
"""
import sys
sys.path.append("..")
from Check import check_cpu, check_memory, check_process, check_threading
from Log import monitor_log
import getopt
import json
import time


f = open("/Monitor/setting.json", "r")
setting = json.load(f)
cpu_max = float(setting["CPU_max"])
memeory_max = float(setting["Memory_max"])
check_time = setting["time"]



def run_process_have():
    return check_threading.process_have(cpu_max, memeory_max)


def run_check_process(name):
   return check_process.get_process(name)


def run_check_process_thread(name):
    return check_process.get_process(name)


def run_get_cpu():
    return check_cpu.get_cpu_none()


def run_get_memory():
    return check_memory.get_memory()


def run_get_cpu_have():
    return check_cpu.get_cpu_have(cpu_max)


def run_get_memory_have():
    return check_memory.get_memory_have(memeory_max)