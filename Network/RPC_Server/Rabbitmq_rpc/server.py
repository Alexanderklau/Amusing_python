# coding: utf-8

__author__ = "lau.wenbo"

import pika

# 建立连接，服务器地址为localhost，可指定ip地址
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='127.0.0.1'))

# 建立会话
channel = connection.channel()

# 声明RPC请求队列
channel.queue_declare(queue='rpc_queue')


# 数据处理方法
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 对RPC请求队列中的请求进行处理
def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)

    # 调用数据处理方法
    response = fib(n)

    # 将处理结果(响应)发送到回调队列
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 负载均衡，同一时刻发送给该服务器的请求不超过一个
channel.basic_qos(prefetch_count=1)

