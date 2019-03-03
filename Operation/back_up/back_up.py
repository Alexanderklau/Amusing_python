# coding: utf-8

__author__ = 'lau.wenbo'

"""
指定位置的配置文件备份脚本
"""

import commands
import difflib


def execute(cmd):
    (status, output) = commands.getstatusoutput(cmd)
    return (status, output)


# 读配置文件
def read_config(config):
    result = []
    with open(config, 'r') as f:
        for line in f:
            result.append(line.strip('\n'))

    return result


# 打包压缩
def compress_file():
    (status, output) = execute("tar -czvf back_up.tar.gz back_up/")


# 解压文件
def uncompress_file():
    (status, output) = execute("tar -zxvf back_up.tar.gz")


# 拷贝文件
def copy_file(file):
    (status, output) = execute("cd back_up/ && cp -avx {file} ./".format(file=file))


# 创建复制文件夹
def mkdir_file():
    (status, output) = execute("mkdir back_up/".format(file=file))


# 覆盖文件并且备份
def cover_file():
    pass


# 读取文件夹下所有文件
def get_file():
    pass


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




if __name__ == "__main__":
    check_file("./file.config", "2.config")
