# !/use/bin/env python
# -*- coding:utf-8 -*-

"""
@author:lijian
@describe:
@time:2019/6/13 17:18
"""
import datetime
import time


class TimeChange:

    # 获取当前服务器时间，变化天数(返回时间2019-01-02 00:00:00)
    def change_day_time(self, days):
        # 获取数据库服务器当前时间
        now_time = datetime.datetime.now()
        temp_time = now_time + datetime.timedelta(days=days)
        return temp_time.strftime('%Y-%m-%d %T')

    # 获取当前服务器时间，变化天数(返回时间2019-01-02)
    def change_day_time_format(self, days):
        now_time = datetime.datetime.now()
        temp_time = now_time + datetime.timedelta(days=days)
        return temp_time.strftime('%Y-%m-%d')

    # 传入时间，加减天数(返回时间2019-01-02 00:00:00)
    def get_day_time_format(self, data_time, days):
        temp_time = data_time + datetime.timedelta(days=days)
        return temp_time.strftime('%Y-%m-%d 00:00:00')

    # 传入时间，加减天数(返回时间2019-01-02 10:01:01)
    def get_day_time(self, data_time, days):
        temp_time = data_time + datetime.timedelta(days=days)
        return temp_time.strftime('%Y-%m-%d %T')

    # 传入时间戳，(解密返回格式：2019-01-02 00:00:00)
    def time_decode(self, data_time):
        dateArray = datetime.datetime.fromtimestamp(data_time)
        otherStyleTime = dateArray.strftime("%Y-%m-%d %T")
        return otherStyleTime

    # 传入时间(格式：2019-01-02 00:00:00)，转换为时间戳int型
    def time_code(self, data_time):
        # 将字符串转换为标准时间结构
        now = time.strptime(data_time, "%Y-%m-%d %H:%M:%S")
        # 转换为时间戳int型
        temp_time = int(time.mktime(now))
        return temp_time
