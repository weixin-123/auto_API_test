#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 17:29
# @Author  : lijian
# @File    : test_order_people.py
# @Software: PyCharm
import unittest

from common.log_color import LogingColor
from test_case.car_service.wash_car_data.sql_db.dev_order_money import DevOrderMoney
from test_case.car_service.wash_car_data.sql_db.online_order_money import OnlineOrder

on_order = OnlineOrder()
de_order = DevOrderMoney()
log = LogingColor()


class TestOrderPeople(unittest.TestCase):

    def test_assert_data(self):
        for i in range(0, 20):
            # ----------------线上----------------
            # 随机获取订单id
            order_id = on_order.rand_order_id()
            # 根据订单id获取订单号
            order_no = on_order.query_order_no(order_id)
            # 做业务~~~~~~~
            # area_name省和市,user_name购车人姓名,user_id_card购车人身份证,user_contact用户联系电话,order_type订单类型：1半价购 2全返购
            on_people = on_order.query_order_people(order_no)
            de_people = de_order.quer_order_people(order_no)
            self.assertIsNotNone(de_people[0][0])  # province
            self.assertIsNotNone(de_people[0][1])  # city
            self.assertEqual(on_people[0][1], de_people[0][2])  # user_name
            self.assertEqual(on_people[0][2], de_people[0][3])  # user_id_card
            self.assertEqual(on_people[0][3], de_people[0][4])  # user_contact
            self.assertEqual(on_people[0][4], de_people[0][5])  # order_type

if __name__ == '__main__':
    TestOrderPeople().test_assert_data()