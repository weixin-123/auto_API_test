#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/24
@File    : online_order.py
"""
from common.log_color import LogingColor
from test_case.car_v2.data_cleaning.status_cleaning.online_sql import OnlineSql

online_db = OnlineSql()
logging = LogingColor()


class OnlineArea:

    # 查询线上：随机获取ordersn
    def query_online_ordersn(self):
        sql = "SELECT ordersn from life_car_orders t1 JOIN " \
              "(SELECT RAND() * (SELECT MAX(id) FROM life_car_contract_installment) AS nid) t2 " \
              "ON t1.id > t2.nid LIMIT 1"
        sql_data = online_db.query_sql('car', sql)[0]
        if sql_data is not None:
            return sql_data[0]
        else:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")

    # 查询线上：随机获取area_name
    def query_online_province(self, ordersn):
        # 记住%s要用单引号引起来
        sql = "SELECT area_name from life_car_orders where ordersn = '%s'" % ordersn
        sql_data = online_db.query_sql('car', sql)
        if sql_data is not None:
            return sql_data
        else:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")

    # def data_fractionation(self):
    #



if __name__ == '__main__':
    OnlineArea().query_online_province(OnlineArea().query_online_ordersn())
