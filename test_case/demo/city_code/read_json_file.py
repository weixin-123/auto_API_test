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

class DoData:
    def get_data(self):
        filename =config_path
        with open(filename) as f:
            area_list = json.load(f)
        data = []
        for area_dict in area_list:
            data.append(area_dict)
        return data

if __name__ == '__main__':
    # data=DoData().get_data()
    print(current_dir)
    print(config_path)
