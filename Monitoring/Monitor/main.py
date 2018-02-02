# coding: utf-8
__author__ = 'lau.wenbo'

"""
主启动程序 所有的源头
"""

from operation import run, Modify_configuration
import sys
import getopt
import json
import time



if __name__ == "__main__":
        print("#" * 30)
        print("选择相对应的监控服务")
        print("1:编辑配置文件\n"
              "2:获取CPU占比率前十的进程\n"
              "3:获取内存占比前十的进程\n"
              "4:获取指定进程的线程(需要输入进程名)\n"
              "5:获取指定进程的CPU，内存占比(需要输入进程名)\n"
              "6:查看正在进行的监控\n"
              "7:帮助")
        print("#" * 30)
        str = raw_input("输入相对应的数字: ")
        if str == "1":
            Modify_configuration.revise()
        else:
            pass





