# coding: utf-8
__author__ = 'lau.wenbo'

from datetime import datetime
from elasticsearch import Elasticsearch
import elasticsearch.helpers
import random

es = Elasticsearch("10.0.6.118:9200")
package = []
for i in range(100000):
    row = {
        "@timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+0800"),
        "http_code": "404",
        "count": random.randint(1, 10000)
    }
    package.append(row)

print(len(package))

actions = [
    {
    '_op_type': 'index',
    '_index': "http_code",
    '_type': "error_code",
    '_source': d
    }
for d in package
]


elasticsearch.helpers.bulk(es, actions)