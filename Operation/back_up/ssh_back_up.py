# coding: utf-8
__author__ = 'lau.wenbo'


from multiprocessing import Pool
import ssh


def back_up_service(hostname,user,password,send_node):
    z = ssh.ssh_work(hostname,user,password)
    z.back_up(hostname)
    z.send_file_node(hostname, send_node)


def back_pack_service(send_node, user, password, ips):
     z = ssh.ssh_work(send_node, user, password)
     z.backpack()
     z.write_config(ips)


def cover_up(node, user, password):
    z = ssh.ssh_work(node, user, password)
    z.cover_up(node)


def etcd_back_up(node, user, password):
    z = ssh.ssh_work(node, user, password)
    z.etcd_back_up()


def etcd_cover_up(node, user, password):
    z = ssh.ssh_work(node, user, password)
    z.etcd_cover_up()



if __name__=='__main__':
    print("=============back_up==================")
    print("===========1.Node backup=================")
    print("===========2. Node recovery =================")
    print("===========3. ETCD backup =================")
    print("===========4.ETCD recovery=================")
    print("===========5.help=====================")
    print("=====================================")
    number = input("请输入命令序号：")
    if number == 1:
        ip_list = raw_input("Please enter the nodes to be backed up, separated by commas: ")
        ips = ip_list.split(",")
        user = raw_input(" Enter user name: ")
        password = raw_input(" Input password:  ")
        send_node = raw_input(" Input Sender Node： ")
        p = Pool(3)
        for i in ips:
            print("backup node：{hostname}".format(hostname=i))
            p.apply_async(back_up_service, args=(i, user, password, send_node))
        print('backup node end! success')
        p.close()
        p.join()
        print('All the node configuration files have been backed up... Begin to pack and transfer')
        back_pack_service(send_node, user, password, ip_list)
        print(" end of transmission ")
    elif number == 2:
        node = raw_input(" Please enter the node to be restored ： ")
        user = raw_input(" enter one user name : ")
        password = raw_input(" Input password : ")
        print(" Start restoring nodes ")
        cover_up(node,user,password)
        print(" Node Restoration Completed ")
    elif number == 3:
        node = raw_input(" Please enter the node to be backed up ： ")
        user = raw_input(" enter one user name : ")
        password = raw_input("Input password : ")
        print("Start backup ETCD")
        etcd_back_up(node, user, password)
        print("backup etcd end")
    elif number == 4:
        node = raw_input(" Please enter the node to be restored ： ")
        user = raw_input(" enter one user name : ")
        password = raw_input(" Input password : ")
        print(" Start restoring ETCD ")
        etcd_cover_up(node, user, password)
        print(" Completion of recovery ")
    else:
        exit()

