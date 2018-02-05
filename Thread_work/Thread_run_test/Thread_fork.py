#!/usr/bin/env python
# coding=utf8

import os, time

# 创建子进程之前声明的变量
source = 10

try:
    pid = os.fork()

    if pid == 0:  # 子进程
        print "这是子进程"
        # 在子进程中source自减1
        source = source - 1
        time.sleep(3)
    else:  # 父进程
        print "这是父进程"

    print source
except OSError, e:
    pass
