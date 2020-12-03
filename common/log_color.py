#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 10:45
# @Author  : lijian
# @File    : log_color.py
# @Software: PyCharm
import logging

fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO,format=fmt,filename='',filemode='w',datefmt='%a, %d %b %Y %H:%M:%S')


class LogingColor():
    #信息打印——黑色
    def info(self, message):
        logging.info('\033[0;20m%s\033[0m', message)

    # 调试等级——紫色
    def debug(self, message):
        logging.debug('\033[0;35m%s\033[0m', message)

    # 警告等级——深蓝色
    def warning(self, message):
        logging.warning('\033[0;34m%s\033[0m', message)

    # 错误等级——红色
    def error(self, message):
        logging.error('\033[0;31m%s\033[0m', message)

    # 重要提示——黄色
    def critical(self, message):
        logging.critical('\033[0;33m%s\033[0m', message)


if __name__ == '__main__':
    My_logger = LogingColor()
    My_logger.debug('今天有点冷啊')
    My_logger.error('快乐哦')
    My_logger.critical('啦啦哦')
    My_logger.info('啦啦哦')
