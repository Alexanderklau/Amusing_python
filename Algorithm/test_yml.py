# coding: utf-8
__author__ = 'lau.wenbo'


import yaml

def write_yml(node, node_list):
    fr = open('elasticsearch.yml','w')
    data = {
        "filebeat.inputs":
    }

    yaml.safe_dump(data, fr, default_flow_style=False, encoding='utf-8', allow_unicode=True)


write_yml("node1",["10.0.6.244","10.0.6.245"])
