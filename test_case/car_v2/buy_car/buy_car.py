#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/13
@File    : buy_car.py
"""
import json

from faker import Faker
from common.request import HttpRequest
from common.log_color import LogingColor
from test_case.car_v2.buy_car.get_new_car_series import GetNewCarSeries
from test_case.car_v2.buy_car.get_old_car_series import GetOldCarSeries
from test_case.car_v2.login_step.login_app import LoginApp

from test_case.car_v2.login_step.random_data import Random_Data
from test_case.car_v2.login_step.use_sql import UseSql


f = Faker('zh_CN')
logging = LogingColor()
module_type_id = Random_Data().module_type_id()
# phone = LoginApp().login_app()
merchant_id = UseSql().use_sql_select_six(13436137948)

class BuyCar:
    def confirm_order(self, module_type_id, car_id):
        url = "/order/app/order/confirm"
        params = {
            "order": {
                # 订单类型；固定：{"type":"car-v2"}
                "type": "car-v2"
            },
            "car_id": car_id,
            # 60:新车、61:二手车
            "module_type_id": module_type_id,
            "down_payment": 3000.00
        }
        temp_params=json.dumps(params)
        result = HttpRequest.post(url, temp_params, "app")
        if result["message"] == "success":
            logging.info('确认订单成功(*^▽^*)')
            return result["data"]["order"]["confirm"]
        else:
            logging.error('(ಥ﹏ಥ)确认订单失败的原因：' + result['message'])
            return result["message"]

    def buy_car(self, module_type_id, offers_type, car_id):
        """
        60:新车、61:二手车
        :return:
        """
        # 服务器向客户端发送确认订单的信息,客户端做出回应
        data = GetNewCarSeries().car_detail(1)
        order = BuyCar().confirm_order(module_type_id,car_id)
        print(order[0])
        city_code = Random_Data().random_city_code()
        standard_type_id=data["standard_type_id"]
        print("standard_type_id:", standard_type_id)
        if module_type_id == 60:
            car_norm = UseSql().use_sql_select_four(data["standard_type_id"])
            print(car_norm)
            # guid_price = UseSql().use_sql_select_five(data["brand_model_id"], 60)
            url = "/order/app/order/create"
            if offers_type == 1:
                """
                1消费补贴 2积分补贴
                """
                """
                客户端回应到的信息将它
                """
                params = {
                    "order": {
                        "confirm": order,
                        "type": "car-v2",
                        "client": 10
                    },
                    "name": f.first_name(),
                    "phone": f.phone_number(),
                    "id_number": f.ssn(),
                    "offers_type": 2,
                    "car_info": {
                        "image": data["image"],
                        # life_car_brand_model_versions brand_model_id
                        # life_car_brand_model brand_id=1  id=5
                        "brand_model_id": data["brand_model_id"],
                        # life_car_brand_model_versions brand_id=1
                        # life_car_brand_model brand_id=1  id=5  name
                        "brand_model": data["brand_model"],
                        # `selling_price` 售价  二手车
                        # `guid_price` 指导价  新车
                        # life_car_brand_model_versions brand_id=1
                        # life_car_brand_model brand_id=1  id=5 guid_price
                        # life_car_brand_models guid_price
                        # "sell_or_guide_price": guid_price,
                        "sell_or_guide_price": data["official_price"],
                        # life_car_brand_model_versions category_type_id 27
                        # SELECT * FROM `life_car_types` id 27
                        "car_rank": data["car_rank"],
                        # life_car_brand_model_versions name
                        "car_versions": data["car_versions"],
                        # life_car_brand_model_versions standard_type_id 72
                        # SELECT * FROM `life_car_types` id 72
                        "car_norm": car_norm
                    },
                    "merchant_id": merchant_id,
                    "city_code": city_code["city"]["code"],
                    "province_code": city_code["province"]["code"],
                    # "member_city_code": city_code["province"]["name"],
                    # "member_province_code": city_code["city"]["name"],
                    "member_city_code": city_code["city"]["code"],
                    "member_province_code": city_code["province"]["code"],
                    # life_car_brand_model_versions id
                    "car_id": car_id,
                    # 新车固定传1
                    "module_type_id": module_type_id,
                    "down_payment": 3000,
                    "note": "",
                    "referrer_phone": ""
                }
                temp_params = json.dumps(params)
                result = HttpRequest.post(url, temp_params, service_name="app")
                if result["message"] == "success":
                    logging.info('购买新车订单提交成功(*^▽^*)')
                else:
                    logging.error('(ಥ﹏ಥ)购买新车订单提交失败的原因：' + result['message'])
                    return result["message"]
            else:
                # 客户端回应到的信息将它
                params = {
                    "order": {
                        "confirm": order,
                        "type": "car-v2",
                        "client": 10
                    },
                    "name": f.first_name(),
                    "phone": f.phone_number(),
                    "id_number": f.ssn(),
                    "offers_type": 2,
                    "car_info": {
                        "image": data["image"],
                        # life_car_brand_model_versions brand_model_id
                        # life_car_brand_model brand_id=1  id=5
                        "brand_model_id": data["brand_model_id"],
                        # life_car_brand_model_versions brand_id=1
                        # life_car_brand_model brand_id=1  id=5  name
                        "brand_model": data["brand_model"],
                        # `selling_price` 售价  二手车
                        # `guid_price` 指导价  新车
                        # life_car_brand_model_versions brand_id=1
                        # life_car_brand_model brand_id=1  id=5 guid_price
                        # life_car_brand_models guid_price
                        # "sell_or_guide_price": guid_price,
                        "sell_or_guide_price": data["official_price"],
                        # life_car_brand_model_versions category_type_id 27
                        # SELECT * FROM `life_car_types` id 27
                        "car_rank": data["car_rank"],
                        # life_car_brand_model_versions name
                        "car_versions": data["car_versions"],
                        # life_car_brand_model_versions standard_type_id 72
                        # SELECT * FROM `life_car_types` id 72
                        "car_norm": car_norm
                    },
                    "merchant_id": merchant_id,
                    "city_code": city_code["city"]["code"],
                    "province_code": city_code["province"]["code"],
                    # "member_city_code": city_code["province"]["name"],
                    # "member_province_code": city_code["city"]["name"],
                    "member_city_code": city_code["city"]["code"],
                    "member_province_code": city_code["province"]["code"],
                    # life_car_brand_model_versions id
                    "car_id": car_id,
                    # 新车固定传1
                    "module_type_id": module_type_id,
                    "down_payment": 3000,
                    "note": "",
                    "referrer_phone": ""
                }
                temp_params = json.dumps(params)
                result = HttpRequest.post(url, temp_params, "app")
                if result["message"] == "success":
                    logging.info('购买新车订单提交成功(*^▽^*)')
                    return result['data']['ordersn']
                else:
                    logging.error('(ಥ﹏ಥ)购买新车订单提交失败的原因：' + result['message'])
                    return result["message"]

        else:
            """
            二手车
            """
            url = "/order/app/order/create"
            data = GetNewCarSeries().car_detail(1)
            sell_price = UseSql().use_sql_select_five(data["result_name"], 61)
            if offers_type == 1:
                """
                1消费补贴 2积分补贴
                """
                data = GetOldCarSeries().get_old_car_detail()
                params = {
                    "order": {
                        """
                        confirm 确认订单 确认有这个车可以进行购买
                        """
                        "confirm": order,
                        "type": "car-v2",
                        # 客户端
                        "client": 10
                    },
                    "name": f.first_name(),
                    "phone": f.phone_number(),
                    "id_number": f.ssn(),
                    "offers_type": 1,
                    "car_info": {"image": data['image'],
                                 "brand_model_id": data['brand_model_id'],
                                 "brand_model": data['brand_model'],
                                 "sell_or_guide_price": sell_price,
                                 "car_rank": data['car_rank'],
                                 "car_versions": data['car_versions'],
                                 "car_norm": data['car_norm']
                                 },
                    "merchant_id": merchant_id,
                    "city_code": city_code["province"]["code"],
                    "province_code": "500000",
                    "member_city_code": city_code["city"]["code"],
                    "member_province_code": city_code["province"]["code"],
                    "car_id": car_id,
                    "module_type_id": module_type_id,
                    "down_payment": 3000,
                    "note": "",
                    "referrer_phone": ""
                }
                result = HttpRequest.post(url, params, service_name="app")
                if result["message"] == "success":
                    logging.info('购买二手车订单提交成功(*^▽^*)----')
                else:
                    logging.error('(ಥ﹏ಥ)购买二手车订单提交失败的原因：' + result['message'])
                    return result["message"]
            else:
                data = GetOldCarSeries().get_old_car_detail()
                params = {
                    "order": {
                        """
                        confirm 确认订单 确认有这个车可以进行购买
                        """
                        "confirm": order,
                        "type": "car-v2",
                        # 客户端
                        "client": 10
                    },
                    "name": f.first_name(),
                    "phone": f.phone_number(),
                    "id_number": f.ssn(),
                    "offers_type": 2,
                    "car_info": {"image": data['image'],
                                 "brand_model_id": data['brand_model_id'],
                                 "brand_model": data['brand_model'],
                                 "sell_or_guide_price": 0,
                                 "car_rank": data['car_rank'],
                                 "car_versions": data['car_versions'],
                                 "car_norm": data['car_norm']
                                 },
                    "merchant_id": merchant_id,
                    "city_code": city_code["province"]["code"],
                    "province_code": "500000",
                    "member_city_code": city_code["city"]["code"],
                    "member_province_code": city_code["province"]["code"],
                    "car_id": car_id,
                    "module_type_id": module_type_id,
                    "down_payment": 3000,
                    "note": "",
                    "referrer_phone": ""
                }
                result = HttpRequest.post(url, params, service_name="app")
                if result["message"] == "success":
                    logging.info('购买二手车订单提交成功(*^▽^*)')
                    return result["data"]["ordersn"]
                else:
                    logging.error('(ಥ﹏ಥ)购买二手车订单提交失败的原因：' + result['message'])
                    return result["message"]


if __name__ == "__main__":
    # 买1消费补贴 2积分补贴  60:新车、61:二手车  car_id
    # # 买新车 消费补贴
    BuyCar().buy_car(60, 1, 21)
    # # 买新车 积分补贴
    # BuyCar().buy_car(60, 2, 31)
    # # 买二手车 消费补贴
    # BuyCar().buy_car(61, 1, 21)
    # # 买二手车 积分补贴
    # BuyCar().buy_car(61, 2, 31)