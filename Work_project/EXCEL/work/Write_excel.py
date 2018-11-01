# coding: utf-8

__author__ = 'lau.wenbo'

'''
修改Excel数值，添加/删除/修改
'''

import xlrd
import res
import xlutils.copy
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

Excel = xlrd.open_workbook("data.xlsx")
table_name = Excel.sheet_names()
one_table = table_name[0]
sheet = Excel.sheet_by_name(one_table)


def Calculator_money(nrows,date):
    dic = {}
    money = 0
    late_time = 0
    for z in sheet.row_values(nrows)[0:date]:
        if u"迟到" in z:
            later_times = re.compile(r'迟到\d+').findall(str(z))[0]
            times = re.compile(r'\d+').findall(str(later_times))[0]
            # print times
            late_time = late_time + int(times)
            if u"餐补40" in z:
                money = money + 40
            elif u"餐补20" in z:
                money = money + 20
            elif u"餐补120" in z:
                money = money + 120
        elif u"餐补40" in z:
            money = money + 40
        elif u"餐补20" in z:
            money = money + 20
        elif u"餐补120" in z:
            money = money + 120

    last_money = money - late_time
    dic["name"] = sheet.row_values(nrows)[0:3][0]
    dic["money"] = last_money
    dic["later"] = late_time
    return dic

def Calculator_tx_money(nrows,date):
    dic = {}
    money = 0
    late_time = 0
    for z in sheet.row_values(nrows)[1:date+1]:
        if u"迟到" in z:
            later_times = re.compile(r'迟到\d+').findall(str(z))[0]
            times = re.compile(r'\d+').findall(str(later_times))[0]
            # print times
            late_time = late_time + int(times)
            if u"餐补40" in z:
                money = money + 40
            elif u"餐补20" in z:
                money = money + 20
            elif u"餐补120" in z:
                money = money + 120
        elif u"餐补40" in z:
            money = money + 40
        elif u"餐补20" in z:
            money = money + 20
        elif u"餐补120" in z:
            money = money + 120

    last_money = money - late_time
    dic["name"] = sheet.row_values(nrows)[0:3][1]
    dic["money"] = last_money
    dic["later"] = late_time
    return dic

def write_data(date, code):
    name = []
    money = []
    later = []
    for i in range(3,sheet.nrows):
        if code == 1:
            message = Calculator_money(i,int(date))
            name.append(message["name"])
            money.append(message["money"])
            later.append(message["later"])
        elif code == 2:
            message = Calculator_tx_money(i, int(date))
            name.append(message["name"])
            money.append(message["money"])
            later.append(message["later"])


    res.write_name_excel(*name)
    res.write_time_excel(*later)
    res.write_money_excel(*money)
    #
    res.save_excel_data()

def server_help():
    data = """
    把表放到和程序同一个文件夹下就可以了，请先将名字改为XX月考勤表这样，也可以不改。
    只能一个一个计算。每次只能有一个表和程序在同一个文件夹内。输出表为当前的表格的餐补，迟到金额等
    """
    print(data)

if __name__ == "__main__":
    while True:
        print("#" * 30)
        print("考勤表生成小程序---专用")
        print("选择相对应的服务")
        print("1:计算一般考勤\n"
              "2:计算特殊考勤\n"
              "3:帮助\n"
              "4:退出")
        print("#" * 30)
        strs = raw_input("选择对应的服务: ")
        if strs == "1":
            date = raw_input("输入本月天数:")
            write_data(date, int(strs))
            print("计算完成，正在退出.....")
            sys.exit("Bye~")
        elif strs == "2":
            date = raw_input("输入本月天数:")
            write_data(date, int(strs))
            print("计算完成，正在退出.....")
            sys.exit("Bye~")
        elif strs == "3":
            print("--------------------")
            print("\n")
            server_help()
            print("\n")
            print("--------------------")
        elif strs == "4":
            sys.exit("Bye~")
        else:
            print("--------------------")
            print("\n")
            print("输入错误了！没这个选项")
            print("\n")
            print("--------------------")