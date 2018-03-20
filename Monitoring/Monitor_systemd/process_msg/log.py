# coding: utf-8
__author__ = 'lau.wenbo'


import logging
from logging.handlers import TimedRotatingFileHandler
import time
import re


rq = time.strftime('%Y%m%d', time.localtime(time.time()))


class Log(object):
      '''日志类 '''
      def __init__(self, name):
            self.path = "/var/log/infinity/process/"  # 定义日志存放路径
            self.filename = self.path + rq + "_process_memory" + ".log"    # 日志文件名称
            self.name = name    # 为%(name)s赋值
            self.logger = logging.getLogger(self.name)
            # 控制日志文件中记录级别
            self.logger.setLevel(logging.INFO)
            # 控制输出到控制台日志格式、级别
            # self.ch = logging.StreamHandler()
            # 日志保留7天,一天保存一个文件
            self.fh = TimedRotatingFileHandler(self.filename, when='D', interval=1, backupCount=7)
            # 删除设置
            self.fh.suffix = '%Y-%m-%d_%H-%M.log'
            self.fh.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
            # 定义日志文件中格式
            self.formatter = logging.Formatter('%(asctime)s - %(levelname)s -   %(name)s[line:%(lineno)d] - %(message)s')
            self.fh.setFormatter(self.formatter)
            self.logger.addHandler(self.fh)

      def info(self, msg):
          self.logger.info(msg)

      def warning(self, msg):
          self.logger.warning(msg)

      def error(self, msg):
          self.logger.error(msg)

      def debug(self, msg):
          self.logger.debug(msg)

      def close(self):
          self.logger.removeHandler(self.fh)

class customError(Exception):
    def __init__(self, msg=None):
        self.msg = msg
    def __str__(self):
        if self.msg:
            return self.msg
        else:
            return "某个不符合条件的语法出问题了"
