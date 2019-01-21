# coding: utf-8

__author__ = "lau.wenbo"

import time

def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
        continue
        yield line


if __name__ == '__main__':
    logfile = open('access-log', 'r')
    loglines = follow(logfile)
    for line in loglines:
        print line
