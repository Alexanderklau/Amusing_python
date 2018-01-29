#coding: utf-8
__author__ = 'lau.wenbo'

import time

#生成测试文件1000个，大小为100M，可以手动更改大小和数量d

def creatfilesize(n,name):
    # local_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
    #写入测试文件
    file_name = "/infinity/%s.txt" % name
    bigFile= open(file_name, 'w')
    bigFile.seek(1024*1024*n)
    bigFile.write('test')
    bigFile.close()
    print "ALL down !"

if __name__ == '__main__':
    for i in range(1000):
        #生成文件1000个，大小为100m/每个
        creatfilesize(100,i)