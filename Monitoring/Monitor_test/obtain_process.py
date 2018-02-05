# coding: utf-8
__author__ = 'lau.wenbo'


# 进程检测程序
import psutil
import types
import datetime

# 获取用户输入的PID
def get_pid():
    pid = psutil.pids()
    return pid

def message():
    for i in get_pid():
        p = psutil.Process(i)
        print('Pid : %s' %i)
        print('进程名 : %s' % p.name())
        print('进程状态 : %s' % p.status())
        print('CPU占用率 : %s%%' % p.cpu_percent(interval=1))
        print('内存使用情况 : %s%%' % p.memory_percent())
        print('进程的线程数 : %s' % p.num_threads())

message()