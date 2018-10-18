# coding: utf-8

__author__ = 'lau.wenbo'

'''
修改Excel数值，添加/删除/修改
'''

import xlrd
import xlutils.copy
import re
import res
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

Excel = xlrd.open_workbook("../Example_by_work/3.xlsx")
table_name = Excel.sheet_names()
one_table = table_name[0]
sheet = Excel.sheet_by_name(one_table)
ws = xlutils.copy.copy(Excel)

# print sheet.name,sheet.nrows,sheet.ncols



def Calculator_money(nrows):
    dic = {}
    money = 0
    late_time = 0
    for z in sheet.row_values(nrows)[0:30]:
        if u"迟到" in z:
            later_times = re.compile(r'迟到\d+').findall(str(z))[0]
            times = re.compile(r'\d+').findall(str(later_times))[0]
            # print times
            late_time = late_time + int(times)
            if u"餐补40" in z:
                money = money + 40
            elif u"餐补20" in z:
                money = money + 20
        elif u"餐补40" in z:
            money = money + 40
        elif u"餐补20" in z:
            money = money + 20

    last_money = money - late_time
    dic["name"] = sheet.row_values(nrows)[0:3][0]
    dic["money"] = last_money
    dic["later"] = late_time
    return dic



name = []
id = []
money = []
later = []
for i in range(3,sheet.nrows):
    message = Calculator_money(i)
    name.append(message["name"])
    money.append(message["money"])
    later.append(message["later"])


res.write_name_excel(*name)
# res.write_id_excel(*id)
res.write_time_excel(*later)
res.write_money_excel(*money)
#
res.save_excel_data()

