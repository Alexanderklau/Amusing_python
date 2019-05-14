# coding: utf-8
__author__ = 'lau.wenbo'


from multiprocessing import Pool
import os
import ssh

def service(ip):
    z = ssh.ssh_work(ip)
    # z.status_es()
    z.install_infinity()
    # z.unisntall_infinity()
    # z.install_infinity()
    # z.restart_es()
    # z.restart_api_server()
if __name__=='__main__':

    # ip_list = ["10.0.7.31","10.0.7.45","10.0.7.78","10.0.7.82","10.0.7.85"]
    # ip_list = ["10.0.7.31","10.0.7.45","10.0.7.65","10.0.7.68","10.0.7.78"]
    # ip_list = ['10.0.30.17','10.0.30.18','10.0.30.19']
    ip_list = ['10.0.6.251','10.0.6.252','10.0.6.253']
    print('Parent process %s.' % os.getpid())
    p = Pool(3)
    for i in ip_list:
        print(i)
        p.apply_async(service, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')