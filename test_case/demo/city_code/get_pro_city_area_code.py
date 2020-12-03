#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/24
@File    : get_pro_city_area_code.py
"""

from common.log_color import LogingColor
from test_case.car_v2.data_cleaning.status_cleaning.online_sql import OnlineSql
from test_case.demo.city_code.read_json_file import DoData
online_db = OnlineSql()
log = LogingColor()


class GetProCityAreaCode:
    # 获取省份code
    def get_province_code(self, province_name):
        # 读取json文件
        json_file_data = DoData().get_data()
        # 遍历所有省份
        for i in json_file_data:
            # 判断城市是否在列表里面，如果在执行下面一条语句
            if province_name in str(i):
                # 取province后面的字段放入列表中
                temp_data = i['province']
                print(temp_data)
                # 遍历所有省的数据
                for pro_data in temp_data:
                    # 取出name，code里面的字段放入列表中
                    proName = pro_data['name']
                    proCode = pro_data['code']
                    # 如果找到关键字就返回code
                    if province_name == proName or province_name in proName:
                        return proCode

    # 获取城市code
    def get_city_code(self, city_name):
        # 读取json文件
        json_file_data = DoData().get_data()
        # 遍历所有省份
        for i in json_file_data:
            # 判断城市
            if city_name in str(i):
                temp_data = i['province'][0]['city']
                for city_data in temp_data:
                    cityName = city_data['name']
                    cityCode = city_data['code']
                    if city_name == cityName or cityName in city_name:
                        return cityCode

    # 获取区code
    def get_area_code(self, area_name):
        # 读取json文件
        json_file_data = DoData().get_data()
        # 遍历所有省份
        for i in json_file_data:
            # 判断城市
            if area_name in str(i):
                temp_data = i['province'][0]['city'][0]['area']
                for area_data in temp_data:
                    areaName = area_data['name']
                    areaCode = area_data['code']
                    if area_name == areaName or areaName in area_name:
                        return areaCode


if __name__ == '__main__':
    province_name = "河南省"
    # city_name = "淮安市"
    # area_name = "瑶海区"
    res=GetProCityAreaCode().get_province_code(province_name)
    print(res)
    # res1=GetProCityAreaCode().get_city_code(city_name)
    # print(res1)
    # res2 = GetProCityAreaCode().get_area_code(area_name)
    # print(res2)
