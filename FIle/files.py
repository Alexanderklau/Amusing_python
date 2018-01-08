# -*- coding:utf8 -*-
import os, os.path
import commands
import logging

Path = r"/home/lau/下载/test/"


#函数递归遍历目录
def visitDir(arg, dirname, names):
    print names
    for filepath in names:     
        filename = os.path.join(dirname, filepath)
        filenames = filename_processing(filename)
        read_file(filenames)

#文件名的处理，文件名内含有空格，括号，书名号等，不能直接调用dd，在对文件名处理后进行调用
def filename_processing(filename):
    filename = filename.replace(" ", "\\ ").replace("(", "\\(").\
    replace(")", "\\)").replace("<", "\\<").replace(">", "\\>")
    return filename

def read_file(filename):
    file, output = commands.getstatusoutput('dd if=' + filename)
    if file == 0:
        
        


if __name__ == "__main__":
    os.path.walk(Path, visitDir, ())
