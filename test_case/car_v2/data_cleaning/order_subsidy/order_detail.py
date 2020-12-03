#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/26
@File    : order_detail.py
"""
import unittest
import datetime
from test_case.car_v2.data_cleaning.order_subsidy.dev_order import DevOrderData
from test_case.car_v2.data_cleaning.order_subsidy.online_order import OnlineOrderData


class OrderSubsidy(unittest.TestCase):

    def test_assert_data(self):
        # 随机获取还款人id
        # online_repay_member_id = OnlineOrderData().query_online_repay_member_id()
        online_repay_member_id = 1066309
        dev_data = DevOrderData().dev_order(online_repay_member_id)
        online_data = OnlineOrderData().query_online_order_detail(online_repay_member_id)
        total = len(online_data)
        print(total)
        # 获取订单号
        online_order_id = OnlineOrderData().query_online_order_id(online_repay_member_id)

        # 获取订单号
        dev_order_id = dev_data[0]
        self.assertEqual(online_order_id, dev_order_id)
        print("订单号：", online_order_id)


        ## 查询线上  # real_channel '还款类型：1银行卡 2余额宝'
        # 获取还款类型
        online_real_channel = online_data[0][0]
        # 获取还款类型
        dev_real_channel = dev_data[1]
        self.assertEqual(online_real_channel, dev_real_channel)
        print("还款类型：", online_real_channel)

        # # bill_date 账单日期
        # 获取第几期
        online_bill_date = online_data[0][1]
        # 获取第几期
        dev_bill_date = dev_data[2]
        self.assertEqual(online_bill_date.strftime("%Y-%m-%d"), dev_bill_date)
        print("获取账单日期：", online_bill_date)

        # # bill_amount 账单金额
        # 获取账单金额
        online_bill_amount = online_data[0][4]
        # 获取账单金额
        dev_bill_amount = dev_data[5]
        self.assertEqual(online_bill_amount, dev_bill_amount)
        print("账单金额：", online_bill_amount)

        # period 第几期
        # 获取第几期
        online_period = online_data[0][2]
        print('dev_bill_date:', online_period)
        # 获取第几期
        dev_period = dev_data[3]
        self.assertEqual(online_period, dev_period)
        print("获取账单日期：", online_period)

        # # status 还款状态
        # 获取还款状态 2
        online_status = online_data[0][3]
        # 获取还款状态 1
        dev_status = dev_data[4]
        self.assertEqual(online_status, dev_status+1)
        print("还款状态：", online_status)







if __name__ == '__main__':
    res=OrderSubsidy().test_assert_data()



