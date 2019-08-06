# coding: utf-8
__author__ = 'lau.wenbo'


import requests
import itchat

KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = { 'key' : KEY,
             'info' : msg,
             'userid' : 'wechat-rebot'}
    try:
        r = requests.post(apiUrl, data =data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply
itchat.auto_login(hotReload=True)
itchat.run()

