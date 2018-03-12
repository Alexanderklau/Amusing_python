# coding: utf-8
__author__ = 'lau.wenbo'

import time

def run_timing(func, check_time):
    while True:
        try:
            # 睡眠
            time_remaining = check_time - time.time() % check_time
            func()
            time.sleep(time_remaining)
        except Exception, e:
            print e


def run_free(func, number, check_time):
    for i in range(number+1):
        time_remaining = check_time - time.time() % check_time
        func()
        time.sleep(time_remaining)





