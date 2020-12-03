#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/09/23
@File    : project_path.py
"""
import os
from datetime import datetime

'''专门来读取路径的值'''
# 项目所在文件夹
folder_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# print(pro_dir)

# 切换到顶级目录
project_path_root = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path_root)

# 获取当前文件目录的绝对路径
current_dir = os.path.abspath(os.path.dirname(__file__))
# print(current_dir)

# 获取测试用例的路径
test_case_path = os.path.join(project_path_root, 'test_case')
# print(test_case_path)

# 测试报告的路径
test_report_path = os.path.join(project_path_root, 'result', 'reports', str(datetime.now().strftime("%Y%m%d")))
# print(test_report_path)

# 配置文件的路径
base_config_path = os.path.join(project_path_root, 'base_config.ini')
user_config_path = os.path.join(project_path_root, 'user_config_bak.ini')
# print(config_path)
# 日志目录的项目路径
logs_path = os.path.join(project_path_root, 'result', 'logs')
# print(logs_path)
# 获取当前子文件的绝对路径
a = os.path.abspath(__file__)
# print(a)