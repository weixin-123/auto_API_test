#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/11
@File    : test_login_app.py
"""
import unittest
import os
from ddt import data, ddt

from common.log_color import LogingColor
from common.read_user_config import ReadUserConfig
from common.request import HttpRequest
from common.operator_excel import DoExcel

logging = LogingColor()
read_user = ReadUserConfig()



@ddt
class LoginApp(unittest.TestCase):

    # EXCEL读取
    test_data = DoExcel().get_data(os.path.abspath(__file__), "Sheet1")

    @data(*test_data)
    def test_login_app(self, request_data):
        case_id = request_data["case_id"]
        title = request_data["title"]
        print("---------执行第" + str(case_id) + "条,caseName为:" + str(title) + ",测试用例---------")

        # 调用接口
        # temp_params = json.loads(request_data["params"])
        result = HttpRequest.post(request_data["url"], request_data["params"], 'app')
        print(result)

        if case_id == 1:
            # code、messsage断言
            logging.info("——————————校验返回code、message——————————")
            self.assertEqual(0, result['code'])
            self.assertEqual('success', result['message'])
            logging.info("——————————code、message校验通过——————————")
            # 查询数据库
            # 数据——断言
            self.assertIsNotNone(result['data'])

        if case_id == 2:
            # code、messsage断言
            logging.info("——————————校验返回code、message——————————")
            self.assertEqual(200083, result['code'])
            self.assertEqual('请输入注册销巴会员的手机号', result['message'])
            logging.info("——————————code、message校验通过——————————")
            # 查询数据库
            # 数据——断言
            self.assertIsNotNone(result['data'])

        if case_id == 3:
            # code、messsage断言
            logging.info("——————————校验返回code、message——————————")
            self.assertEqual(422, result['code'])
            self.assertEqual('validation_error', result['message'])
            logging.info("——————————code、message校验通过——————————")
            # 查询数据库
            # 数据——断言
            self.assertIsNotNone(result['data'])


if __name__ == "__main__":
    # 一次性加载某个测试类里面的所有方法
    my_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    my_suite.addTest(loader.loadTestsFromTestCase(LoginApp))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(my_suite)

    # suite = unittest.TestLoader().loadTestsFromTestCase(LoginApp)
    # unittest.TextTestRunner(verbosity=2).run(suite)
