# -*- coding: utf-8 -*- 
#!/usr/bin/env python
"""
Author: Denis Liu<liu.yong@datatom.com>
Date: 2016-10-14
Function: sysdb node manage apps 
ChangLog:
"""
import sys
import socket
import ConfigParser
import time
import re
import logging
import infinity.common.infidef
import infinity.syslog.infi_syslog as syslog
import infinity.common.rpc.rpc_client as rpc
import infinity.misc.csync2.util as csync2
import infinity.common.inficore as infinity
import infinity.sysdb.sysdb as sysdb
import infinity.system.net as net
from cluster.cls_node import ClsNode

CONFIG_FILE = "/etc/sysdb/sysdb.conf"
DEFAULT_NODES_NUM = 5
DEFAULT_DATA_DIR = "/var/lib/sysdb"
TOKEN_STANDALONE = "standalone"
TOKEN_CLUSTER = "cluster"
MEMBER_READY_RETRY_TIMES = 10    # retry times
MEMBER_READY_WAIT = 2  # seconds

class SysdbMgt:
	def __init__(self):
		self.default_sysdb_num = DEFAULT_NODES_NUM
		self.log = syslog.InfiSyslog()
		return
		
	def _get_sysdb_endpoints(self):
		nodes = ""
		nodes_info = ""
		try:
			cf = ConfigParser.ConfigParser()
			cf.read(CONFIG_FILE)

			for item in cf.options("nodes"):
				if item == "nodes":
					nodes = cf.get('nodes', 'nodes')
		
		except Exception, ex:
			self.log.syslog(syslog.LOG_WARN, "sysdb mgt parse config failed")

		if not nodes:
			nodes_info = "127.0.0.1:2379"
			return nodes_info
		else:
			for item in nodes.split(','):
				nodes_info += "%s:2379," % item

			return nodes_info.rstrip(',')

	def _get_sysdb_node_member_id(self, ip):
		id = ""

		cmd = "/usr/bin/etcdctl --endpoints=%s member list" % self._get_sysdb_endpoints()
		(status, output) = sysdb.execute(cmd)
		for item in output.split('\n'):
			if re.search(r'%s' % ip, item):
				return item.split(',')[0].strip()
			
		return id

	def get_sysdb_nodes(self):
		nodes = []

		index = 0
		is_ready = False
		while index < MEMBER_READY_RETRY_TIMES:
			index += 1
			cmd = "/usr/bin/etcdctl --endpoints=%s member list" \
				% self._get_sysdb_endpoints()
			(status, output) = sysdb.execute(cmd)
			if status != 0:
				self.log.syslog(syslog.LOG_ERR, "get sysdb member info retry:%d, endpoint:%s,\
						output:%s" % (index, self._get_sysdb_endpoints(), output))
				continue
			else:
				is_ready = True
				break

		if not is_ready:
			self.log.syslog(syslog.LOG_ERR, "get sysdb member info failed:%s" % output)
			return (-1, nodes)
		
		#print output

		for item in output.split('\n'):
			detail = item.split(',')
			if detail[-1].strip().startswith("http://"):
				node_info = detail[-1].strip().split(':')
				node_info = node_info[1][2:]
				nodes.append(node_info)

		return (0, nodes)

	def is_sysdb_master_node(self):
		info = 0    # 0-unhealthy, 1-healthy
		end_points = ""

		(status, nodes) = self.get_sysdb_nodes()
		if status != 0:
			return False

		for item in nodes:
			end_points += item + ":2379," 

		if not end_points:
			return False

		cmd = "/usr/bin/etcdctl --endpoints=%s endpoint status" \
				% end_points.rstrip(',')
		(status, output) = sysdb.execute(cmd)
		if status != 0:
			self.log.syslog(syslog.LOG_ERR, "get sysdb health failed")
			return False

		#print nodes, output
		for item in output.split('\n'):
			if re.search(r"true", item.strip()):
				# if one node is healthy, the sysdb cluster is healty
				ip = item.split(':')[0]
				if net.is_local_ip(ip.strip()):
					return True
				else:
					return False

		return False


	def health(self):
		info = 0    # 0-unhealthy, 1-healthy
		end_points = ""

		(status, nodes) = self.get_sysdb_nodes()
		if status != 0:
			return (-1, info)

		for item in nodes:
			end_points += item + ":2379," 

		if not end_points:
			return (-1, info)

		cmd = "/usr/bin/etcdctl --endpoints=%s endpoint health" \
				% end_points.rstrip(',')
		(status, output) = sysdb.execute(cmd)
		if status != 0:
			self.log.syslog(syslog.LOG_ERR, "get sysdb health failed")
			return (0, info)

		#print nodes, output
		for item in output.split('\n'):
			if re.search(r"is healthy", item.strip()):
				# if one node is healthy, the sysdb cluster is healty
				info = 1 
				break

		return (0, info)

	def info(self):
		node_info = []
		value = {"cluster":"unhealthy"} 
		end_points = ""
		
		(status, nodes) = self.get_sysdb_nodes()
		if status != 0:
			return (-1, value)

		for item in nodes:
			end_points += item + ":2379," 

		# sysdb hostname convert to storage node
		handle = ClsNode()
		(status, output) = handle.list_system_node()
		if status != 0:
			# ignore the system node info
			self.log.syslog(syslog.LOG_ERR, "get sytsem node info failed")
			return (-1, value)
		else:
			node_info = output

		cmd = "/usr/bin/etcdctl --endpoints=%s endpoint health" \
				% end_points.rstrip(',')
		(status, output) = sysdb.execute(cmd)
		if status != 0:
			self.log.syslog(syslog.LOG_ERR, "get sysdb health failed")
			return (-1, value)

		#print nodes, output
		for node_item in nodes:
			for item in output.split('\n'):
				state = ""
				if item.strip().startswith(node_item):
					if re.search(r"is healthy", item.strip()):
						state = "healthy"
						value['cluster'] = "healthy"
					elif re.search(r"is unhealthy", item.strip()):
						state = "unhealthy"
					else:
						# invalid state, should not be here
						self.log.syslog(syslog.LOG_ERR, "get sysdb health unknown:%s, %s" \
								% (node_item, item))
						state = "unknown"

					# get hostname
					node_host = ""
					if node_info:
						for host_item in node_info['nodes']:
							if host_item['ip'] == node_item:
								node_host = host_item['hostname']
					
					if not node_host:
						self.log.syslog(syslog.LOG_ERR, "get sysdb health node hostname failed:%s" \
								% node_item)
						value[node_item] = state
					else:
						value[node_host] = state

					break

		return (0, sorted(value.items()))

	def _get_sysdb_instance_name(self, ip):
		(status, output) = infinity.execute("echo -n '%s' | md5sum | awk '{print $1}'" % ip)

		return output.strip()

	def do_enable_sysdb_node_service(self, ips):
		data_dir = ""
		# update config
		try:
			cf = ConfigParser.ConfigParser()
			cf.read(CONFIG_FILE)

			data_dir = cf.get('globals', 'data_dir')
			cfd = open(CONFIG_FILE, 'w')
			cf.set('nodes', 'nodes', ips)
			cf.write(cfd)
			cfd.close()
		except Exception, ex:
			self.log.syslog(syslog.LOG_ERR, "enable sysdb node service, update config failed:%s" % ips)
			return (-1, "failed to update config")

		# Clear sysdb dir 
		if not data_dir:
			data_dir = DEFAULT_DATA_DIR
		infinity.execute("rm -rf %s/*" % data_dir)
		
		# start sysdb service
		infinity.execute("systemctl reset-failed;systemctl restart sysdb")

		return (0, "success")

	def do_enable_sysdb_node(self, ip):
		(status, nodes_info) = self.get_sysdb_nodes()
		if status != 0:
			return (-1, "get enable sysdb node: get nodes failed")

		cmd = "/usr/bin/etcdctl --endpoints=%s member add %s --peer-urls=http://%s:2380" \
				% (self._get_sysdb_endpoints(), self._get_sysdb_instance_name(ip), ip)
		(status, output) = sysdb.execute(cmd)
		if status != 0:
			self.log.syslog(syslog.LOG_ERR, "do add member failed:%s" % output)
			return (-1, output)

		ip_info = ""
		for item in nodes_info: 
			ip_info += item + ","
		# new sysdb nodes ip
		ip_info += ip    
			
		(status, output) = rpc.RpcClient.send_message(ip, "mod", "misc.sysdb.sysdb_mgt.sys_enable_sysdb_node_service", [ip_info])
		if status != 0 or eval(output)[0] != 0:
			self.log.syslog(syslog.LOG_ERR, "do start new node sysdb service failed:%s,%s" % (ip, output))
			return (-1, "start new node sysdb service failed:%s, %d, %s" % (ip, status, output))

		return (0, "success")

	def do_disable_sysdb_node_service(self, ips):
		data_dir = ""
		# update config
		try:
			cf = ConfigParser.ConfigParser()
			cf.read(CONFIG_FILE)
			data_dir = cf.get('globals', 'data_dir')
			cfd = open(CONFIG_FILE, 'w')
			cf.set('nodes', 'nodes', "%s" % ips)
			cf.write(cfd)
			cfd.close()
		except Exception, ex:
			self.log.syslog(syslog.LOG_ERR, "disable sysdb node service, update config failed:%s" % ips)
			return (-1, "failed to update config")

		# Clear sysdb dir 
		if not data_dir:
			data_dir = DEFAULT_DATA_DIR
		infinity.execute("rm -rf %s/*" % data_dir)
		
		# start sysdb service
		infinity.execute("systemctl reset-failed;systemctl restart sysdb")

		return (0, "success")

	def do_disable_sysdb_node(self, ip):
		(status, nodes_info) = self.get_sysdb_nodes()
		if status != 0: 
			return (-1, "get sysdb node info failed")

		if len(nodes_info) == 1:
			return (-1, "there should be have one sysdb node")

		is_sysdb = False
		for item in nodes_info:
			if item == ip:
				# is a sysdb node
				is_sysdb = True
				break

		if not is_sysdb:
			# not sysdb node, just return
			return (0, 'success')

		member_id = self._get_sysdb_node_member_id(ip)
		if not member_id:
			return (-1, "get sysdb member id failed:%s" % ip)

		cmd = "/usr/bin/etcdctl --endpoints=%s member remove %s" \
				% (self._get_sysdb_endpoints(), member_id)
		(status, output) = sysdb.execute(cmd)
		if status != 0:
			return (-1, "disable sysdb failed:%d, %s" % (status, output))
		
		ips = ""
		for item in nodes_info:
			if item != ip:
				ips += item + ','

		ips = ips.rstrip(',')
		(status, output) = rpc.RpcClient.send_message(ip, "mod", "misc.sysdb.sysdb_mgt.sys_disable_sysdb_node_service", [ips])
		if status != 0 or eval(output)[0] != 0:
			detail = "disable sysdb node service failed:%s" % output
			self.log.syslog(syslog.LOG_ERR, detail)
			return (-1, detail)

		self.log.syslog(syslog.LOG_INFO, "disable sysdb node %s success" % ip)
		return (0, "success")

	def do_stop_sysdb_service(self, ip):
		(status, output) = self.get_sysdb_nodes()
		if status != 0:
			detail = "get sysdb nodes failed"
			self.log.syslog(syslog.LOG_ERR, detail)
			return (-1, detail)

		is_sysdb = False
		for item in output:
			if ip == item:
				is_sydb = True
				break

		if is_sysdb != True:
			detail  = "stop sysdb:%s is not a sysdb node" % ip
			self.log.syslog(syslog.LOG_INFO, detail)
			return (-1, detail)

		(status, output) = rpc.RpcClient.send_message(ip, "exe", "systemctl stop sysdb")
		if status != 0 or eval(output)[0] != 0:
			detail = "to stop sysdb service:%s failed" % ip
			self.log.syslog(syslog.LOG_INFO, detail)
			return (-1, detail)

		return (0, "success")

	def do_resume_sysdb_service(self, ip):
		(status, output) = self.get_sysdb_nodes()
		if status != 0:
			detail = "get sysdb nodes failed" 
			self.log.syslog(syslog.LOG_ERR, detail)
			return (-1, detail)

		is_sysdb = False
		for item in output:
			if ip == item:
				is_sydb = True
				break

		if is_sysdb != True:
			detail  = "resume sysdb:%s is not a sysdb node" % ip
			self.log.syslog(syslog.LOG_INFO, detail)
			return (-1, detail)

		(status, output) = rpc.RpcClient.send_message(ip, "exe", "systemctl restart sysdb")
		if status != 0 or eval(output)[0] != 0:
			detail = "to resume sysdb service:%s failed" % ip
			self.log.syslog(syslog.LOG_INFO, detail)
			return (-1, detail)

		return (0, "success")

	def do_add_sysdb_node(self, ips):
		data_dir = ""
		try:
			cf = ConfigParser.ConfigParser()
			cf.read(CONFIG_FILE)
			data_dir = cf.get('globals', 'data_dir')

			cfd = open(CONFIG_FILE, 'w')
			cf.set('nodes', 'nodes', ips)
			cf.set('globals', 'token', TOKEN_CLUSTER)
			cf.write(cfd)
			cfd.close()
		except Exception, ex:
			self.log.syslog(syslog.LOG_ERR, "add sysdb node, update config failed:%s, %s" % (Exception, ex))
			return (-1, "update config failed")

		# stop sysdb service and delete old data
		infinity.execute("systemctl stop sysdb")
		if data_dir == "":
			data_dir = DEFAULT_DATA_DIR
		infinity.execute("rm -rf %s/*" % data_dir)

		return (0, "success")

	def init_sysdb(self, ips):
		local_ip = ""
		ip_info = ""
		
		# if new sysdb have the local ip, first time to init sysdb cluster?
		is_local = False
		for item in ips.split(','):
			if net.is_local_ip(item.strip()):
				local_ip = item.strip()
				is_local = True
				continue

			ip_info += item.strip() + ","
		
		if is_local:
			(status, output) = self.create_sysdb_node("", local_ip)
			if status != 0:
				return (status, output)
		
		if ip_info:
			ip_info = ip_info.rstrip(',')
			for item in ip_info.split(','):
				# sleep some seconds, to make sure the nodes info is updated
				(status, output) = self.get_sysdb_nodes()
				if status != 0:
					detail = "init sysdb , get sysdb nodes failed:%s" % item
					self.log.syslog(syslog.LOG_ERR, detail)
					return (-1, detail)
				
				cur_ips = ""
				for node_item in output:
					cur_ips += node_item + ','

				(status, output) = self.create_sysdb_node(cur_ips.rstrip(','), item)
				if status != 0:
					return (status, output)

		# sync final sysdb conf, and restart sysdb service, to avoid conflicts of confsync
		(status, output) = self.get_sysdb_nodes()
		if status != 0:
			# do nothing
			pass
		else:
			db_nodes = ""
			for item in output:
				db_nodes += item + ','

			for item in output:
				self.log.syslog(syslog.LOG_INFO, "init sysdb: %s, sysdb nodes:%s" % (ips, db_nodes))
				(status, output) = rpc.RpcClient.send_message(item, "mod", "misc.sysdb.sysdb_mgt.sys_update_sysdb_node_config", ["nodes", "nodes", db_nodes.rstrip(',')])
				if status != 0 or eval(output)[0] != 0:
					self.log.syslog(syslog.LOG_INFO, "init sysdb: %s, sync %s failed" % (ips, item))
				else:
					print rpc.RpcClient.send_message(item, "exe", "systemctl restart sysdb")
					self.log.syslog(syslog.LOG_INFO, "init sysdb: %s, sync %s success" % (ips, item))

		return (0, "success")

	# when add new sysdb node, we need to wait sysdb nodes ready(in member list), then 
	# to do other things, IMPORTANT!
	def _wait_sysdb_nodes_ready(self, cur_ips, add_ip):
		member_info = ""
		is_ready = False
		index = 0
		while index < MEMBER_READY_RETRY_TIMES:
			index += 1
			time.sleep(MEMBER_READY_WAIT)
			(status, output) = self.get_sysdb_nodes()
			if status != 0: 
				# maybe in critical time, wait seconds and try 
				self.log.syslog(syslog.LOG_INFO, "wait sysdb node ready:%s,%s,%d, %s, retry:%d" \
					% (cur_ips, add_ip, status, output, index))
				continue
				
			member_info = ""
			for item in output:
				member_info += item + ","
				if add_ip == item:
					is_ready = True

			if is_ready:
				break

			self.log.syslog(syslog.LOG_INFO, "wait sysdb node ready:%s,%s,%d, %s, retry:%d" \
				% (cur_ips, add_ip, status, output, index))

		if is_ready:
			self.log.syslog(syslog.LOG_INFO, "wait sysdb node ready:%s,%s,%s succsss" \
					% (cur_ips, add_ip, member_info.rstrip(',')))
		else:
			self.log.syslog(syslog.LOG_ERR, "wait sysdb node ready:%s,%s,%s failed" \
					% (cur_ips, add_ip, member_info.rstrip(',')))

		return is_ready 

	# Only support to add sysdb node one by one, avoid to cause sysdb cluster to be 
	# inconsistent state
	def create_sysdb_node(self, cur_ips, add_ip):
		self.log.syslog(syslog.LOG_INFO, "create sysdb node:%s, %s" % (cur_ips, add_ip))
		if not cur_ips:
			# self add self
			# no sysdb cluser before, first time to initialize
			# must be current node
			if not net.is_local_ip(add_ip.strip()):
				self.log.syslog(syslog.LOG_ERR, "init sysdb, the first sysdb node must be local")
				return (-1, "the first sysdb node ip must be local")


			# no init sysdb cluster before, do initialize
			# current node is the master node of init cluster
			try:
				cf = ConfigParser.ConfigParser()
				cf.read(CONFIG_FILE)

				cfd = open(CONFIG_FILE, 'w')
				cf.set('globals', 'token', TOKEN_CLUSTER)
				cf.set('nodes', 'nodes', add_ip)
				cf.write(cfd)
				cfd.close()
			except Exception, ex:
				self.log.syslog(syslog.LOG_ERR, "init sysdb update token failed")
				print Exception, ex
				return (-1, "failed to update cluster token")

			# do restart sysdb service, to be cluster mode
			infinity.execute("systemctl restart sysdb")

			self._wait_sysdb_nodes_ready(cur_ips, add_ip)

			return (0, "success")
	
		# there is sysdb cluster before, to add new node
		# firstly to update the new node sysdb config
		(status, output) = self.get_sysdb_nodes()
		(status, output) = rpc.RpcClient.send_message(add_ip, "mod", "misc.sysdb.sysdb_mgt.sys_add_sysdb_node", [cur_ips])
		if status != 0 or eval(output)[0] != 0:
			self.log.syslog(syslog.LOG_ERR, "init sydb, add sysdb node failed:%d, cur_ips:%s, add_ip:%s, %s" \
					% (status, cur_ips, add_ip, str(output)))
			return (-1, "add sysdb node failed")

		# secondly, to choose the new node as sysdb node or not
		# if the sysdb nodes >= DEFAULT_NODES_NUM, just return
		(status, output) = self.get_sysdb_nodes()
		if status != 0:
			# return ok
			return (0, "add sysdb node, get node num failed")

		if len(output) >= DEFAULT_NODES_NUM:
			return (0, "success")

		self._wait_sysdb_nodes_ready(cur_ips, add_ip)

		# add the the new ip as sysdb node
		(status, output) = self.do_enable_sysdb_node(add_ip)
		if status != 0: 
			self.log.syslog(syslog.LOG_ERR, "init sysdb, enable sysdb node failed:%d, %s" % (status, output))
			return (-1, output)

		self._wait_sysdb_nodes_ready(cur_ips, add_ip)

		# update local nodes config
		try:
			cf = ConfigParser.ConfigParser()
			cf.read(CONFIG_FILE)

			cfd = open(CONFIG_FILE, 'w')
			cf.set('nodes', 'nodes', cur_ips + ',' + add_ip)
			cf.write(cfd)
			cfd.close()
		except Exception, ex:
			self.log.syslog(syslog.LOG_ERR, "init sysdb update nodes failed:%s, %s" % (Exception, ex))

		return (0, "success")

	def do_update_sysdb_node_config(self, section, key, value):
		try:
			cf = ConfigParser.ConfigParser()
			cf.read(CONFIG_FILE)

			cfd = open(CONFIG_FILE, 'w')
			cf.set(section, key, value)
			cf.write(cfd)
			cfd.close()
		except Exception, ex:
			detail = "update sysdb config failed:%s, %s, %s" % (section, key, value)
			self.log.syslog(syslog.LOG_ERR, detail)
			return (-1, detail)

		return (0, "success")

	def destroy_sysdb_node(self, ip):
		# no need to check return value
		(status, output) = self.do_disable_sysdb_node(ip)
		if status != 0: 
			detail = "destroy sysdb node, disable failed:%s" % output
			self.log.syslog(syslog.LOG_ERR, detail)

		# update the destory node config of sysdb
		(status, output) = rpc.RpcClient.send_message(ip, "mod", "misc.sysdb.sysdb_mgt.sys_update_sysdb_node_config", ["nodes", "nodes", ""])
		if status != 0 or eval(output)[0] != 0:
			detail = "destroy sysdb node, update nodes info failed:%s"  % ip
			self.log.syslog(syslog.LOG_ERR, detail)

		(status, output) = rpc.RpcClient.send_message(ip, "mod", "misc.sysdb.sysdb_mgt.sys_update_sysdb_node_config", ["globals", "token", TOKEN_STANDALONE])
		if status != 0 or eval(output)[0] != 0:
			detail = "destroy sysdb node, update nodes token failed:%s" % ip
			self.log.syslog(syslog.LOG_ERR, detail)

		(stauts, output) = rpc.RpcClient.send_message(ip, "exe", "systemctl stop sysdb;rm -rf %s/*;systemctl restart sysdb;systemctl restart infi-api" % DEFAULT_DATA_DIR)
		if status != 0 or eval(output)[0] != 0:
			detail = "destory sysdb node ,restart the node sysdb service failed:%s" % ip
			self.log.syslog(syslog.LOG_ERR, detail)

		# update the sysdb config of cluster
		try:
			new_nodes = ""
			cf = ConfigParser.ConfigParser()
			cf.read(CONFIG_FILE)
			nodes = cf.get('nodes', 'nodes')
			(status, output) = self.get_sysdb_nodes()
			if status != 0:
				self.log.syslog(syslog.LOG_ERR, "destory sysdb node, get sysdb node failed")
				for item in nodes.split(','):
					if item != ip:
						new_nodes += item + ','
			else:
				for item in output:
					new_nodes += item + ','
			
			cfd = open(CONFIG_FILE, 'w')
			cf.set('nodes', 'nodes', new_nodes.rstrip(','))
			cf.write(cfd)
			cfd.close()
		except Exception, ex:
			self.log.syslog(syslog.LOG_ERR, "destroy sysdb, update nodes failed:%s, %s" % (Exception, ex))

		self.log.syslog(syslog.LOG_INFO, "destroy sysdb node %s success" % ip)
		return (0, "success")

	def reset_sysdb(self):
		db_dir = ""

		# firstly, stop sysdb service
		infinity.execute("systemctl stop sysdb")
		
		# secondly, update config file
		try:
			cf = ConfigParser.ConfigParser()
			cf.read(CONFIG_FILE)
			db_dir = cf.get('globals', 'data_dir')

			cfd = open(CONFIG_FILE, 'w')
			cf.set('nodes', 'nodes', '')

			# reset to be standalone mode
			cf.set('globals', 'token', TOKEN_STANDALONE)
			cf.write(cfd)
			cfd.close()
		except Exception, ex:
			self.log.syslog(syslog.LOG_ERR, "reset sysdb, update config failed:%s" % ex)
			return (-1, "failed to update config file")

		# finally, delete old db, and start service
		if db_dir:
			infinity.execute('rm -rf %s/*' % db_dir)
		else:
			infinity.execute('rm -rf %s/*' % DEFAULT_DATA_DIR)
		
		infinity.execute('systemctl reset-failed')
		# restart services
		srv_list = ['sysdb', 'infi-monitor', 'smartord', 'infi-api']
		for item in srv_list:
			infinity.execute('systemctl restart %s' % item, 30)


		return (0, "success")


# interface
def sys_enable_sysdb_node_service(ips):
	handle = SysdbMgt()

	(status, output) = handle.do_enable_sysdb_node_service(ips)

	return (status, output)

def sys_disable_sysdb_node_service(ips):
	handle = SysdbMgt()

	(status, output) = handle.do_disable_sysdb_node_service(ips)

	return (status, output)

def sys_update_sysdb_node_config(section, key, value):
	handle = SysdbMgt()

	(status, output) = handle.do_update_sysdb_node_config(section, key ,value)

	return (status, output)

def sys_add_sysdb_node(ips):
	handle = SysdbMgt()

	(status, output) = handle.do_add_sysdb_node(ips)

	return (status, output)

if __name__=='__main__':
	m = SysdbMgt()
	ips = sys.argv[1]
	#print m.health()
	#print m.info()
	#print m.is_sysdb_master_node("sysdb")
	#print m.get_sysdb_nodes("sysdb")
	#print m.init_sysdb("10.0.5.31,10.0.5.32,10.0.5.33","svetcd")
	#print m.do_disable_sysdb_node("10.0.7.42")
	#print m.do_disable_sysdb_node("10.0.7.147")
	m.init_sysdb(ips)
	#print m.do_disable_sysdb_node("10.0.7.147")
	#print m.do_enable_sysdb_node('10.0.7.42')
	#print m.do_enable_sysdb_node('10.0.7.147')
	#print m.reset_sysdb()
	#print m.destroy_sysdb_node('10.0.7.184')
	pass
