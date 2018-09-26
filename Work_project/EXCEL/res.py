# coding: utf-8

__author__ = 'lau.wenbo'


import xlwt

workbook = xlwt.Workbook(encoding = 'ascii')

worksheet = workbook.add_sheet('My Worksheet',cell_overwrite_ok=True)

# def craete_table():
#
#     a = [u'考勤号',u'姓名',u'迟到早退',u'餐补']
#
#     for i in range(0, len(a)):
#         worksheet.write(0, i, a[i])

def write_name_excel(*name):
    for i in range(0, len(name)):
        worksheet.write(i, 0, name[i])

# def write_id_excel(*id):
#     for i in range(0, len(id)):
#         worksheet.write(i, 0, id[i])

def write_time_excel(*times):
    for i in range(0, len(times)):
        worksheet.write(i, 1, times[i])

def write_money_excel(*money):
    for i in range(0, len(money)):
        worksheet.write(i, 2, money[i])

def save_excel_data():
    workbook.save('Excel_Workbook.xls')
