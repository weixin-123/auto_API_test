#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/11
@File    : register_member.py
"""
import json

from common.request import HttpRequest
from common.log_color import LogingColor

logging = LogingColor()

from test_case.car_v2.login_step.random_data import Random_Data

from test_case.car_v2.login_step.use_sql import UseSql


class Register_Member:

    def register_app(self):
        """
        注册销巴会员
        :param phone:
        :return:
        """
        phone = Random_Data().random_phone()
        register_url = "/app/index/app/register"
        while 1:
            print("开始执行while语句")
            data = UseSql().use_sql_select_one(phone)
            if data == "true":
                print("开始执行自动生成手机号")
                phone = Random_Data().random_phone()
                print("重新生成的手机号是：", phone)
                continue

            else:
                logging.info("请求URL：" + register_url)
                params = {
                    "password": "aa123456",
                    "password_confirmation": "aa123456",
                    "code": "123456",
                    "username": phone
                }
                logging.info("请求参数:" + str(params))
                temp_params = json.dumps(params)
                result = HttpRequest.post(register_url, temp_params, service_name="app")
                # result_json = result.json()
                # print(result_json)
                if result["message"] == "success":
                    logging.info('注册销巴会员成功(*^▽^*)')
                    return phone
                else:
                    logging.error('(ಥ﹏ಥ)注册销巴会员失败的原因：' + result['message'])
                    return result["message"]


if __name__ == "__main__":
    res = Register_Member().register_app()
