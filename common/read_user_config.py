#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/09/23
@File    : read_user_config.py
"""
import os
import configparser

from common.project_path import base_config_path,user_config_path,project_path_root

# 以配置的方式读取文件
cf_1 = configparser.ConfigParser()
cf_1.read(base_config_path, encoding="utf-8")

# 获取配置内容
configuration_file = cf_1.get("configuration", "configuration_file")

# 判断使用哪份配置文件（目的是）
if configuration_file == "user_config.ini":
    file_name = "user_config.ini"
    print("正在使用[user_config.ini]配置文件\n")
else:
    # 新建user_config_bak.ini的目的是一种身份识别，在执行操作时，会做一些数据替换，比如电话号码，这时候为了避免和他人的冲突替换，
    # 因此需要复制一个与user_config.ini文件内容一致的信息
    file_name = "user_config_bak.ini"
    print("正在使用[user_config_bak.ini]配置文件\n")
# 最终配置文件路径
config_path = os.path.join(project_path_root, file_name)
print(config_path)

class ReadUserConfig:
    def __init__(self):
        # 实例化一个对象
        self.cf = configparser.ConfigParser()
        # 选取.ini文件
        self.cf.read(user_config_path, encoding="utf-8")
        # # 打印出配置文件的sections
        # print(self.cf.sections())

    def get_header_token(self, service):
        """
        :tips  这个方法在common.Request有用到不需要更改
        :param service: APP或者管理台的配置文件
        :return:
        """
        value = self.cf.get(service, "token")
        return value

    def set_login_info(self, service_name, name, value):
        """
        修改配置表中对应登录的key对应的value值
        :param service_name: user_config[app][admin][store_app][store_admin]
        :param name: 需要的字段
        :param value:值
        :return:
        """
        self.cf.set(str(service_name), name, value)
        try:
            with open(config_path, 'w+') as f:
                self.cf.write(f)
        except IOError:
            raise (file_name + "下无" + str(service_name) + "配置，或者设置失败！")


if __name__ == "__main__":
    t = ReadUserConfig().get_header_token('admin')
    print(t)
