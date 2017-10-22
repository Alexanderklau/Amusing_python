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


def getdistrictcode():
    with open('districtcode') as file:
        data = file.read()
    districtlist = data.split('\n')
    global codelist, state, city
    codelist = []
    for node in districtlist:
        # print node
        if node[10:11] != ' ':
            state = node[10:].strip()
        if node[10:11] == ' ' and node[12:13] != ' ':
            city = node[12:].strip()
        if node[10:11] == ' ' and node[12:13] == ' ':
            district = node[14:].strip()
            code = node[0:6]
            codelist.append({"state": state, "city": city, "district": district, "code": code})


if __name__ == '__main__':
    print getdistrictcode()
