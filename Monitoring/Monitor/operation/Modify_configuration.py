# coding: utf-8
__author__ = 'lau.wenbo'

import json
import sys


def revise():
    print("修改哪一项?")
    with open("./Monitor/setting.json", "rb") as load_f:
        load_dict = json.load(load_f)
    print("1.CPU阀值:{0}%\n"
          "2.内存阀值:{1}%\n"
          "3.检测时间:{2}秒\n"
          "4.返回上一步".format(load_dict["CPU_max"], load_dict["Memory_max"], load_dict["time"]))
    str = raw_input("输入对应的数字: ")
    if str == "1":
        str = input("输入修改的数值: ")
        if int(str) > 100 or int(str) < 0:
            print("输入值不合法！检查你的输入是否大于100或者小于0！")
            print("返回上一步.........")
        else:
            load_dict["CPU_max"] = str
            print("修改成功！")
            print("返回上一步.........")
    elif str == "2":
        str = input("输入修改的数值: ")
        if int(str) > 100 or int(str) < 0:
            print("输入值不合法！检查你的输入是否大于100或者小于0！")
            print("返回上一步.........")
        else:
            load_dict["Memory_max"] = str
            print("修改成功！")
            print("返回上一步.........")
    elif str == "3":
        str = input("输入修改的数值: ")
        if int(str) > 100 or int(str) < 0:
            print("输入值不合法！检查你的输入是否大于100或者小于0！")
            print("返回上一步.........")
        else:
            load_dict["time"] = str
            print("修改成功！")
            print("返回上一步.........")
    elif str == "4":
        sys.exit()
    else:
        print("错误的输入")
    a = load_dict

    with open("../Monitor/setting.json", "wb") as f:
        data = json.dump(a, f)


