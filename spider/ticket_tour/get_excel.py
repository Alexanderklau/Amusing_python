# coding: utf-8
__author__ = 'lau.wenbo'

"""
我这套逻辑依靠的是addTourist接口，这个接口主要就是解决excel添加
现在的逻辑是解析excel --> 调用添加api ---> 添加用户 --->
"""


import requests
import xlrd

add_url = "http://b.jowong.com/team/addTourist.do?" \
          "bznote={bznote}&" \
          "touristname={name}" \
          "credentialstype=01&" \
          "credentials={id}&" \
          "mobile={phone}"


# 打开名为1的excel 文件
ExcelFile=xlrd.open_workbook('1.xls')
table = ExcelFile.sheets()[0]
nrows = table.nrows
t = ["name","type","id","phone"]
z = []
for i in range(nrows):
    if i == 0:
        continue
    z.append(dict(zip(t,table.row_values(i))))


# bznote 已经有了，所以这里就不再显示
for x in z:
    requests.post(add_url.format(bznote,x["name"],x["id"],x["phone"]))


