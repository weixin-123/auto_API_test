#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/10/17
@File    : test_CarModel.py
"""
# 第三方包
import unittest
from faker import Faker

from common.request import HttpRequest
from common.connect_db import DoMysql

f = Faker('zh_CN')


class CarModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 查询数据库当前索引位置
        a = DoMysql().query_sql('car-v2',
                                "SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA='car-v2' AND TABLE_NAME='life_car_brands'")
        index = a[0][0]  # 索引
        return index

    def setUp(self):
        pass

    def test_Add_Branch(self):
        """
        :return: 上传品牌
        """
        # 调用接口
        url = "/car-v2/staff/car-model/brand/add"
        data = {
            "name": '重庆测试',
            "logo": f.image_url()
        }
        response = HttpRequest.post(url, data, service_name="admin")
        # 返回结果断言
        self.assertEqual(0, response['code'])
        self.assertEqual('success', response['message'])

    def test_brandDel(self):
        """
        :return: 删除品牌
        """
        url = '/car-v2/staff/car-model/brand/brandDel'
        data1 = DoMysql().query_sql('car-v2', "SELECT MAX(ID) FROM `life_car_brands`")
        # 取id的value值
        data = data1[0][0]
        a = {'id': data}
        response = HttpRequest.post(url, a, service_name="admin")
        # 返回结果断言
        self.assertEqual(0, response['code'])
        self.assertEqual('success', response['message'])

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        index1 = CarModel.setUpClass()
        print(index1)
        DoMysql().roll_back('car-v2')
        a=DoMysql().query_sql('car-v2', f"ALTER TABLE life_car_brands AUTO_INCREMENT = {index1}")
        print(a)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CarModel)
    unittest.TextTestRunner(verbosity=2).run(suite)
