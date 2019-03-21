# coding: utf-8
__author__ = 'lau.wenbo'


from multiprocessing import Pool
import os
import ssh

def service(ip):
    z = ssh.ssh_work(ip)
    z.restart_es()
    z.restart_api_server()

if __name__=='__main__':
    ip_list = ["10.0.6.244","10.0.6.245","10.0.6.246"]
    print('Parent process %s.' % os.getpid())
    p = Pool(2)
    for i in ip_list:
        print(i)
        p.apply_async(service, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')