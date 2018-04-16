# coding: utf-8
__author__ = "Yemilice_lau"


import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

headers = {
    "charset":"utf-8",
    "Accept-Encoding":"gzip",
    "refer":"https://servicewechat.com/wx43b7026dd2b6a475/2/page-frame.html",
    "thirdkey":"9iJTBmLglpNszMnRr0rHskUkf9RCUnkJwl1PtvJyVm2B3v7vQfioyKmWwvPEPjna",
    "scene":"1089",
    "appcode":"1",
    "Content-type":"application/x-www-form-urlencoded,application/json",
    "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; OPPO R9 Plusm A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044005 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060634) NetType/WIFI Language/zh_CN MicroMessenger/6.6.6.1300(0x26060634) NetType/WIFI Language/zh_CN",
    "Host":"wxapp.58.com",
    "Content-Length":"353",
    "Connection":"Keep-Alive",
}

data = {
    "param":{
        "cityId":102,
        "cateCode":"1",
        "cateId":"8",
        "dispCateId":"8",
        "pageNum":1,
        "key":"",
        "queryList":{},
        "thirdKey":"9iJTBmLglpNszMnRr0rHskUkf9RCUnkJwl1PtvJyVm2B3v7vQfioyKmWwvPEPjna"
    },
    "thirdKey":"9iJTBmLglpNszMnRr0rHskUkf9RCUnkJwl1PtvJyVm2B3v7vQfioyKmWwvPEPjna",
    "appCode":1

}

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
a = requests.post("https://wxapp.58.com/list/info", data = json.dumps(data), headers = headers, verify=False)
print(a.text)
# c = a.content
# print(c.decode("utf-8"))

