# coding: utf-8

__author__ = "lau.wenbo"


import paramiko

class ssh_work:
    def __init__(self, hostname):
        self.hostname = hostname
        self.username = "root"
        self.password = "daemon"
        self.port = 22

    def ssh_work(self, command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)
        ssh.exec_command(command)
        ssh.close()


    def restart_es(self):
        es = self.ssh_work("systemctl restart elasticsearch")


    def restart_api_server(self):
        infi_api = self.ssh_work("systemctl restart infi-api")


    def install_infinity(self):
        insatll_infi = self.ssh_work("bash /root//install.sh")

    def unisntall_infinity(self):
        uninstall_infi = self.ssh_work("bash /root/uninstall.sh")

