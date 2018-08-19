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

Excel = xlrd.open_workbook("../Example_by_work/test.xlsx")
sheet = Excel.sheet_by_name('Sheet1')
ws = xlutils.copy.copy(Excel)

# print sheet.name,sheet.nrows,sheet.ncols



def Calculator_money(nrows):
    dic = {}
    money = 0
    late_time = 0
    for z in sheet.row_values(nrows)[4:35]:
        if "/" in z:
            money = money + 20
        elif "X" in z:
            times = re.compile(r'\d+').findall(str(z))[0]
            late_time = late_time + int(times)
            if u"餐补" in z:
                money = money + 40
            else:
                money = money + 20
        elif u"餐补+1" in z:
            money = money + 20
        elif u"餐补" in z:
            money = money + 40
        else:
            continue

    last_money = money - late_time

    dic["name"] = sheet.row_values(nrows)[1:3][1]
    dic["id"] = int(sheet.row_values(nrows)[1:3][0])
    dic["money"] = last_money
    dic["later"] = late_time

    return dic



name = []
id = []
money = []
later = []
for i in range(4,sheet.nrows):
    message = Calculator_money(i)
    name.append(message["name"])
    id.append(message["id"])
    money.append(message["money"])
    later.append(message["later"])


res.write_name_excel(*name)
res.write_id_excel(*id)
res.write_time_excel(*later)
res.write_money_excel(*money)

res.save_excel_data()

