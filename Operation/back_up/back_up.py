# coding: utf-8

__author__ = 'lau.wenbo'

"""
指定位置的配置文件备份脚本
"""

import commands
import difflib
import json
import os
import sys
import time
import infinity.common.inficore as infinity
import system.system_api as system_api
import etcd_backup



def execute(cmd):
    (status, output) = commands.getstatusoutput(cmd)
    return (status, output)


# 读配置文件
def read_config(config):
    with open(config, 'r') as f:
        temp = json.loads(f.read())
    return temp


# 打包压缩
def compress_file(node):
    (status, output) = execute("tar -czvf {node}.tar.gz back_up/".format(node=node))
    (status, output) = execute("cd bach_up/ && rm -rf back_up/")


# 解压文件
def uncompress_file(node):
    (status, output) = execute("tar -zxvf {node}.tar.gz".format(node=node))


# 拷贝文件
def copy_file(path, file):
    print("正在拷贝{file}".format(file=file))
    (status, output) = execute("cd back_up/{path} && \cp -avx --parents {file} ./".format(path = path, file=file))
    if status != 0:
        print("拷贝失败{file}".format(file=file))
        time.sleep(1)
# 创建复制文件夹
def mkdir_file():
    (status, output) = execute("mkdir back_up/")


# 创建项目备份文件夹
def mkdir_item_file(name):
    (status, output) = execute("cd back_up && mkdir {name}/".format(name=name))


# 备份网卡信息
def back_up_network():
    print("正在拷贝网卡信息")
    (status, output) = execute("cd back_up/ && rm -rf network && mkdir network && cd network && \cp -avx "
                               "/etc/sysconfig/network-scripts ./")
    if status != 0:
        print("拷贝网卡信息失败.... .")
        time.sleep(1)


# 备份磁盘信息
def back_up_disk(ipaddr):
    print("正在拷贝磁盘信息")
    (status, output) = execute("cd back_up/ && touch disk.file")
    f = open("./back_up/disk.file", "w+")
    ret = system_api.list_disk(ipaddr)
    if ret[0] == 0:
        lists = ret[1]["disklist"]
        for i in lists:
            f.write(str(i))
    f.close()

def back_up_ssh():
    print("备份SSH信息")
    (status, output) = execute("cd back_up/ && rm -rf ssh && mkdir ssh/ && cd ssh && \cp -avx /root/.ssh ./ ")
    print("备份成功")


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
    print("正在覆盖{file}".format(file=file))
    (status, output) = execute("cd back_up/{path} && \cp -avx {file}/*  /{file}/".format(path=path, file=file))
    if status != 0:
        print("覆盖失败{file}".format(file=file))
        time.sleep(1)


def cover_ssh():
    print("覆盖SSH")
    (status, output) = execute("cd back_up/ssh/ && \cp -r /root/.ssh/* /root")
    print("覆盖成功")


def cover_up_file(config):
    message = read_config(config)
    for i in message:
            path = "./back_up/{file_path}/".format(file_path = i)
            dirs = os.listdir(path)
            for files in dirs:
                cover_file(i, files)


def systemctl_restart(config):
    services = read_config(config)
    for i in services:
        print("重启{service}系列服务开始".format(service=i))
        for s in services[i]:
            (status, output) = execute(s)
            if status == 0:
                print("重启服务成功".format(service=s))
            else:
                print("重启服务失败".format(service=s))


def ceph_setting(node):
    ceph_status = {}
    (status, output) = execute("cd back_up/ && touch ceph.file")
    f = open("./back_up/ceph.file", "w+")
    ret = execute("ETCDCTL_API=\"3\" /usr/bin/etcdctl get \"infi-cluster/{node}\"".format(node=node))
    try:
        message = eval(ret[1].split("\n")[1])
    except:
        message = {}
    ceph_list = ["mgr_node", "mds_node", "mon_node"]
    for i in ceph_list:
        try:
            statuss = message[i]
        except:
            continue
        ceph_status[i] = statuss
    f.write(str(ceph_status))
    f.close()

def etcd_back_up():
    print("开始备份ETCD数据............")
    (status, output) = execute("cd back_up/ && mkdir etcd")
    active = etcd_backup.dumpAllData()

def etcd_cover_up():
    print("开始恢复ETCD数据.............")
    active = etcd_backup.putAllData()

def ceph_back_up(node):
    f = open("./back_up/ceph.file", "r")
    message = f.readlines()
    ceph_lists = {"mgr_node": "mgr", "mds_node": "mds", "mon_node": "mon"}
    for i in ceph_lists.keys():
        try:
            ceph_status = eval(message[0])[i]
        except:
            continue
        if ceph_status == 1:
            (status, output) = execute("cd /var/datatom/infinity-cluster/ && ceph-deploy {ceph} create {node}".format(ceph=ceph_lists[i], node=node))
            if status != 0:
                print "{ceph}服务创建错误".format(ceph=i)
                time.sleep(3)
    (status, output) = execute("ceph-disk activate-all")
    if status!= 0:
        print("ceph-disk activate-all error!!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please enter the correct option！"
    else:
        if sys.argv[1] == "back_up":
                config = "setting.json"
                node = sys.argv[2]
                ipaddr = sys.argv[3]
                back_up_file(config)
                back_up_network()
                back_up_disk(ipaddr)
                back_up_ssh()
                etcd_back_up()
                ceph_setting(node)
                compress_file(node)
        elif sys.argv[1] == "cover_up":
                node = sys.argv[2]
                config = "setting.json"
                service_config = "service.json"
                cover_ssh()
                uncompress_file(node)
                cover_up_file(config)
                systemctl_restart(service_config)
        elif sys.argv[1] == "ceph_back_up":
                node = sys.argv[2]
                ceph_back_up(node)
        elif sys.argv[1] == "etcd_cover_up":
                etcd_cover_up()
        else:
            print "Illegal operation"



