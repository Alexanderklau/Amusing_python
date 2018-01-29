#!/usr/bin/python
#coding=utf-8
# -*- coding:utf-8 -*-
from multiprocessing import Process,Pool
import os,time
import commands

Path = r"/home/lau"
def run_proc():        ##定义一个函数用于进程调用
  for value in [os.path.join(root, fn) for root, dirs, files in os.walk(Path) for fn in files]:
    filename = value.replace(" ", "\\ ").replace("(", "\\(").replace(")", "\\)"). \
      replace("<", "\\<").replace(">", "\\>")
    file, output = commands.getstatusoutput('dd if=' + filename)
    if file == 0:
      pass
      #    #正确的文件可以不写入日志，可调整。
      #    # logging.info('%s This is helath file!' % (filename))
    else:
      pass



#执行一次该函数共需1秒的时间
if __name__ =='__main__': #执行主进程
    print 'Run the main process (%s).' % (os.getpid())
    mainStart = time.time() #记录主进程开始的时间
    p = Pool()           #开辟进程池                                #开辟5个进程
    for i in range(6):
      p.apply_async(run_proc)#每个进程都调用run_proc函数，
    print 'Waiting for all subprocesses done ...'
    p.close() #关闭进程池
    p.join()  #等待开辟的所有进程执行完后，主进程才继续往下执行
    print 'All subprocesses done'
    mainEnd = time.time()  #记录主进程结束时间
    print 'All process ran %0.2f seconds.' % (mainEnd-mainStart)  #主进程执行时间