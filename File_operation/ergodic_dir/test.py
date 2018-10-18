# coding: utf-8

__author__ = 'lau.wenbo'

import os, logging, pdb


def search(s):
    rootdir = '../'  # 指明被遍历的文件夹

    # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:  # 输出文件信息
            # print "filename is:" + filename
            if filename.find(s) != -1:
                path = os.path.abspath(os.path.join(parent, filename))  # 输出文件路径信息
                comand = 'cp -r {path} /root/one'.format(path=path)
                os.system(comand)


if __name__ == '__main__':
    a = [
        "bind - 9.9.4 - 51.el7_4.2.x86_64.rpm",
        "bind - libs - 9.9.4 - 51.el7_4.2.x86_64.rpm",
        "bind - license - 9.9.4 - 51.el7_4.2.noarch.rpm",
        "bind - utils - 9.9.4 - 51.el7_4.2.x86_64.rpm",
        "python2 - psutil - 5.4.3 - 4.el7.x86_64.rpm",
        "python - crypto - 2.6.1 - 1.el7.x86_64.rpm",
        "python - ecdsa - 0.11 - 3.el7.centos.noarch.rpm",
        "python-netifaces - 0.10.4 - 3.el7.x86_64.rpm",
        "python-paramiko - 1.15.1 - 1.el7.noarch.rpm",
        "parted - 3.1 - 28.el7.x86_64.rpm",
    ]
    for i in a:
        search(i)