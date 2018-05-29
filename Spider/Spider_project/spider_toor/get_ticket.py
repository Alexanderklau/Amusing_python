# coding: utf-8
__author__ = "Yemilice_lau"


import requests

a = requests.get("http://b.jowong.com/provider/ticket/ticketsearch.do?pdno=06027&rzti=2018-04-17&r=524")

print(a.text)