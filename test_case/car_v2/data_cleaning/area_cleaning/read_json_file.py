#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/24
@File    : read_json_file.py
"""
import json
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(current_dir, "area.json")

from test_case.car_v2.data_cleaning.area_cleaning.online_area import OnlineArea


class DoData:
    """
    读取json文件数据
    """

    def get_data(self):
        filename = config_path
        with open(filename) as f:
            area_list = json.load(f)
        data = []
        for area_dict in area_list:
            data.append(area_dict)
        return data

    """
    线上area_name数据拆分
    """

    def area_name_migration(self):
        online_area = OnlineArea().query_online_province(OnlineArea().query_online_ordersn())[0][0]
        print(online_area)
        str_list = online_area.split(" ")

        return str_list


if __name__ == '__main__':
    DoData().get_data()
