# coding: utf-8
__author__ = 'lau.wenbo'
# 两种情况，一种有阀值，一种没有，所以分为两种方式去检查CPU

import os
import re
import psutil
import prettytable



def get_cpu_none():
    """
    无阈值，默认情况，读取CPU占比前十的进程
    将CPU占用率前十的进程的详细信息写入CPU.tmp文件
    这里需要写入临时文件，因为测试CPU占用的算法需要加上时限，
    Python去计算非常慢，所以用shell计算完直接调用
    """
    os.popen('ps aux|head -1;ps aux|grep -v PID|sort -rn -k +3|head > CPU.tmp')
    # 读取TMP数据，将其规范，格式化
    with open('CPU.tmp', 'r') as f:
        lines = f.readlines()
    # 将数据标准化，以dict格式输出
    dicts = {}
    for i in lines:
        # 用正则去规范化字符串
        lines_strs = re.sub(' +', ',', i)
        a = lines_strs.split(",")
        # Pid为key， CPU占比为value
        dicts[a[1]] = a[2]
    os.remove('CPU.tmp')
    cpu_dicts = dicts
    ps_result = list()
    for key, value in cpu_dicts.items():
        p = psutil.Process(int(key))
        ps_result.append(dict(name=p.name(), pid=int(key), cpu_percent=float(value)))
    # 排序，输出
    table = prettytable.PrettyTable()
    table.field_names = ["No.", "Name", "Pid", "Cpu_percent"]
    for i, item in enumerate(sorted(ps_result, key=lambda x: x['cpu_percent'], reverse=True)):
        table.add_row([i + 1, item['name'], item['pid'], format(str(item['cpu_percent']) + "%")])
        if i >= 9:
            break
    return str(table)

def get_cpu_have(threshold):
    """
    有阈值， 使用阈值的数值去判断.
    读取瞬时所有的cpu进程， 写入到tmp文件，根据阈值去判断，最后输出
    """
    os.popen('ps aux|head -1;ps aux|grep -v PID|sort -rn -k +3 > CPU2.tmp')
    with open('CPU2.tmp', 'r') as f:
        lines = f.readlines()
    # 将数据标准化，以dict格式输出
    dicts = {}
    for i in lines:
        # 用正则去规范化字符串
        lines_strs = re.sub(' +', ',', i)
        a = lines_strs.split(",")
        # 如果超过阈值，写入字典待用
        if float(a[2]) >= threshold:
            dicts[a[1]] = a[2]
    os.remove('CPU2.tmp')
    cpu_dicts = dicts
    ps_result = list()
    try:
        for key, value in cpu_dicts.items():
            p = psutil.Process(int(key))
            ps_result.append(dict(name=p.name(), pid=int(key), cpu_percent=float(value)))
    except:
        pass
    # 排序，输出
    table = prettytable.PrettyTable()
    table.field_names = ["No.", "Name", "Pid", "Cpu_percent"]
    for i, item in enumerate(sorted(ps_result, key=lambda x: x['cpu_percent'], reverse=True)):
        table.add_row([i + 1, item['name'], item['pid'], format(str(item['cpu_percent']) + "%")])
        if i >= 9:
            break
    return str(table)
