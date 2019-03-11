# coding: utf-8

__author__ = "lau.wenbo"


import psutil


# 获取CPU完整信息
print psutil.cpu_times()
# 获取单项数据信息，如用户User和CPU时间比
print psutil.cpu_times().user
# 获取CPU个数
print psutil.cpu_count()
# 获取CPU物理个数
print psutil.cpu_count(logical=True)
# 获取内存信息
mem = psutil.virtual_memory()
# 获取内存总数
print mem.total
# 获取空闲内存数
print mem.free
# 获取swpa分区信息
print psutil.swap_memory()