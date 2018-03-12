# coding: utf-8


import os
import time

res = os.fork()
print('res == %d'%res)
if res == 0:
    print('我是子进程,我的pid是:%d,我的父进程id是:%d'%(os.getpid(),os.getppid()))
else:
    print('我是父进程,我的pid是:%d'%os.getpid())