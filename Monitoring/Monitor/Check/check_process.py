# coding: utf-8
__author__ = 'lau.wenbo'


from subprocess import check_output
import prettytable

# 根据输入去拿到pid
def get_process(name):
    dicts = {}
    pid_list = map(int,check_output(["pidof",name]).split())
    print(pid_list)
    for pid in pid_list:
        dicts[pid] = name
    return dicts
a = get_process("firrfox")
def check_process():
    pass

#
#
#
# def check_process_thread(pid):

# for key, value in dicts.items():
#     rr = re.compile(r'kworker\w*',flags=re.S)
#     # print(key)
#     print(rr.findall(key))
#     print(t.findall(key))