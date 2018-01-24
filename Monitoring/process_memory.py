# coding: utf-8
__author__ = 'lau.wenbo'

# 打印出所有进程


import psutil

pid = psutil.pids()
print(pid)
for k, i in enumerate(pid):
    try:
        proc = psutil.Process(i)
        print  k,i,"%.2f%%" % (proc.memory_percent()), "%", proc.name(), proc.exe()

    except psutil.AccessDenied:
        print "psutil.AccessDenied"
