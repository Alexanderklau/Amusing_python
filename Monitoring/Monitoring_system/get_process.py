# coding: utf-8
__author__ = 'lau.wenbo'

import os
import re
import psutil
import prettytable


def check_cpu():
    # 将CPU占用率前十的进程的详细信息写入CPU.tmp文件
    os.popen('ps aux|head -1;ps aux|grep -v PID|sort -rn -k +3|head > CPU.tmp')
    # 读取TMP数据，将其规范，格式化
    with open('CPU.tmp', 'r') as f:
        lines = f.readlines()
    # 将数据标准化，以dict格式输出
    dicts = {}
    for i in lines:
        a = re.sub(' +', ',', i)
        a = a.split(",")
        dicts[a[1]] = a[2]
    # 添加列表
    ps_result = list()
    for key, value in dicts.items():
        p = psutil.Process(int(key))
        ps_result.append({'name': p.name(), 'pid': int(key), 'cpu_percent': float(value)})
    # 排序，输出
    table = prettytable.PrettyTable()
    table.field_names = ["No.", "Name", "Pid", "Cpu_percent"]
    for i, item in enumerate(sorted(ps_result, key=lambda x: x['cpu_percent'], reverse=True)):
        table.add_row([i + 1, item['name'], item['pid'], format(str(item['cpu_percent']) + "%")])
        if i >= 9:
            break
    return table


def check_memory():
    ps_result = list()
    for proc in psutil.process_iter():
        ps_result.append({'name': proc.name(), 'pid': proc.pid, 'memory_percent': proc.memory_percent()})
    print(ps_result)
    table = prettytable.PrettyTable()
    table.field_names = ["No.", "Name", "Pid", "Memory percent"]
    for i, item in enumerate(sorted(ps_result, key=lambda x: x['memory_percent'], reverse=True)):
        table.add_row([i + 1, item['name'], item['pid'], format(item['memory_percent'] / 100, '.2%')])
        if i >= 9:
            break
    return table

# f = file("test.txt", "a+")
# f.write(str(check_cpu()))
# f.close()
