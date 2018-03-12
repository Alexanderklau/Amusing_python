# coding: utf-8
__author__ = 'lau.wenbo'


from subprocess import check_output
from log import Log
import psutil
import prettytable
import os
import re
import json
import time


def get_process(name):
    dicts = {}
    try:
        pid_list = map(int,check_output(["pidof",name]).split())
        # print(pid_list)
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
    for i, item in enumerate(sorted(ps_result, key=lambda x: x['process_memory'], reverse=True)):
        table.add_row([i + 1, item['name'], item['pid'], format(str(item['process_memory']) + "%")])
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

if __name__ == "__main__":
    f = open("../setting/setting.json", "r")
    setting = json.load(f)
    process_name = setting["process"]
    check_time = setting["time"]
    log = Log("Process_message")
    while True:
        try:
            pid = get_process(process_name)
            for p in pid:
                time_remaining = check_time - time.time() % check_time
                log.info("\n进程的线程\n" + check_process_thread(p) + "\n进程占用内存\n" + check_process_memory(p))
                time.sleep(time_remaining)
        except Exception, e:
            log.error(e)
            break
