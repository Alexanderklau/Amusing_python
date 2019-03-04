# coding: utf-8

__author__ = 'lau.wenbo'

"""
指定位置的配置文件备份脚本
"""

import commands
import difflib
import json
import os


def execute(cmd):
    (status, output) = commands.getstatusoutput(cmd)
    return (status, output)


# 读配置文件
def read_config(config):
    with open(config, 'r') as f:
        temp = json.loads(f.read())
    return temp


# 打包压缩
def compress_file():
    (status, output) = execute("tar -czvf back_up.tar.gz back_up/")
    (status, output) = execute("cd bach_up/ && rm -rf back_up/")


# 解压文件
def uncompress_file():
    (status, output) = execute("tar -zxvf back_up.tar.gz")


# 拷贝文件
def copy_file(path, file):
    (status, output) = execute("cd back_up/{path} && \cp -avx --parents {file} ./".format(path = path, file=file))


# 创建复制文件夹
def mkdir_file():
    (status, output) = execute("mkdir back_up/")


# 创建项目备份文件夹
def mkdir_item_file(name):
    (status, output) = execute("cd back_up && mkdir {name}/".format(name=name))


# 备份网卡信息
def back_up_network():
    pass


# 备份磁盘信息
def back_up_disk():
    pass


# 比对文件差异
def diff_file(filenames):
    fileHandle = open(filenames, 'rb')
    text = fileHandle.read().splitlines()
    fileHandle.close()
    return text


def check_file(file1, file2):
    text1_lines = diff_file(file1)
    text2_lines = diff_file(file2)
    d = difflib.Differ()
    diff = difflib.unified_diff(text1_lines, text2_lines)
    print "\n".join(diff)


def back_up_file(config):
    message = read_config(config)
    # 创建备份文件夹
    mkdir_file()
    # 遍历目录
    for i in message:
        # 拷贝
        mkdir_item_file(i)
        # 拿到目录详细名称
        for x in message[i]:
            copy_file(i, x)


# 覆盖文件并且备份
def cover_file(path, file):
    (status, output) = execute("cd back_up/{path} && \cp -avx {file} /{file}/*".format(path=path, file=file))


def cover_up_file(config):
    message = read_config(config)
    for i in message:
            path = "./back_up/{file_path}/".format(file_path = i)
            dirs = os.listdir(path)
            for files in dirs:
                cover_file(i, files)



if __name__ == "__main__":
    pass

