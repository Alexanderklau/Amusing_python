# coding: utf-8

__author__ = 'lau.wenbo'

import paramiko
import threading
import subprocess


def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active():
        ssh_session.exec_command(command)
        print(ssh_session.revc(1024))
    return


ssh_command('10.0.20.192', "root", "daemon", "ls")

