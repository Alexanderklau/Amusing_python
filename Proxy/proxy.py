#coding:utf-8
from socket import *


# 创建socket，绑定到端口，开始监听
tcpSerPort = 8899
tcpSerSock = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
tcpSerSock.bind(('', tcpSerPort))
tcpSerSock.listen(5)

while True:
    # 开始从客户端接收请求
    print 'Ready to serve...'
    tcpCliSock, addr = tcpSerSock.accept()
    print 'Received a connection from: ', addr
    message = tcpCliSock.recv(4096)

    # 从请求中解析出filename
    print message.split()[1]
    filename = message.split()[1].partition("/")[2]
    fileExist = "false"
    filetouse = "/" + filename
    try:
        # 检查缓存中是否存在该文件
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        print 'File Exists!'

        # 缓存中存在该文件，把它向客户端发送
        tcpCliSock.send("HTTP/1.0 200 OK\r\n\r\n")

        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i])
        print 'Read from cache'

        # 缓存中不存在该文件，异常处理
    except IOError:
        print 'File Exist: ', fileExist
        if fileExist == "false":
            # 在代理服务器上创建一个tcp socket
            print 'Creating socket on proxyserver'
            c = socket(AF_INET, SOCK_STREAM)

            hostn = filename.replace("www.", "", 1)
            print 'Host Name: ', hostn
            try:
                # 连接到远程服务器80端口
                c.connect((hostn, 80))
                print 'Socket connected to port 80 of the host'

                # 在代理服务器上缓存请求的文件
                fileobj = c.makefile('r', 0)
                #拼凑http get请求的请求行。注意格式为： "请求方法 URI HTTP版本"，空格不能省略!
                fileobj.write("GET " + "http://" + filename + " HTTP/1.0\n\n")

                # Read the response into buffer
                buff = fileobj.readlines()

                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket
                # and the corresponding file in the cache
                tmpFile = open("./" + filename,"wb")
                for i in range(0, len(buff)):
                    tmpFile.write(buff[i])
                    tcpCliSock.send(buff[i])

            except:
                print "Illegal request"

        else:
            # HTTP response message for file not found
            # Do stuff here
            print 'File Not Found...Stupid Andy'
            a = 2
    # Close the client and the server sockets
    tcpCliSock.close()
# Fill in start.
tcpSerSock.close()