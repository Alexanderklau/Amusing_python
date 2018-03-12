# coding: utf-8
__author__ = 'lau.wenbo'


import psutil


p1 = psutil.Process(9042)

# 打印本机的内存信息
print ('直接打印内存占用： {0}'.format((str)(psutil.virtual_memory)))
# 打印内存的占用率
print ('获取内存占用率： {0}%'.format((str)(psutil.virtual_memory().percent)))
# 本机cpu的总占用率
print ("打印本机cpu占用率： {0}%".format((str)(psutil.cpu_percent(0))))
# 该进程所占cpu的使用率
print ("打印该进程CPU占用率: {0}%".format((str)(p1.cpu_percent(interval=1))))
# 直接打印进程所占内存占用率
print (p1.memory_percent)
# 格式化后显示的进程内存占用率
print "进程内存占用率: {:.2f}%".format(p1.memory_percent())

