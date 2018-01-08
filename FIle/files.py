# -*- coding:utf8 -*-
import os, os.path
import commands
import logging

Path = r"/"


# #日志设置
# def file_log():
#     logging.basicConfig(level=logging.DEBUG,
#                         format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                         datefmt='%a, %d %b %Y %H:%M:%S',
#                         filename='myapp.log',
#                         filemode='w')

#函数递归遍历目录
def visitDir(arg, dirname, names):
    for filepath in names:     
        filename = os.path.join(dirname, filepath)
        filenames = filename_processing(filename)
        read_file(filenames)


#文件名的处理，文件名内含有空格，括号，书名号等，不能直接调用dd，在对文件名处理后进行调用
def filename_processing(filename):
    filename = filename.replace(" ", "\\ ").replace("(", "\\(").\
    replace(")", "\\)").replace("<", "\\<").replace(">", "\\>")
    return filename

#读文件
def read_file(filename):
    if os.path.isdir(filename):
        print "It is a dictory!!"
    elif os.path.isfile(filename):
        file, output = commands.getstatusoutput('dd if=' + filename)
        if file == 0:
            print 'This is helath file!'
        else:
            logging.warning("%s:%s" %(filename,output))
    else:
        print "it's a special file (socket, FIFO, device file)"


if __name__ == "__main__":
    os.path.walk(Path, visitDir, ())
