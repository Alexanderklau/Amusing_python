# coding: utf-8

__author__ = "lau.wenbo"


import smtplib
from email.mime.text import MIMEText

msg_from = 'xxxxxxxxx@qq.com'  # 发送方邮箱
passwd = 'abcdefghigklmnop'  # 填入发送方邮箱的授权码
msg_to = 'xxxxx@foxmail.com'  # 收件人邮箱

subject = "python邮件测试"  # 主题
content = "这是我使用python smtplib及email模块发送的邮件"
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print ("发送成功")
except s.SMTPException, e:
    print "发送失败"
finally:
    s.quit()