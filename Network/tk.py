# coding: utf-8
__author__ = 'lau.wenbo'

import time

# 打开文件
def read_file():
    try:
        fo = open("/media/lau/datas/home/lau/我的资源/炊事班的故事1/01.flv", "r")
        for line in fo.readlines():  # 依次读取每行
            lines = line.strip()  # 去掉每行头尾空白
            print(lines)
            fo.close()
            return 0
    # 关闭文件
    except:
        return -1



read_file()