#coding: utf-8
__author__ = 'lau.wenbo'

import time

def creatfilesize(n,name):
    # local_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
    #写入测试文件
    file_name = "./test/%s.txt" % name
    bigFile= open(file_name, 'w')
    bigFile.seek(1024*1024*n)
    bigFile.write('test')
    bigFile.close()
    print "ALL down !"

if __name__ == '__main__':
    for i in range(1000):
        creatfilesize(10,i)
