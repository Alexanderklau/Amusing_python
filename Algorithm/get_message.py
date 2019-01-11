# coding: utf-8
__author__ = 'lau.wenbo'

import yaml

filename = open('test.yml')
y = yaml.load(filename)
print(y["ip_list"])
# with open('test.yml') as f:
#     doc = yaml.load(f)
#     ip_list = doc['ip_list']
#     print(ip_list)
#     ip_list.remove("10.0.6.217")
#     doc['ip_list'] = ip_list
#
# with open('test.yml', 'w') as f:
#     yaml.dump(doc, f, default_flow_style=False, encoding='utf-8', allow_unicode=True)
