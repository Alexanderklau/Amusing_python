# -*- coding: utf-8 -*-
__author__ = 'yemilice_lau'
"""
1.身份证必须能够通过身份证校验程序。
2.出生年月日是8位,顺序码是3位，男生末尾为基数，女生末尾为偶数。

校验码算法：
前17位数字每一位有一个权重值
将第i位上的权重值记作Wi，Wi的值为 7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2
将身份证第i位的数字记作Ai
则使用下列公式算出一个数
S = Sum(Ai*Wi) mod 11 ------------- Sum(Ai*Wi) 取11的模。
"""
from datetime import date
from datetime import timedelta
import random


def getdistrictcode():
    with open('id_code.txt') as file:
        data = file.read()
    districtlist = data.split('\n')
    global codelist, state, city
    codelist = []
    for node in districtlist:
        if node != '':
            if node[10:11] != ' ':
                state = node[10:].strip()
            if node[10:11] == ' ' and node[12:13] != ' ':
                city = node[12:].strip()
            if node[10:11] == ' ' and node[12:13] == ' ':
                district = node[14:].strip()
                code = node[0:6]
                codelist.append({"state": state, "city": city, "district": district, "code": code})
        else:
            pass
    return codelist


def gennerator(code=None):
    id = codelist[random.randint(0, len(codelist))]['code']  # 地区项
    id = id + str(random.randint(1930, 2013))  # 年份项
    da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理

    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                 '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]
    id = id + checkcode[str(count % 11)]  # 算出校验码
    return id


if __name__ == "__main__":
    lt = []
    i = 1
    s = 0
    while i <= 10:
        i = i + 1
        code_list = getdistrictcode()
        code = gennerator(code_list)
        lt.append(code)
    print lt
