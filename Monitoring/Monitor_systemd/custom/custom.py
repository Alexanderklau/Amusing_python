# coding: utf-8
__author__ = 'lau.wenbo'


"""
这里考虑了阈值情况，如果启用的话，如果超过阈值，就写入到日志中，
如果没有超过阈值，那么就做持续监控，直到超过为止
"""

import os
import re
import psutil
import prettytable
import json
import time
from log import Log


def process_have(cpu, memory):
    os.popen('ps aux|head -1;ps aux|grep -v PID|sort -rn -k +3 > total.tmp')
    with open("total.tmp", "r") as f:
        lines = f.readlines()

    dicts = {}
    for i in lines:
        # 用正则去规范化字符串
        lines_strs = re.sub(' +', ',', i)
        a = lines_strs.split(",")
        # 如果超过阈值，写入字典待用
        if float(a[2]) >= cpu and float(a[3]) >= memory:
            dicts[a[1]] = a[2]
    os.remove('total.tmp')
    cpu_dicts = dicts
    ps_result = list()
    for key, value in cpu_dicts.items():
        try:
            p = psutil.Process(int(key))
            ps_result.append(dict(name=p.name(), pid=int(key), cpu_percent=value,
                                  memory_percent=p.memory_percent()))
        except:
            pass
    # 排序，输出
    table = prettytable.PrettyTable()
    table.field_names = ["No.", "Name", "Pid", "Cpu_percent", "Memory_percent"]
    for i, item in enumerate(sorted(ps_result, key=lambda x: x['cpu_percent'], reverse=True)):
        table.add_row(
            [i + 1, item['name'], item['pid'], format(str(item['cpu_percent']) + "%"),
             format(item['memory_percent'] / 100, '.2%')])
        if i >= 9:
            break
    return str(table)

if __name__ == "__main__":
    log = Log("自定义检测")
    f = open("../setting/setting.json", "r")
    setting = json.load(f)
    cpu_max = float(setting["CPU_max"])
    memeory_max = float(setting["Memory_max"])
    check_time = setting["time"]
    while True:
        try:
            # 睡眠
            time_remaining = check_time - time.time() % check_time
            log.info("\nCPU占用详情\n" + process_have(cpu_max,memeory_max))
            time.sleep(time_remaining)
        except Exception, e:
            print e
