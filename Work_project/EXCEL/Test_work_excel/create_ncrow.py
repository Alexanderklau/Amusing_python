# coding: utf-8

__author__ = 'lau.wenbo'

'''
先拿到数据，再清洗数据，最后再计算数据，计算完毕之后挨个写入。
'''
import xlrd
import xlutils.copy
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

Excel = xlrd.open_workbook("../../Example_by_work/1.xlsx")

table_name = []
for i in Excel.sheet_names():
     if u"考勤明细-1" in i:
         table_name.append(i)

sheet = Excel.sheet_by_name(table_name[0])
ws = xlutils.copy.copy(Excel)

def get_name_list(ncrow):
    name = sheet.row_values(ncrow)[0:35][3]
    return name

def return_name():
    name_list = []
    for i in range(2,sheet.nrows):
        name_list.append(get_name_list(i))

    a = set(name_list)
    return a

