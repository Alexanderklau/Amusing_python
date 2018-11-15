# coding: utf-8
__author__ = 'lau.wenbo'

import httplib
import time
import os


def get_webservertime(host):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("GET", "/")
        r = conn.getresponse()
        # r.getheaders() #获取所有的http头
        ts = r.getheader('date')  # 获取http头date部分
        print '============================'
        print ts
        print '============================'
        # 将GMT时间转换成北京时间
        ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
        # print(ltime)
        ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
        # print(ttime)
        dat = "date %u-%02u-%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)
        tm = "time %02u:%02u:%02u" % (ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
        currenttime = "%u-%02u-%02u %02u:%02u:%02u" % (
        ttime.tm_year, ttime.tm_mon, ttime.tm_mday, ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
        print currenttime
        print (dat, tm)
        os.system(dat)
        os.system(tm)
    except:
        return False


get_webservertime('www.baidu.com')