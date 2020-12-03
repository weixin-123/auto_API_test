#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/09/24
@File    : logs.py
"""
import logging
# 按时间自动更换,保证日志单个文件不会太大
from logging.handlers import TimedRotatingFileHandler


class MyLog:
    @classmethod
    def url_replace(cls, path):
        """

        :param path: 路径替换
        :return:
        """
        # 将测试用例的路径替换成同层级下的excel表路径
        file_url = path.replace("test_case", "test_case_excel").replace(".py", ".xlsx")
        return file_url

    def my_log(self, msg, level):
        # 定义一个自己的日志收集器
        my_logger = logging.getLogger('test')
        # 设定级别
        my_logger.setLevel('DEBUG')
        # 设置输出格式
        formatter = logging.Formatter("%(asctime)s-%(levelname)s-[%(filename)s-->line:%(lineno)d] - 日志信息：- %(levelname)s: %(message)s")
        # 创建自己的输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('ERROR')
        ch.setFormatter(formatter)

        # 按天进行记录
        fh = TimedRotatingFileHandler("日志文件.txt", when='d',
                                      interval=1, backupCount=7,
                                      encoding="utf-8")
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)
        # 两者对接---指定输出渠道
        # 控制台
        my_logger.addHandler(ch)
        # 日志文件
        my_logger.addHandler(fh)

        # 收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        if level == 'CRITICAL':
            my_logger.critical(msg)

        # 关闭渠道，不关闭的话会日志重复
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')


if __name__ == '__main__':
    My_logger = MyLog()
    My_logger.debug('今天有点冷啊')
    My_logger.error('快乐哦')
    My_logger.critical('啦啦哦')

