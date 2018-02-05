# -*- coding=utf-8 -*-


"""
每隔5秒输出本地时间到指定的文件
path: /home/test.py
"""

import time


filepath = 'test.log' # 文件路径
fm = '%Y-%m-%d %X'

def get_time():
    while 1:
        nowtime = time.strftime(fm, time.localtime())
        with open(filepath, 'a') as fp:
            fp.write(nowtime)
            fp.write('\n')
        time.sleep(5)
if __name__ == '__main__':
    get_time()
