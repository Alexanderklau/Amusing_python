#coding: utf-8
import os, time, random
import logging
import commands
from datetime import datetime
import multiprocessing


Path = r"/home/lau"


# 写数据进程执行的代码:
# def write():
#  # lock.acquire()
#  return [os.path.join(root,fn) for root,dirs,files in os.walk(Path) for fn in files]

     # 写入队列
     # q.put(filename,block=True,timeout=10)
 # lock.release()

# 读数据进程执行的代码:
def read(filename):
            print 'Get %s from queue.' % filename
            filenames = filename.replace(" ", "\\ ").replace("(", "\\(").replace(")", "\\)"). \
                replace("<", "\\<").replace(">", "\\>")
            logging.basicConfig(filename='file.log', filemode="w", level=logging.DEBUG)
            file, output = commands.getstatusoutput('dd if=' + filenames)
                # 如果返回值=0，说明文件可以正常读取,反之则否
            if file == 0:
                pass
                #    #正确的文件可以不写入日志，可调整。
                #    # logging.info('%s This is helath file!' % (filename))
            else:
                logging.warning("%s:%s:%s" % (datetime.now(), filenames, output))

if __name__=='__main__':
    t1 = time.time()
    manager = multiprocessing.Manager()
    filename = [os.path.join(root,fn) for root,dirs,files in os.walk(Path) for fn in files]
    p = multiprocessing.Pool(3)
    p.map(read, filename)
    p.close()
    p.join()
    t2 = time.time()
    print '时间 %d' %(int(t2-t1))
    print '所有数据都已经读完'