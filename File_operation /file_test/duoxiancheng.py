#! -*-coding: utf-8 -*-
import os
path = "/home/lau/下载/"                   # 文件夹目录

def read_file(file_name):     #  读取文件内容并返回
    print file_name
    # str = os.system('dd if=' + file_name )

    return str

def write_file(paths):
    flag = True                               # 定义一个判断标示
    data = [paths]                            #　置一个存放文件夹的list, 这里将要读取的文件夹存入
    while flag:
        for i in xrange(len(data)):           # 遍历目录list
            file_path = data.pop()            # 取出一个文件目录
            files = os.listdir(file_path)     # 读出目录中的下一级所有文件名和文件夹
            for file in files:                # 遍历文件夹
                # print file_path+file
                if not os.path.isdir(file_path+file):   #判断是否是文件夹，不是文件夹才打开
                    str = read_file(file_path+file)
                else:
                    if "." not in file:
                        data.append(file_path + file + "/")
        if len(data) <= 0:
            flag = False
write_file(path)