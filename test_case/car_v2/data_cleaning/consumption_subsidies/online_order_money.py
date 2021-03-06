#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 17:30
# @Author  : lijian
# @File    : game_sum.py
# @Software: PyCharm
from common.log_color import LogingColor
from test_case.car_v2.data_cleaning.status_cleaning.online_sql import OnlineSql

online_db = OnlineSql()
logging = LogingColor()

begin_time = '2018-01-01 00:00:00'
end_time = '2020-11-23 14:00:00'


class OnlineOrder:
    # 随机获取订单id
    def rand_order_id(cls):
        # SELECT MAX(id) FROM life_car_contract_installment获取最大的id值
        # SELECT RAND() * (SELECT MAX(id) FROM life_car_contract_installment) 在1-MAX(id) 区间内随机取一个id
        # 当使用 >= 而不是a = 时，我们可以摆脱CEIL并以更少的工作获得相同的结果。
        sql = "SELECT order_id FROM life_car_contract_installment t1 JOIN (SELECT RAND() * (SELECT MAX(id) FROM life_car_contract_installment) AS nid) t2 ON t1.id > t2.nid LIMIT 1"
        sql_data = online_db.query_sql('car', sql)[0]
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        else:
            logging.info("随机获取的订单id为：" + str(sql_data[0]))
            return sql_data[0]

    # 查询线上：订单分期金额
    def query_bill_amount(self, order_id):
        sql = "SELECT bill_amount from life_car_installment_repayments WHERE order_id ='%s' " % (
            order_id)
        sql_data = online_db.query_sql('car', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == 0:
            return sql_data
        elif len(sql_data) > 1:
            return sql_data
        else:
            return sql_data[0]

    # 查询线上：账单日期
    def query_bill_data(self, order_id):
        sql = "SELECT bill_date from life_car_installment_repayments WHERE order_id ='%s' " % (
            order_id)
        sql_data = online_db.query_sql('car', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == 0:
            return sql_data
        elif len(sql_data) > 1:
            return sql_data
        else:
            return sql_data[0]

    # 查询线上：已还款账单日期总数
    def query_over_bill(self, order_id):
        sql = "SELECT COUNT(id) from life_car_installment_repayments WHERE order_id ='%s' and `status`='2' " % (
            order_id)
        sql_data = online_db.query_sql('car', sql)[0]
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        else:
            return sql_data[0]

    # 查询线上：已还款账单日期
    def query_over_bill_data(self, order_id):
        sql = "SELECT bill_date from life_car_installment_repayments WHERE order_id ='%s' and `status`='2' " % (
            order_id)
        sql_data = online_db.query_sql('car', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        else:
            return sql_data
    # 获取订单号
    def query_order_no(cls, order_id):
        sql = "SELECT ordersn from life_car_orders WHERE id ='%s' " % (order_id)
        sql_data = online_db.query_sql('car', sql)[0]
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == 0:
            logging.error("根据订单id，查询不到数据")
            return sql_data
        else:
            logging.info("订单号ordersn：" + sql_data[0])
            return sql_data[0]
   # 获取订单号
    def query_order_people(cls, order_no):
        sql = "SELECT area_name,user_name,user_id_card,user_contact,order_type from life_car_orders WHERE ordersn ='%s' " % (order_no)
        sql_data = online_db.query_sql('car', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == 0:
            logging.error("根据订单id，查询不到数据")
            return sql_data
        else:
            return sql_data