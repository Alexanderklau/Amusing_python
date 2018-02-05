#coding: utf-8
__author__ = 'lau.wenbo'

import time
import psutil

def cpu():
    while True:
        time.sleep(1)
        cpu_liyonglv = psutil.cpu_percent()
        print "当前cpu利用率：\033[1;31;42m%s%%\033[0m"%cpu_liyonglv
#         if cpu_liyonglv >15.0:
#             baojing()
# def baojing():
#     i = 0
#     while i < 10 :
#         i += 1
#         time.sleep(0.5)
#         winsound.PlaySound("ALARM8",winsound.SND_ALIAS)
cpu()