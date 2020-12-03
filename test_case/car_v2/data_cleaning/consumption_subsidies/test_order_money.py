#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 14:09
# @Author  : lijian
# @File    : test_order_money.py
# @Software: PyCharm
import json
import unittest
from datetime import time

from common.log_color import LogingColor
from test_case.car_v2.data_cleaning.consumption_subsidies.dev_order_money import DevOrderMoney
from test_case.car_v2.data_cleaning.consumption_subsidies.online_order_money import OnlineOrder

on_order_money = OnlineOrder()
de_order_money = DevOrderMoney()
log = LogingColor()


class TestOrderMoney(unittest.TestCase):

    def test_assert_data(self):
        for i in range(15):
            # ----------------线上----------------
            # 随机获取订单id
            order_id = on_order_money.rand_order_id()
            # order_id = 5826
            # 根据订单id获取线上分期金额
            online_money = on_order_money.query_bill_amount(order_id)
            # ----------------老数据库----------------
            # 根据订单id获取订单号
            order_no = on_order_money.query_order_no(order_id)
            dev_data = de_order_money.quer_perk_details(order_no)
            temp_data = json.loads(dev_data)
            print("temp_data:", temp_data)
            # ----------------数据校验对比----------------
            # 校验每期还款金额
            j = 0
            for i in temp_data['periods_details']:
                dev_money = i['subsidy_money']
                info = "第%s期，还款金额为：" % j
                log.info(info + dev_money)
                self.assertEqual(str(online_money[j][0]), dev_money)
                j = j + 1
            log.info("每期还款金额检验完成———————————————————")
            # 账单日期
            on_order_data = on_order_money.query_bill_data(order_id)
            m = 0
            for data in temp_data['periods_details']:
                subsidy_date = data['subsidy_date']
                info = "第%s账单日期为：" % m
                log.info(info + subsidy_date)
                self.assertEqual(str(on_order_data[m][0]), subsidy_date)
                m = m + 1
            log.info("每期账单日期检验完成———————————————————")
            # 校验已还款期数
            on_overorder_data_id = on_order_money.query_over_bill(order_id)
            n = 0
            nn = 0
            for data in temp_data['periods_details']:
                subsidy_status = data['subsidy_status']
                if n == nn:
                    info = "查询已经还款期数，第%s期" % n
                    log.info(info)
                else:
                    info = "剩余未还期数，第%s期" % nn
                    log.info(info)
                if subsidy_status == 1:
                    n = n + 1
                nn = nn + 1
            self.assertEqual(on_overorder_data_id, n)
            log.info("校验已还款期数次数检验完成———————————————————")
            # 已还款期数，每期日期校验
            on_overorder_data = on_order_money.query_over_bill_data(order_id)
            b = 0
            bb = 0
            log.info("已还款期数日期开始检验~~~~~~~~~~~~~~~")
            for data in temp_data['periods_details']:
                subsidy_status = data['subsidy_status']
                subsidy_date1 = data['subsidy_date']

                if b == bb:
                    info = "已还款日期，第%s期--" % b
                    log.info(info + subsidy_date1)
                else:
                    info = "剩余未还款日期，第%s期--" % bb
                    log.info(info + subsidy_date1)
                if subsidy_status == 1:
                    temp_data = on_overorder_data[b][0].strftime('%Y-%m-%d')
                    self.assertEqual(temp_data, subsidy_date1)
                    b = b + 1
                bb = bb + 1
            log.info("已还款日期检验完成———————————————————")


if __name__ == '__main__':
    TestOrderMoney().test_assert_data()
