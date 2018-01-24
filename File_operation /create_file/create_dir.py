#coding: utf-8
__author__ = 'lau.wenbo'


def gen_file(path, size):
    # 首先以路径path新建一个文件，并设置模式为写
    file = open(path, 'w')
    # 根据文件大小，偏移文件读取位置
    file.seek(1024 * 1024 * 1024 * size)  # 以GB为单位
    file.write('\x00')
    file.close()


def create_file():
    for i in range(10):
        print(i)
        gen_file(('./%i.dat' %i),1)

create_file()
