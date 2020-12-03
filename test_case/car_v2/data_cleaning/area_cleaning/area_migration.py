#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/24
@File    : area_migration.py
"""
from common.log_color import LogingColor

from test_case.car_v2.data_cleaning.area_cleaning.read_json_file import DoData
from test_case.car_v2.data_cleaning.status_cleaning.online_sql import OnlineSql

online_db = OnlineSql()
log = LogingColor()


str_list = DoData().area_name_migration()


class AreaMigration:


    def area_cleanning(self):
        # 取第一条字母的数据
        # one = DoData().get_data()[0]
        # print(one)
        # # 取第一条数据下面的省
        # two = DoData().get_data()[0]['province'][0]
        # print(two)
        # # 取第一条数据下面的城市
        # three = DoData().get_data()[0]['province'][0]['city'][0]
        # print(three)

        temp_data_list = []
        # 遍历所有字母
        letter_total = len(DoData().get_data())
        for i in range(letter_total - 1):
            # 遍历字母,从A开始
            letter_list = DoData().get_data()[i]
            # 计算字母下面省的总数
            province_total = len(letter_list)
            # 遍历所有省
            for j in range(province_total - 1):
                # province = DoData().get_data()[0]['province'][0]
                # print("市总数：", len(DoData().get_data()[0]['province'][0]['city']))
                # 遍历所有省
                province_list = letter_list['province'][j]

                city_total = len(province_list['city'])
                for k in range(city_total - 1):
                    city_name = province_list['city'][k]['name']
                    city_code = province_list['city'][k]['code']
                    province_name = province_list['name']
                    province_code = province_list['code']
                    # # {"province": {"name": "澳门特别行政区", "code": "820000"}, "city": {"name": "风顺堂区", "code": "820005"}}
                    temp_car_data = {"province": {"province_name": province_name, 'province_code': province_code},
                                     "city": {"city_name": city_name, "city_code": city_code}}
                    temp_data_list.append(temp_car_data)
        return temp_data_list

    def province_migration(self):
        online_province = str_list[0]
        temp_data_list = AreaMigration().area_cleanning()
        for i in temp_data_list:
            # 判断城市
            # print(i)
            if online_province in str(i):
                return i

    # 判断省是否存在
    def province_check(self):
        data = AreaMigration().province_migration()
        if data is None:
            print("省市不存在")
        else:
            online_city = str_list[1]
            temp_data_list = AreaMigration().area_cleanning()
            for i in temp_data_list:
                # 判断城市
                if online_city in str(i):
                    return i

    def city_check(self):
        data = AreaMigration().province_check()
        if data is None:
            print("城市不存在")
        else:
            print(data)


if __name__ == '__main__':
    AreaMigration().city_check()
