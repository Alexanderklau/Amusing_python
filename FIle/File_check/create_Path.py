#coding: utf-8
#找到infinsty下所有的目录，写入到某文件和log中，然后再依次去读。
import os, time, random
import logging
import commands
from datetime import datetime
import multiprocessing

Path = '/home/lau'

filename = "Directory.txt"
logging.basicConfig(filename='Directory.log', filemode="w", level=logging.DEBUG)


def create_dir():
    dir = []
    directory = os.path.expanduser(Path)
    for f in os.listdir(directory):
        # logging.info("%s下的子文件夹%s" % (Path, f))
        if os.path.isdir(os.path.join(directory, f)):
            ff = Path + "/" + f
            dir.append(ff)
    return dir

print(create_dir())


def write():
    Path_list = create_dir()
    for path in Path_list:
        filename = [os.path.join(root, fn) for root, dirs, files in os.walk(path) for fn in files]


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
    else:
        pass
        # logging.warning("%s:%s:%s" % (datetime.now(), filenames, output))

if __name__=='__main__':
    t1 = time.time()
    manager = multiprocessing.Manager()
    Path_list = create_dir()
    for path in Path_list:
        logging.info("开始扫描文件夹%s"%path)
        filename = [os.path.join(root, fn) for root, dirs, files in os.walk(path) for fn in files]
        p = multiprocessing.Pool(3)
        p.map(read, filename)
        p.close()
        p.join()
        t2 = time.time()
        # print '时间 %d' %(int(t2-t1))
        logging.info("文件夹%s数据都已经读完"%path)
        # print '所有数据都已经读完'