# coding: utf-8
__author__ = 'lau.wenbo'

import os
import time
import re
import psutil
import prettytable
import logging

logging.basicConfig(filename='/var/log/monitoring.log', level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)


# logging.getLogger('').addHandler(console)


def get_cpu():
    """
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
    return dicts


def check_cpu():
    # 添加列表
    cpu_dict = get_cpu()
    ps_result = list()
    for key, value in cpu_dict.items():
        p = psutil.Process(int(key))
        ps_result.append({'name': p.name(), 'pid': int(key), 'cpu_percent': float(value)})
    # 排序，输出
    table = prettytable.PrettyTable()
    table.field_names = ["No.", "Name", "Pid", "Cpu_percent"]
    for i, item in enumerate(sorted(ps_result, key=lambda x: x['cpu_percent'], reverse=True)):
        table.add_row([i + 1, item['name'], item['pid'], format(str(item['cpu_percent']) + "%")])
        if i >= 9:
            break
    return str(table)


def check_memory():
    """
    这里不需要调用shell命令，Python自带的功能可以去查询实时的内存占用,快，好用
    """
    ps_result = list()
    for proc in psutil.process_iter():
        ps_result.append({'name': proc.name(), 'pid': proc.pid, 'memory_percent': proc.memory_percent()})
    table = prettytable.PrettyTable()
    table.field_names = ["No.", "Name", "Pid", "Memory percent"]
    for i, item in enumerate(sorted(ps_result, key=lambda x: x['memory_percent'], reverse=True)):
        table.add_row([i + 1, item['name'], item['pid'], format(item['memory_percent'] / 100, '.2%')])
        if i >= 9:
            break
    return str(table)


# 主函数
def run(interval):
    while True:
        try:
            # 睡眠
            time_remaining = interval - time.time() % interval
            logging.info("\n" + "CPU" + "\n" + check_cpu())
            logging.info("\n" + "Memory" + "\n" + check_memory())
            time.sleep(time_remaining)
        except Exception as e:
            print (e)


if __name__ == "__main__":
    interval = 60
    run(interval)
