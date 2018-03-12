# coding: utf-8
__author__ = 'lau.wenbo'

import time


filepath = '/media/lau/datas/home/lau/log/test.log' # 文件路径
fm = '%Y-%m-%d %X'

def get_time():
    while 1:
        nowtime = time.strftime(fm, time.localtime())
        with open(filepath, 'a') as fp:
            fp.write(nowtime)
            fp.write('\n')
        time.sleep(2)

if __name__ == '__main__':
    get_time()