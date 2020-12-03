#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 17:30
# @Author  : lijian
# @File    : game_sum.py
# @Software: PyCharm
from common.log_color import LogingColor
from test_case.car_v2.data_cleaning.status_cleaning.dev_sql import DevSql

dev_db = DevSql()
logging = LogingColor()

begin_time = '2018-01-01 00:00:00'
end_time = '2020-11-20 16:00:00'


class DevOrderMoney:

    # 查询线上：订单分期金额
    # 查询补贴详情
    def quer_perk_details(self, order_sn):
        logging.info("——————————查询数据库——————————")
        sql = "select perk_details from `life_car_order` WHERE order_code in('%s')" % order_sn
        result = dev_db.query_sql('car-v2', sql)[0]
        if result[0] is not None:
            return result[0]
        else:
            return "数据查询不到"

    def quer_order_people(self, order_sn):
        logging.info("——————————查询数据库——————————")
        sql = "select province_code,city_code,name,id_number,phone,offers_type from `life_car_order` WHERE order_code in('%s')" % order_sn
        result = dev_db.query_sql('car-v2', sql)
        if result[0] is not None:
            return result
        else:
            return "数据查询不到"
