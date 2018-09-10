# coding: utf-8
__author__ = 'lau.wenbo'

import xlrd
import xlwt

# data = {'date': u'1',
#         'tk_message': u'\u9910\u886540',
#         'id': u'78',
#         'name': u'\u51af\u5434\u5ca9'}

Excel = xlrd.open_workbook("./simple.xls")
sheet = Excel.sheet_by_name('data')
row = sheet.row_values(0)
col = sheet.col_values(0)




haha = []
for z,i in zip(range(0,len(col)),col):
    haha.append((z, i))

dic = []
for z, i in zip(range(0, len(row)), row):
    dic.append((z, i))

def get_row(data):
    for c in dic:
        try:
            if data["date"] == c[1]:
                row = c[0]
                return row
            else:
                continue
        except:
            return

def get_col(data):
    for h in haha:
        try:
            if data["id"] == h[1]:
                col = h[0]
                return col
            else:
                continue
        except:
            return


