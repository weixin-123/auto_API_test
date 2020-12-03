#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/18
@File    : pay_car_order.py
"""
from common.request import HttpRequest
from test_case.car_v2.buy_car.buy_car import BuyCar
from common.log_color import LogingColor

# ordersn = BuyCar().buy_car()
logging = LogingColor()


class PayCarOrder:
    """
    支付订单
    """

    def balance_pay(self, ordersn):

        url = '/order/app/order/pay'
        # pay_type= RandomData.randomPayType() # 支付方式 1：银联 2：支付宝 3：微信 4：余额 5：支付宝H5 6：微信H5 7: 微信小程序支付
        params = {
            "password": 123456,
            "money": 3000.00,
            'ordersn': ordersn,
            "pay_type": 4,
            'success_url': '',
            'result_url': ''
        }
        result = HttpRequest.post(url, params, "app")
        if result["message"] == "success":
            logging.info('购买新车成功(*^▽^*)，欢迎下次再来')
        else:
            logging.error('(ಥ﹏ಥ)购买新车失败的原因：' + result['message'])
            return result["message"]


if __name__ == "__main__":
    ordersn = BuyCar().buy_car(60, 2, 56)
    PayCarOrder().balance_pay(ordersn)
