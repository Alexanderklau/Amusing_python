# coding: utf-8

__author__ = 'lau.wenbo'

'''
先拿到数据，再清洗数据，最后再计算数据，计算完毕之后挨个写入。
'''
import operator
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
    dic = {}
    name = sheet.row_values(ncrow)[0:35][3]
    id = sheet.row_values(ncrow)[0:35][1]
    dic[int(id)] = name
    return dic

def return_name():
    name_list = []
    for i in range(2,sheet.nrows):
        name_list.append(get_name_list(i))

    name_id = [{value: key} for key, value in dict([d.items()[0] for d in name_list]).items()]

    return name_id
#
# return_name()


# def return_id():
#     id_list = []
#     for i in range(2, sheet.nrows):
#         id_list.append(get_id_list(i))
#
#     # print(id_list)
#
#     a = set(id_list)
#     return a

