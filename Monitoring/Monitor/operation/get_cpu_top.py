# coding: utf-8
__author__ = 'lau.wenbo'


import sys
sys.path.append("..")
from Monitor import Monitor_process
import run
import time


def get_cpu():
    print "请选择监控模式......."
    str = raw_input("1: 定时监控\n"
                    "2: 自定义监控\n"
                    "输入相对应的数字: ")
    while True:
        if str == "1":
            strs = raw_input("您想要多久检查一次CPU占用前十的进程？输入数字，单位：秒")
            try:
                if int(strs) > 0:
                    print "开始监控，请关注日志信息.........."
                    run.run_timing(Monitor_process.run_get_cpu, int(strs))
                    break
                else:
                    print "输入的不是合法数字！返回上一步!"
                    time.sleep(0.5)
                    pass
            except:
                print "输入的不是合法数字! 返回上一步!"
                time.sleep(0.5)
                pass
        elif str == "2":
            strs = raw_input("您想要多久检查一次CPU占用前十的进程？输入数字，单位：秒")
            try:
                if int(strs) > 0:
                    strk = raw_input("您想要检查几次？输入次数: ")
                    try:
                        if int(strk) > 0:
                            print "开始监控，请关注日志信息.........."
                            run.run_free(Monitor_process.run_get_cpu, int(strk), int(strs))
                            sys.exit()
                        else:
                            pass
                    except:
                        break
                else:
                    print "输入的不是合法数字！返回上一步!"
                    time.sleep(0.5)
                    pass
            except:
                print "输入的不是合法数字! 返回上一步!"
                time.sleep(0.5)
                pass

