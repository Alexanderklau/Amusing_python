# coding: utf-8

__author__ = "lau.wenbo"


import paramiko
import os


HOST_IP = "10.0.6.214"
REMOTE_PATH = '/home'
REMOTE_FILENAME = 'lwb'
LOCAL_PATH  = './proc'
USERNAME = 'root'
PASSWORD = '123456'



def remote_scp(host_ip, remote_path, local_path, file_name, username, password):
    t = paramiko.Transport(host_ip, 22)
    # 登陆远程服务器
    t.connect(username=username, password=password)
    # sftp传输协议
    sftp = paramiko.SFTPClient.from_transport(t)
    src = remote_path + '/' + file_name
    des = local_path + '/' + file_name
    sftp.get(src, des)
    t.close()



    if not os.path.isdir(LOCAL_PATH):
        os.makedirs(LOCAL_PATH)

    if not os.path.isfile(LOCAL_PATH + '/' + REMOTE_FILENAME):
        fp = open(LOCAL_PATH + '/' + REMOTE_FILENAME, 'w')
        fp.close()


if __name__ == "__main__":
    remote_scp(HOST_IP,REMOTE_PATH,LOCAL_PATH,REMOTE_FILENAME,USERNAME,PASSWORD)