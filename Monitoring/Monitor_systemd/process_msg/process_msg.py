# coding: utf-8
__author__ = 'lau.wenbo'


from subprocess import check_output
from log import Log
import psutil
import prettytable
import os
import re
import json
import commands


def get_process_message(name):
    process_list = []
    try:
        commands.getoutput(("top -b -n 1 |grep {0} > process.tmp").format(name))
        with open("process.tmp", "r") as f:
            lines = f.readlines()

        for i in lines:
            # 用正则去规范化字符串
            lines_strs = re.sub(' +', ',', i)
            a = lines_strs.split(",")
            process_list.append(dict(name=a[11].replace("\n", ""),pid=a[0],process_cpu=a[8],process_memory=a[9]))
    except:
        pass
    os.remove('process.tmp')
    if len(process_list) == 0:
        return "没有那个进程"
    else:
        table = prettytable.PrettyTable()
        table.field_names = ["No.", "Name", "Pid", "Process_memory","Process_cpu"]
        for i, item in enumerate(sorted(process_list, key=lambda x: x['process_memory'], reverse=True)):
            table.add_row([i + 1, item['name'], item['pid'], item['process_memory'] + "%", item['process_cpu'] + "%"])
        return str(table)


# 打印进程的线程
def check_process_thread(name):
    thread_dicts = {}
    thread_list = []
    commands.getoutput(("top -b -n 1 |grep {0} > pid.tmp").format(name))
    with open("pid.tmp", "r") as f:
        lines = f.readlines()
    for i in lines:
        # 用正则去规范化字符串
        lines_strs = re.sub(' +', ',', i)
        a = lines_strs.split(",")
        pid = a[0]
        os.popen("ps -T -p {0} | head".format(int(pid)) + " > thread.tmp")
        os.remove('pid.tmp')
        with open("thread.tmp", 'r') as f:
            lines = f.readlines()
            del lines[0]
        for i in lines:
            # 用正则去规范化字符串
            lines_strs = re.sub(' +', ',', i)
            a = lines_strs.split(",")
            thread_dicts[a[4].replace('\n', "")] = a[1]
            thread_list.append(dict(name=a[4].replace('\n', ""),spid=a[1],pid=a[0]))
        os.remove('thread.tmp')
        if len(thread_list) == 0:
            return "没有子进程"
        table = prettytable.PrettyTable()
        table.field_names = ["No.", "Name", "Pid", "Spid"]
        for i, item in enumerate(thread_list):
            table.add_row([i + 1, item['name'], item['pid'], item['spid']])
            if i >= 9:
                break
        return str(table)

if __name__ == "__main__":
    # log = Log("定点检测")
    f = open("../setting/setting.json", "r")
    setting = json.load(f)
    process_name = setting["process"]
    check_time = setting["process_time"]
    print(check_process_thread(process_name))
    # print get_process_message(process_name)
    # while True:
    #     try:
    #         pid = get_process(process_name)
    #         time_remaining = check_time - time.time() % check_time
    #         for key, value in pid.items():
    #             log.info("\n进程占用内存\n" + check_process_memory(key))
    #         time.sleep(time_remaining)
    #     except Exception, e:
    #         log.error(e)
