#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/10/15
@File    : read_base_config.py
"""
import configparser
from common.project_path import base_config_path


class ReadBaseConfig:
    def __init__(self):
        # 实例化一个对象
        self.cf = configparser.ConfigParser()
        # 选取.ini文件
        self.cf.read(base_config_path, encoding='utf-8')
        # # 打印出配置文件的sections
        # print(self.cf.sections())

    def get_data(self, config_title, config_name):
        """
        :param config_title:
        :param config_name:
        :return:
        """
        if type(config_name) == str and type(config_title) == str:
            value = self.cf.get(str(config_title), config_name)
            return value
        else:
            raise TypeError("传入参数类型不正确")


if __name__ == '__main__':
    pass
