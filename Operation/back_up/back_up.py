# coding: utf-8

__author__ = 'lau.wenbo'

"""
指定位置的配置文件备份脚本
"""

import commands


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
    pass


# 解压文件
def uncompress_file():
    pass


# 拷贝文件
def copy_file(file):
    z = execute("cd back_up/ && cp -avx {file} ./".format(file=file))


# 创建复制文件夹
def mkdir_file():
    z = execute("mkdir back_up/".format(file=file))


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


if __name__ == "__main__":
    mkdir_file()
