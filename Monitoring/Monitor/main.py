# coding: utf-8
__author__ = 'lau.wenbo'

"""
主启动程序 所有的源头
"""

from operation import run, Modify_configuration, get_cpu_top, get_memory_top
import sys
import getopt
import json
import time



if __name__ == "__main__":
    while True:
        print("#" * 30)
        print("监控将全部记入日志")
        print("选择相对应的监控服务")
        print("1:编辑配置文件\n"
              "2:根据配置文件监控符合条件的进程\n"
              "3:监控CPU占比率前十的进程\n"
              "4:监控内存占比前十的进程\n"
              "5:获取指定进程的线程(需要输入进程名)\n"
              "6:获取指定进程的CPU，内存占比(需要输入进程名)\n"
              "7:查看正在进行的监控\n"
              "8:帮助\n"
              "9:退出")
        print("#" * 30)
        str = raw_input("输入相对应的数字: ")
        if str == "1":
            Modify_configuration.revise()
        elif str == "2":
            pass
        elif str == "3":
            get_cpu_top.get_cpu()
        elif str == "4":
            get_memory_top.get_memory()
        elif str == "5":

        else:
            pass





