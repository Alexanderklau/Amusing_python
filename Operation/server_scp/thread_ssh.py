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
    ip_list = ['10.0.7.31','10.0.7.45','10.0.7.65','10.0.7.68','10.0.7.78']
    # ip_list = ['10.0.7.11','10.0.7.12','10.0.7.13',"10.0.7.18","10.0.7.20","10.0.7.24","10.0.7.25","10.0.7.26","10.0.7.27","10.0.7.28","10.0.7.29","10.0.7.30",
    #            "10.0.7.31","10.0.7.32","10.0.7.33","10.0.7.37","10.0.7.38","10.0.7.40","10.0.7.41"]
    print('Parent process %s.' % os.getpid())
    p = Pool(3)
    for i in ip_list:
        print(i)
        p.apply_async(service, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')