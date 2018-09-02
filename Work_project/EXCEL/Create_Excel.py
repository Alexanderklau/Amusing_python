# coding: utf-8

__author__ = 'lau.wenbo'


import xlrd
import xlutils.copy

Excel = xlrd.open_workbook("../Example_by_work/1.xlsx")

table_name = []
for i in Excel.sheet_names():
     if u"考勤明细-1" in i:
         table_name.append(i)


sheet = Excel.sheet_by_name(table_name[0])
ws = xlutils.copy.copy(Excel)


def create_dict(nrows):
    dicts = {}
    message = sheet.row_values(nrows)[1:35]
    id = message[0]
    name = message[2]
    date = message[4].split('/')[2]

    start_work_date = message[8]
    end_work_date = message[9]

    if start_work_date.strip() == "" or end_work_date.strip() == "":
        tk_message = "?"
    elif int(start_work_date.split(":")[0]) >= 10 and int(end_work_date.split(":")[0]) >= 22:
        start_late_time = str(int(start_work_date.split(":")[1]))
        time_date = "X{time}MIN".format(time=start_late_time)
        tk_message = time_date + "," + u'餐补'
    elif int(start_work_date.split(":")[0]) >= 10:
        start_late_time = str(int(start_work_date.split(":")[1]))
        time_date = "X{time}MIN".format(time=start_late_time)
        tk_message = time_date
    elif int(end_work_date.split(":")[0]) >= 22:
        tk_message = u'餐补'
    else:
        tk_message = '/'

    dicts["id"] = id
    dicts["name"] = name
    dicts["date"] = date
    dicts["tk_message"] = tk_message
    print name, tk_message
    return dicts


for i in range(1,sheet.nrows):
    message = create_dict(i)
    print message


