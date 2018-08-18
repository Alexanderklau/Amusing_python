# coding: utf-8

__author__ = 'lau.wenbo'

'''
修改Excel数值，添加/删除/修改
'''

import xlrd
import xlwt
import xlutils.copy
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

Excel = xlrd.open_workbook("../Example_by_work/work.xlsx")
sheet = Excel.sheet_by_name('Sheet1')
ws = xlutils.copy.copy(Excel)

# print sheet.name,sheet.nrows,sheet.ncols



def Calculator_money(nrows):
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

    return last_money

def Write_excel(nrows,money):
    table = ws.get_sheet(0)
    table.write(nrows,53,money)


for i in range(4,sheet.nrows):
    money = Calculator_money(i)
    Write_excel(i,money)
ws.save("../Example_by_work/work.xlsx")

