# coding: utf-8

__author__ = "lau.wenbo"

import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        # 建立连接，指定服务器的ip地址
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))

        # 建立一个会话，每个channel代表一个会话任务
        self.channel = self.connection.channel()

        # 声明回调队列，再次声明的原因是，服务器和客户端可能先后开启，该声明是幂等的，多次声明，但只生效一次
        result = self.channel.queue_declare(exclusive=True)
        # 将次队列指定为当前客户端的回调队列
        self.callback_queue = result.method.queue

        # 客户端订阅回调队列，当回调队列中有响应时，调用`on_response`方法对响应进行处理;
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    # 对回调队列中的响应进行处理的函数
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    # 发出RPC请求
    def call(self, n):

        # 初始化 response
        self.response = None

        # 生成correlation_id
        self.corr_id = str(uuid.uuid4())

        # 发送RPC请求内容到RPC请求队列`rpc_queue`，同时发送的还有`reply_to`和`correlation_id`
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(n))

        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


# 建立客户端
fibonacci_rpc = FibonacciRpcClient()

# 发送RPC请求
print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)