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


class DevCarData:

    # 查询dev：未删除的汽车订单所有状态数量
    def query_dev_count(self):
        sql = "SELECT COUNT(id) from life_car_order WHERE created_at between '%s' and '%s'" % (begin_time, end_time)
        sql_data = dev_db.query_sql('car-v2', sql)[0]
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == 0:
            return sql_data
        else:
            return sql_data[0]

    # 查询dev：`offers_type` '订单类型：1补贴购 2全返购'
    def query_dev_type(self, offers_type):
        sql_type_one = "SELECT COUNT(id) from life_car_order WHERE offers_type ='%s' AND created_at between '%s' and '%s'" % (
            offers_type,
            begin_time,
            end_time)
        sql_data = dev_db.query_sql('car-v2', sql_type_one)[0]

        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == 0:
            return sql_data
        else:
            return sql_data[0]

    # 订单状态(-10关闭订单 0未支付 5已支付 10车辆信息核实 15订单信息录入 20事业部审核 25补贴 30完成 )
    def query_dev_status(self, status):
        sql_status = "SELECT COUNT(id) from life_car_order WHERE `status` ='%s' AND created_at between '%s' and '%s'" % (
            status, begin_time, end_time)
        dev_status = dev_db.query_sql('car-v2', sql_status)[0]

        if dev_status == "" or dev_status is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif dev_status == 0:
            return dev_status
        else:
            return dev_status[0]
        # 订单状态(-10关闭订单 0未支付 5已支付 10车辆信息核实 15订单信息录入 20事业部审核 25补贴 30完成 )

    def query_dev_status_tyepe(self, status):
        sql_status = "SELECT COUNT(id) from life_car_order WHERE `status` ='%s' AND offers_type='2' AND created_at between '%s' and '%s'" % (
            status, begin_time, end_time)
        dev_status = dev_db.query_sql('car-v2', sql_status)[0]

        if dev_status == "" or dev_status is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif dev_status == 0:
            return dev_status
        else:
            return dev_status[0]

    # 售后状态:-2售后关闭,-1已驳回,1待退款,2退款中,3退款完成
    def query_dev_restatus(self, refund_status):
        sql_status = "SELECT COUNT(id) from life_car_order WHERE refund_status ='%s' AND created_at between '%s' and '%s'" % (
        refund_status, begin_time, end_time)
        dev_status = dev_db.query_sql('car-v2', sql_status)[0]

        if dev_status == "" or dev_status is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif dev_status == 0:
            return dev_status
        else:
            return dev_status[0]

    def query_dev_refound(self, refund_status):
        sql_status = "SELECT COUNT(id) from life_car_order_refund WHERE status ='%s' AND created_at IS NULL" % (
            refund_status)
        dev_status = dev_db.query_sql('car-v2', sql_status)[0]

        if dev_status == "" or dev_status is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif dev_status == 0:
            return dev_status
        else:
            return dev_status[0]

    # 订单状态+优惠类型
    def query_dev_order_type_status(self, status, order_type):
        sql = "SELECT COUNT(id) from life_car_order WHERE `status` ='%s' AND order_type ='%s' AND created_at between '%s' and '%s'" % (
            status, order_type, begin_time, end_time)
        sql_data = dev_db.query_sql('car-v2', sql)[0]

        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        elif sql_data == 0:
            return sql_data
        else:
            return sql_data[0]
