# coding: utf-8
__author__ = 'Yemilice_lau'


import paramiko

def info():
    hostname = '10.1.101.186'
    username = 'root'
    password = '123456'
    port = 22

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command("cd  /root/paramiko;mkdir lxy")
    print stdout.readlines()
    ssh.close()

def install():
    commands = ("bash ./install.sh")