# coding: utf-8
__author__ = 'lau.wenbo'

import paramiko

hostname = 'node2'
username = 'root'
password = 'daemon'
port = 22
name='infinity-install'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,port=port,username=username,password=password)
stdin, stdout, stderr = ssh.exec_command("cd  /root/infinity-install/infinity.boreas; ./uninstall.sh")

"""
实时打印输出信息，copy的，这个很有参考价值
"""
def line_buffered(f):
    line_buf = ""
    while not f.channel.exit_status_ready():
        line_buf += f.read(1)
        if line_buf.endswith('\n'):
            yield line_buf
            line_buf = ''

for l in line_buffered(stdout):
    print l

ssh.close()