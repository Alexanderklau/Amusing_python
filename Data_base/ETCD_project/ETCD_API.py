# coding: utf-8

__author__ = 'Yemilice_lau'

import etcd


def __init__(self,
            host='127.0.0.1',
            port=4001,
            srv_domain=None,
            version_prefix='/v2',
            read_timeout=60,
            allow_redirect=True,
            protocol='http',
            cert=None,
            ca_cert=None,
            username=None,
            password=None,
            allow_reconnect=False,
            use_proxies=False,
            expected_cluster_id=None,
            per_host_pool_size=10
    ):
    client = etcd.Client(
        host='127.0.0.1',
        port=4003,
        allow_reconnect=True,
        protocol='https', )