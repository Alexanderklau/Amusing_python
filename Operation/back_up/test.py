# coding: utf-8
__author__ = 'lau.wenbo'



node = "node214"
ceph_status = {'mgr_node': 1, 'mon_node': 1, 'mds_node': 1}
ceph_lists = {"mgr_node":"rgw","mds_node":"mds","mon_node":"mon"}
for i in ceph_lists.keys():
    status = ceph_status[i]
    if status == 1:
        a = "ceph-deploy {ceph} create {node}".format(ceph=ceph_lists[i], node=node)
