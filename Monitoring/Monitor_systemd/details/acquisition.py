# coding: utf-8
__author__ = 'lau.wenbo'


import os
import re
import psutil
import prettytable
import time
from log import Log



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
        try:
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


def get_memory_none():
    """
        这里不需要调用shell命令，Python自带的功能可以去查询实时的内存占用,快，好用
        """
    ps_result = list()
    for proc in psutil.process_iter():
        ps_result.append(dict(name=proc.name(), pid=proc.pid, memory_percent=proc.memory_percent(), memory_virt=proc.memory_info().vms,memory_rss=proc.memory_info().rss))
    table = prettytable.PrettyTable()
    table.field_names = ["No.", "Name", "Pid", "Memory percent", "Memory virt", "Memory rss"]
    for i, item in enumerate(sorted(ps_result, key=lambda x: x['memory_percent'], reverse=True)):
        table.add_row([i + 1, item['name'], item['pid'], format(item['memory_percent'] / 100, '.2%'), str(item['memory_virt'] / 1048576) + "M", str(item['memory_rss'] / 1048576) + "M"])
        if i >= 9:
            break
    return str(table)


if __name__ == "__main__":
    print get_memory_none()
    # log = Log("get_cpu_memory")
    # while True:
    #     try:
    #         time_remaining = check_time - time.time() % check_time
    #         log.info("\nCPU占用详情\n" + get_cpu_none() + "\n内存占用详情\n" + get_memory_none())
    #         time.sleep(time_remaining)
    #     except Exception, e:
    #         log.error(e)
    check_time = 60


