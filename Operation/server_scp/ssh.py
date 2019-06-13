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
        stdin,stdout,stderr = ssh.exec_command(command)
        for i in stdout.readlines():
            print(i)
        ssh.close()

    def status_es(self):
        es = self.ssh_work("systemctl stop elasticsearch")

    def rm_es(self):
        es = self.ssh_work("systemctl stop elasticsearch && rm -rf /etc/elasticsearch/es_node.yml && rm -rf /etc/elasticsearch/elasticsearch.yml && rm -rf /var/lib/elasticsearch/*")
        return es


    def restart_api_server(self):
        infi_api = self.ssh_work("systemctl restart infi-api")


    def install_infinity(self):
        insatll_infi = self.ssh_work("bash /root/infinity-3.3.0/install.sh")

    def unisntall_infinity(self):
        uninstall_infi = self.ssh_work("bash /root/uninstall.sh")

    def clear_rabitmq(self):
        clear_infi = self.ssh_work("python /opt/infinity/python/apps/misc/rabbitmq/rabbitmq_utils.py")

    def back_up_Es_node_yml(self):
        back_up = self.ssh_work("rm -rf /etc/elasticsearch/es_node.yml && mv /etc/elasticsearch/.es_node.yml /etc/elasticsearch/es_node.yml")





