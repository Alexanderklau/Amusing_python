# coding: utf-8
__author__ = 'lau.wenbo'


import sys
import os
import time
import re
import psutil
import prettytable
import logging
import getopt
import commands


logging.basicConfig(filename='monitoring.log', level=logging.DEBUG,
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
    os.remove('CPU.tmp')
    return dicts


def check_cpu():
    # 添加列表
    cpu_dict = get_cpu()
    ps_result = list()
    for key, value in cpu_dict.items():
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


def check_memory():
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


# 主函数
def run_check(interval):
    while True:
        try:
            # 睡眠
            time_remaining = interval - time.time() % interval
            logging.info("\n" + "CPU" + "\n" + check_cpu())
            logging.info("\n" + "Memory" + "\n" + check_memory())
            time.sleep(time_remaining)
        except Exception, e:
            print e


# # 获取参数
# def get_parameter(cpu, memeory):
#


# 获取所有进程的CPU，内存
def get_cpu_memory():
    message = commands.getoutput("ps aux > check.tmp")
    dicts_cpu = {}
    dicts_memory = {}
    for i in message:
        # 用正则去规范化字符串
        lines_strs = re.sub(' +', ',', i)
        a = lines_strs.split(",")
        # Pid为key， CPU占比为value
        dicts_cpu[a[1]] = a[2]
        dicts_memory[a[1]] = a[3]
    os.remove('check.tmp')





if __name__ == "__main__":
    options, args = getopt.getopt(sys.argv[1:], "hc:m:s:qk:", ["help", "cpu=", "memory=", "start=", "quit", "kid="])
    settings = {}
    for name, value in options:
        if name in ("-h", "--help"):
            print "=" * 70
            print "命令功能：监控CPU，内存占用"
            print "1. 设定CPU阀值进行监控，不加会默认前十  -c, --cpu 参数"
            print "2. 设定内存阀值进行监控，不加会默认前十  -m, --memeory 参数"
            print "3. 开始操作，设定监控时间，默认前十 -s, --start 参数"
            print "4. 打印进程的线程  -k --kid"
            print "5. 删除配置并停止操作 -q --quit"
            print "=" * 70
        elif name in ("-c", "--cpu"):
            print "设定CPU内存阀值{0}".format(value)
            settings["cpu"] = value
        elif name in ("-m", "--memory"):
            print "设定memory内存阀值{0}".format(value)
            settings["memory"] = value
        elif name in ("-s", "--start"):
            print "设定为 {0}秒 检查一次CPU和内存".format(value)
            run_check(int(value))
        elif name in ("-k", "--kid"):
            print "读取配置，打印线程......."
        elif name in ("-q", "--quit"):
            print settings
            print "退出所有在进行中的监控，并且清空配置"
            print(sys.exit())
