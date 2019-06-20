# coding: utf-8
__author__ = 'Yemilice_lau'


import random

random.seed(0x1010)  # 设置随机种子数
# 设置种子选择空间
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
ls = []  # 存取密码的列表
FirstPsw = ""  # 存取第一个密码的字符

while len(ls) < 20:  # 十个随机密码
    pwd = ""
    for i in range(8): # 密码位数
        pwd += s[random.randint(0, len(s) - 1)]
    if pwd[0] in FirstPsw:
        continue
    else:
        ls.append(pwd)
        FirstPsw += pwd[0]

    fo = open("user.txt", "w", encoding="utf-8")
    fo.write("\n".join(ls))
    fo.close()