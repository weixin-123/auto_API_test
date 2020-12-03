#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 15:45
# @Author  : lijian
# @File    : test_wash_car_data.py
# @Software: PyCharm
import unittest

from test_case.car_v2.data_cleaning.status_cleaning.dev_car_data import DevCarData
from test_case.car_v2.data_cleaning.status_cleaning.online_car_data import OnlineCarData

online_data = OnlineCarData()
dev_data = DevCarData()


class TestWashCarData(unittest.TestCase):

    def quer_data(self):
        # 查询指定时间内的订单数目
        online_data.query_online_count()
        # 汽车1.0
        # 订单状态：1待付定金 2待服务 3服务中 4已完成 5支付中 -1用户取消（未付定金）-2待退定金 -3已退定金 -4已关闭
        # 订单类型：1补贴购 2全返购
        # 汽车2.0
        # 订单状态(-10关闭订单 0未支付 5已支付 10车辆信息核实 15订单信息录入 20事业部审核 25补贴 30完成 )
        # 订单类型：1消费补贴 2积分补贴
        pass

    def test_assert_data(self):
        # 校验订单总数
        online_count = online_data.query_online_count()
        dev_count = dev_data.query_dev_count()
        self.assertEqual(online_count, dev_count)
        print("订单总数：", dev_count)
        # 校验订单类型：1补贴购
        online_type_one = online_data.query_online_type(1)
        dev_type_one = dev_data.query_dev_type(1)
        self.assertEqual(online_type_one, dev_type_one)
        print("消费补贴：", online_type_one)
        # 校验订单类型：2全返购、积分补贴
        online_type_two = online_data.query_online_type(2)
        dev_type_two = dev_data.query_dev_type(2)
        self.assertEqual(online_type_two, dev_type_two)
        print("全赠积分：", online_type_two)
        # 校验订单状态：1待付定金、0未支付
        online_status_one = online_data.query_online_status(1)  # 待付定金
        online_status_5 = online_data.query_online_status(5)  # 支付中
        online_status_2 = online_data.query_online_status(-2)   # 待退定金
        online_status_3 = online_data.query_online_status(-3)   # 已退定金
        # 求和
        temp_sum_data = online_status_one + online_status_5 + online_status_2 + online_status_3
        dev_status_one = dev_data.query_dev_status(0)   # 未支付
        # self.assertEqual(temp_sum_data, dev_status_one)
        print("未支付订单：", temp_sum_data)
        # 校验订单状态：2待服务、10车辆信息核实
        online_status_two = online_data.query_online_status(2)  # 待服务
        dev_status_two = dev_data.query_dev_status(10)  # 车辆信息核实
        # self.assertEqual(online_status_two, dev_status_two)
        print("车辆信息待核实：", online_status_two)
        # 校验订单状态：3服务中、20事业部审核
        online_status_three = online_data.query_online_status(3)
        dev_status_three = dev_data.query_dev_status(20)
        self.assertEqual(online_status_three, dev_status_three)
        print("事业部审核：", online_status_three)
        # 校验订单状态：4已完成、25补贴中、
        online_status_four = online_data.query_online_status(4)
        dev_status_four = dev_data.query_dev_status(25)
        print("补贴中：", online_status_four)
        # 积分补贴 30已完成
        dev_status_tyepe1 = dev_data.query_dev_status_tyepe(30)
        self.assertEqual(online_status_four, dev_status_four + dev_status_tyepe1)
        print("全赠积分订单已完成：", dev_status_tyepe1)
        # 5支付中_____这种情况没得，属于未支付
        # -1用户取消（未付定金）属于未支付
        # 校验订单状态：-2待退定金、1待退款
        online_refound_status = online_data.query_online_status(-2)
        dev_refound_status = dev_data.query_dev_restatus(1)
        self.assertEqual(online_refound_status, dev_refound_status)
        # 校验订单状态：退款完成
        online_refound_status = online_data.query_online_restatus(4)
        dev_refound_status = dev_data.query_dev_refound(4)
        self.assertEqual(online_refound_status, dev_refound_status)
        print("退款订单完成：", online_refound_status)

        # 校验订单状态：-1用户取消 -4已关闭——————   -10关闭订单
        online_refound_status2 = online_data.query_online_status(-4)
        online_status_fuone = online_data.query_online_status(-1)
        # 求和
        temp_sum_data1 = online_refound_status2 + online_status_fuone
        dev_refound_status2 = dev_data.query_dev_status(-10)
        self.assertEqual(temp_sum_data1, dev_refound_status2)
        print("订单关闭：", temp_sum_data1)


# 订单状态：1待付定金 2待服务 3服务中 4已完成 5支付中 -1用户取消（未付定金）-2待退定金 -3已退定金 -4已关闭
# 新订单状态(-10关闭订单 0未支付 5已支付 10车辆信息核实 15订单信息录入 20事业部审核 25补贴 30完成 )
# 售后状态:-2售后关闭,-1已驳回,1待退款,2退款中,3退款完成
if __name__ == '__main__':
    TestWashCarData().test_assert_data()
