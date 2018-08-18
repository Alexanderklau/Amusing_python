# coding: utf-8

__author__ = 'lau.wenbo'


import xlrd

Excel = xlrd.open_workbook("../Example_by_work/work.xlsx")
sheet = Excel.sheet_by_name('Sheet1')
#打印sheet的名称，行数，列数
print sheet.name,sheet.nrows,sheet.ncols

#获取整行或者整列的数据
print sheet.row_values(4)
print sheet.col_values(4)


#获取单元格内容
print sheet.cell(1,0).value.encode('utf-8')
print sheet.cell_value(1,0).encode('utf-8')
print sheet.row(1)[0].value.encode('utf-8')