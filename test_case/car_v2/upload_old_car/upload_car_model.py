#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/12
@File    : upload_car_model.py
"""
import json

from faker import Faker

from common.request import HttpRequest
from common.log_color import LogingColor
from test_case.car_v2.login_step.use_sql import UseSql
from test_case.car_v2.login_step.random_data import Random_Data

f = Faker('zh_CN')
logging = LogingColor()

vehicle_identification_num = Random_Data.vehicle_identification_num()
location = Random_Data().random_city_code()
brand_model_version_id = Random_Data().brand_model_version_id()
# print("brand_model_version_id:", brand_model_version_id)
images = Random_Data().random_images(brand_model_version_id)
# print("images:", images)
# print(location)

class UploadCarModel:
    def upload_car(self):
        """
        上传二手车
        :return:
        """
        # UploadCarModel().Change_System_Settings()
        merchant_id = UseSql().use_sql_select_two(13436137948)
        logging.info("上传二手车辆中")
        url = "/car-v2/app/sell-car/second_hand_car"
        params = {
            "brand_model_version_id": brand_model_version_id,
            "location": json.dumps(location),
            "mileage": 120000,
            "transfers_num": f.random_int(0, 5),
            "vehicle_identification_num": vehicle_identification_num,
            "official_price": 20000,
            # 时间不能用dumps 要不然不能被解析 会报参数错误
            "first_registration_at": "2020-01-01",
            # "vehicle_description": "好车欢迎购买",
            "images": images,
            "merchant_id": merchant_id
        }
        # json.load ''  json.dumps "" 字典
        temp_data = json.dumps(params)
        result = HttpRequest.post(url, temp_data, service_name="app")
        print(result)
        if result["message"] == "success":
            logging.info('%s提交成功，审核通过(*^▽^*)')
        else:
            logging.error('(ಥ﹏ಥ)%s提交失败的原因：' + result['message'])
            return result["message"]

    def Change_System_Settings(self):
        """
        更改系统设置(直接通过)
        :return:
        """
        url = "/car-v2/staff/car-setting/edit"
        data = {
            # 0关闭车辆审核 1开启车辆审核
            "id": 1,
            "value": 0.58
        }
        result = HttpRequest.post(url, data, service_name="admin")
        if result["message"] == "success":
            logging.info("系统设置成功(*^▽^*)---取消审核---")
            return "true"
        else:
            logging.error('(ಥ﹏ಥ)系统设置更改失败的原因：' + result['message'])
            return result["message"]


if __name__ == "__main__":
     UploadCarModel().upload_car()
