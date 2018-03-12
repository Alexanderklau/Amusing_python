# coding: utf-8
__author__ = 'lau.wenbo'
# 还是分为有阈值和无阈值状态

import os
import re
import psutil
import prettytable

def get_memory():
    """
        这里不需要调用shell命令，Python自带的功能可以去查询实时的内存占用,快，好用
        """
    ps_result = list()
    for proc in psutil.process_iter():
        ps_result.append(dict(name=proc.name(), pid=proc.pid, memory_percent=proc.memory_percent()))
    table = prettytable.PrettyTable()
    table.field_names = ["No.", "Name", "Pid", "Memory percent"]
    for i, item in enumerate(sorted(ps_result, key=lambda x: x['memory_percent'], reverse=True)):
        table.add_row([i + 1, item['name'], item['pid'], format(item['memory_percent'] / 100, '.2%')])
        if i >= 9:
            break
    return str(table)


def get_memory_have(threshold):
    """
    有阈值， 使用阈值的数值去判断.
    读取瞬时所有的cpu进程， 写入到tmp文件，根据阈值去判断，最后输出
    """
    os.popen('ps aux|head -1;ps aux|grep -v PID|sort -rn -k +3 > memory.tmp')
    with open('memory.tmp', 'r') as f:
        lines = f.readlines()
    # 将数据标准化，以dict格式输出
    dicts = {}
    for i in lines:
        # 用正则去规范化字符串
        lines_strs = re.sub(' +', ',', i)
        a = lines_strs.split(",")
        # 如果超过阈值，写入字典待用
        if float(a[3]) >= threshold:
            dicts[a[1]] = a[3]
    os.remove('memory.tmp')
    cpu_dict = dicts
    ps_result = list()
    try:
        for key, value in cpu_dict.items():
            p = psutil.Process(int(key))
            ps_result.append(dict(name=p.name(), pid=int(key), memory_percent=float(value)))
    except:
        pass
    # 排序，输出
    table = prettytable.PrettyTable()
    table.field_names = ["No.", "Name", "Pid", "Memory_percent"]
    for i, item in enumerate(sorted(ps_result, key=lambda x: x['memory_percent'], reverse=True)):
        table.add_row([i + 1, item['name'], item['pid'], format(str(item['memory_percent']) + "%")])
        if i >= 9:
            break
    return str(table)