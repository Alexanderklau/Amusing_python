# coding: utf-8

__author__ = 'lau.wenbo'


class ssh_work:
    def __init__(self, hostname, username, daemon):
        self.hostname = hostname
        self.username = username
        self.password = daemon
        self.port = 22

    def ssh_work(self, command):
        import paramiko
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)
        stdin, stdout, stderr = ssh.exec_command(command)
        print stderr.read()
        ssh.close()


    def install(self):
        z = "tar -zxvf /root/back/back_up.tar.gz"
        back_up = self.ssh_work(z)
        print back_up

    def transmission(self, node):
        z = "scp -r back_up root@{node}:/root".format(node=node)
        transmission = self.ssh_work(z)
        print(transmission)


if __name__=='__main__':
    ip = raw_input(" Enter the current hostaname :")
    send_ip = raw_input(" Enter the hotsname to install, separated by commas: ")
    ips = send_ip.split(",")
    user = raw_input(" enter one user name: ")
    password = raw_input(" Input password: ")
    z = ssh_work(ip, user, password)
    z.install()
    for i in ips:
        z.transmission(i)

