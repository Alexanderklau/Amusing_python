# coding: utf-8

__author__ = 'lau.wenbo'


import xlwt
from xlwt import Workbook
import create_work


book = Workbook(encoding='utf-8')

sheet1 = book.add_sheet('data')

def get_month_day(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        days = 31
    elif month in (4, 6, 9, 11):
        days = 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days = 29
        else:
            days = 28
    else:
        return

    return days

def create_column(day):
    sheet1.write(0,0,u"名字")
    for i in range(1, int(day) + 1):
        sheet1.write(0,i,i)
    sheet1.write(0,int(day+1),u'迟到早退')

    book.save('simple.xls')

def create_name(name_list):
    z = [i for i in name_list]
    x = [i for i in range(1, len(name_list) + 1)]
    for a,b in zip(z,x):
        sheet1.write(b, 0, a)
    book.save('simple.xls')

def create_message(message):
    pass


day = get_month_day(9, 2018)
create_column(day=int(day))
name_list = create_work.return_name()
create_name(name_list)
