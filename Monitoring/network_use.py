# coding: utf-8
__author__ = 'lau.wenbo'

import psutil
import time

count = psutil.net_io_counters()
print "发送字节数：\033[1;31;42m%s\033[0mbytes,接收字节数：\033[1;31;42m%s\033[0mbytes,发送包数：%s,接收包数%s" \
      % (count.bytes_sent, count.bytes_recv, count.packets_sent, count.packets_recv)

users = psutil.users()
print "当前登录用户：", users[0].name
# 时间
curent_time = psutil.boot_time()

curent_time_1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(curent_time))
print curent_time_1
