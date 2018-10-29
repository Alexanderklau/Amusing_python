# coding: utf-8
__author__ = 'lau.wenbo'

import smtplib

from email.mime.text import MIMEText

from email.header import Header



sender = 'xxxxxxxxxx@163.com'

receivers = ['xxxxxxxxx@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱



# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码

message = MIMEText('test.in', 'plain', 'utf-8')


subject = '抢注域名'

message['Subject'] = Header(subject, 'utf-8')


smtp = smtplib.SMTP()

smtp.connect("smtp.163.com",25)    # 25 为 SMTP 端口号

smtp.login("xxxxxxxxxxx@163.com","password")

smtp.sendmail(sender, receivers, message.as_string())

smtp.quit()

print ("邮件发送成功")