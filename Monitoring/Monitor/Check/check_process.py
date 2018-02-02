# coding: utf-8
__author__ = 'lau.wenbo'


from subprocess import check_output
import psutil
import prettytable
import os
import re

# 根据进程名去拿到进程的pid
def get_process(name):
    dicts = {}
    try:
        pid_list = map(int,check_output(["pidof",name]).split())
        print(pid_list)
        for pid in pid_list:
            dicts[pid] = name
        return dicts
    except:
        print("没有这个进程！")

# 打印进程占用内存
def check_process_memory(pid):
    ps_result = list()
    p = psutil.Process(int(pid))
    ps_result.append(dict(name=p.name(), pid=int(pid), process_memory=p.memory_percent()))
    table = prettytable.PrettyTable()
    table.field_names = ["No.", "Name", "Pid", "Memory_percent"]
    for i, item in enumerate(sorted(ps_result, key=lambda x: x['memory_percent'], reverse=True)):
        table.add_row([i + 1, item['name'], item['pid'], format(str(item['memory_percent']) + "%")])
        if i >= 9:
            break
    return str(table)


# 打印进程的线程
def check_process_thread(pid):
    os.popen("ps -T -p {0} | head".format(pid) + " > thread.tmp")
    with open("thread.tmp", 'r') as f:
        lines = f.readlines()
        del lines[0]
    dicts = {}
    for i in lines:
        # 用正则去规范化字符串
        lines_strs = re.sub(' +', ',', i)
        a = lines_strs.split(",")
        dicts[a[2]] = a[1]
    os.remove('thread.tmp')
    ps_result = list()
    for key, value in dicts.items():
        p = psutil.Process(int(value))
        ps_result.append(dict(name=p.name(), pid=int(value), spid=int(key)))
        # 排序，输出
    table = prettytable.PrettyTable()
    table.field_names = ["No.", "Name", "Pid", "Spid"]
    for i, item in enumerate(ps_result):
        table.add_row([i + 1, item['name'], item['pid'], item['spid']])
        if i >= 9:
            break
    return str(table)

