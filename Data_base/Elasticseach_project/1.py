# coding: utf-8
__author__ = 'lau.wenbo'

dic = {}
a = "2018-12-26T01:29:42.928569-05:00 node111 smbd_audit: huangke|share|10.0.6.148|unlink|ok|总结.docx"
time = a.split("smbd_audit:")[0].split(" ")[0].split("T")[0]
ss = a.split("smbd_audit:")[0].split(" ")[0].split("T")[1].split('.')[0]
dic["time"] = time + " " + ss
dic["user_name"] = a.split("smbd_audit:")[1].split(" ")[1].split("|")[0]
dic["share_name"] = a.split("smbd_audit:")[1].split(" ")[1].split("|")[1]
dic["user_ip"] = a.split("smbd_audit:")[1].split(" ")[1].split("|")[2]
dic["user_op"] = a.split("smbd_audit:")[1].split(" ")[1].split("|")[3]
dic["user_op_status"] = a.split("smbd_audit:")[1].split(" ")[1].split("|")[4]
dic["user_op_target"] = a.split("smbd_audit:")[1].split(" ")[1].split("|")[5]

print(dic)