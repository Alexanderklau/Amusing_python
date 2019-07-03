# coding: utf-8

__author__ = 'Yemilice_lau'


import requests
import random
import os
import sys
import time
import ConnectionError
import Module_bException

module_b = "10.10.10.115:10081,10.10.10.115:10082,10.10.10.115:10083,10.10.10.115:10084"

class Module_b():

    def __init__(self):
        self.url_prefix = [val.strip() for val in module_b.split(',')]

    def _request(self, short_uri, payload):
        res = None
        try_count = 1
        url_prefixs = self.url_prefix[:]
        url_prefixs.sort(key=lambda f: random.randint(0, 100))

        for curr_url_prefix in url_prefixs:
            url = os.path.join(curr_url_prefix, short_uri)
            try:
                res = requests.post(url, data=payload)
                break
            except ConnectionError as e:
                try_count += 1
                sys.stderr.write('can not connect to Module_b, retry ...\n')
                time.sleep(1)
                if try_count == len(url_prefixs):
                    raise e
        if res.status_code != 200:
            raise Module_bException('HTTP ERROR: %s' % res.text)
        result = res.json()
        if result['status'] != '0':
            raise Module_bException(result['errstr'])
        return result['result']