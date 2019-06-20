# coding: utf-8

__author__ = "lau.wenbo"


import paramiko

class ssh_work:
    def __init__(self, hostname, username, daemon):
        self.hostname = hostname
        self.username = username
        self.password = daemon
        self.port = 22


    def ssh_work(self, command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)
        stdin, stdout, stderr = ssh.exec_command(command)
        print (stderr.read())
        ssh.close()


    def back_up(self, hostname):
        z = "cd /root/back_up/tool && python back_up.py back_up {hostname}".format(hostname=hostname)
        back_up = self.ssh_work(z)


    def send_file_node(self, hostname, send_node):
        uninstall_infi = self.ssh_work("scp -r /root/back_up/tool/{hostname}.tar.gz root@{send_node}:/root/back_up/tool".format(hostname=hostname, send_node=send_node))


    def backpack(self):
        back_pack = self.ssh_work("cd /root/back_up/tool && tar czvf infinity-cluster.tar.gz *.tar.gz && mv infinity-cluster.tar.gz /mnt && rm -rf *.tar.gz")


    def write_config(self, ips):
        command = "echo {ips} > /mnt/host".format(ips = ips)
        write_config = self.ssh_work(command)


    def cover_up(self, hostname):
        cover_up = self.ssh_work("cd /root/back_up/tool && python back_up.py cover_up {hostname}".format(hostname=hostname))


    def etcd_back_up(self):
        etcd_back_up = self.ssh_work("cd /root/back_up/tool && python back_up.py etcd_back_up")


    def etcd_cover_up(self):
        etcd_cover_up= self.ssh_work("cd /root/back_up/tool && python back_up.py etcd_cover_up")

    def scp_r(self, ip, node):
        work = self.ssh_work("scp -r {ip} /etc/csync2.cfg root@{node}".format(ip=ip, node=node))
