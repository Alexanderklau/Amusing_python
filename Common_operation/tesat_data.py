# coding: utf-8
__author__ = 'lau.wenbo'

message_list = [{'count': 1, 'severity': u'WARNING',
                 'hostname': 'node1', 'latest_time': u'1537950467.9',
                 'time': u'1537950467.9', 'module_name': u'nodes',
                 'description': u' storage node (node3) is down'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1',
                 'latest_time': u'1537950317.31', 'time': u'1537950317.31',
                 'module_name': u'cluster', 'description': u'1/3 mons down, quorum node2,node1'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1', 'latest_time': u'1537950467.9',
                 'time': u'1537950467.9', 'module_name': u'nodes', 'description': u' storage node (node3) is down'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1', 'latest_time': u'1537950467.9', 'time': u'1537950467.9',
                 'module_name': u'nodes', 'description': u' storage node (node3) is down'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1', 'latest_time': u'1537950467.9',
                 'time': u'1537950467.9', 'module_name': u'nodes', 'description': u' storage node (node3) is down'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1', 'latest_time': u'1537950467.9', 'time': u'1537950467.9',
                 'module_name': u'nodes', 'description': u' storage node (node3) is down'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1', 'latest_time': u'1537950467.9',
                 'time': u'1537950437.9', 'module_name': u'nodes', 'description': u' storage node (node3) is down'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1', 'latest_time': u'1537950467.9',
                 'time': u'1537950447.9', 'module_name': u'nodes', 'description': u' storage node (node3) is down'}]
l4=[]
# print(message_list[0])
l4.append(message_list[0])
for dict in message_list:
    k=0
    for item in l4:
      if dict['description'] != item['description']:
        k=k+1
      else:
        break
      if k == len(l4):
        l4.append(dict)
print "l4: ",l4