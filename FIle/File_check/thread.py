#coding: utf-8
import commands
import os
from multiprocessing.dummy import Pool as ThreadPool

Path = "/home/lau"

def run_proc(value):        ##定义一个函数用于进程调用
    print("get %s" %value)
    filename = value.replace(" ", "\\ ").replace("(", "\\(").replace(")", "\\)"). \
      replace("<", "\\<").replace(">", "\\>")
    file, output = commands.getstatusoutput('dd if=' + filename)
    if file == 0:
      pass
      #    #正确的文件可以不写入日志，可调整。
      #    # logging.info('%s This is helath file!' % (filename))
    else:
      pass


pool = ThreadPool()
filename = [os.path.join(root, fn) for root, dirs, files in os.walk(Path) for fn in files]
results = pool.map(run_proc,filename)
print results
pool.close()
pool.join()

print 'main ended'