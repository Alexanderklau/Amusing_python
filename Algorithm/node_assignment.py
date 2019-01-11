# coding: utf-8

__author__ = 'lau.wenbo'

"""
节点分配代码
节点列表
节点角色    
根据数量随机节点角色
{{node:"node1",part="master"},{node:"node2",part="data"}}
"""

import yaml

def write_yml(node, node_list):
    fr = open('elasticsearch.yml','w')
    data = {
        'path.logs': '/var/log/elasticsearch',
        'discovery.zen.minimum_master_nodes': 1,
        'network.bind_host': '::',
        'node.data': True,
        'discovery.zen.ping.unicast.hosts': node_list,
        'http.port': 9200,
        'http.cors.enabled': True,
        'network.host': '10.0.6.244',
        'cluster.name': 'Es_test',
        'path.data': '/var/lib/elasticsearch',
        'transport.tcp.port': 9300,
        'http.cors.allow-origin': '*',
        'node.name': 'es_{node}'.format(node=node),
        'node.master': True
           }

    yaml.safe_dump(data, fr, default_flow_style=False, encoding='utf-8', allow_unicode=True)


write_yml("node1",["10.0.6.244","10.0.6.245"])
