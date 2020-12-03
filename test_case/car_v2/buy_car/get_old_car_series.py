#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/17
@File    : get_old_car_series.py
"""
import json
import random
from faker import Faker

from common.request import HttpRequest
from common.log_color import LogingColor

f = Faker('zh_CN')

logging = LogingColor()


class GetOldCarSeries:
    """
    获取所有二手车信息
    """

    def get_old_car_list(self):
        url = "/car-v2/app/buy-car/second_hand_car/filter"
        result = HttpRequest.get(url, None, service_name="app")
        if result["message"] == "success":
            logging.info('这是所有的二手车啦，快快带走你心仪的车车吧~~~')
            result_data = result['data']['list']
            temp_data_list = []
            for i in result_data:
                data = i
                temp_data = data['id']
                temp_data_list.append(temp_data)
            old_car_id = random.choice(temp_data_list)
            print("result_data:", old_car_id)
            # return的目的就是保证调用改方法时不返回空值(None)
            return old_car_id
        else:
            logging.error('抱歉没有查到关于二手车的信息哦！获取二手车失败的原因：' + result['message'])
            result["message"] = json.dumps("message")
            return result["message"]

    """
    获取二手车详情 
    """

    def get_old_car_detail(self):
        car_source_id = GetOldCarSeries().get_old_car_list()
        url = "/car-v2/app/buy-car/second_hand_car/%s" % car_source_id
        result = HttpRequest.get(url, None, service_name="app")
        print(result)

        if result["message"] == "success":
            logging.info('车系挑选成功啦！最后一步挑选你喜欢的车型进行购买吧！')
            result_data = result['data']
            # 车辆标题图 "http://car-goods.qiniudns.shall-buy.com/brand_model_versions_52769_0.jpg",
            result_front_image = result_data['images']['front']
            # 品牌型号id 5
            result_brand_model_id = result_data['brand_model_version']['brand_model']['id']
            # 品牌于车系 "奥迪Q2L"
            result_brand_model = result_data['brand_model_version']['brand_model']['name']
            # 汽车级别 SUV
            result_category_type = result_data['category_type']
            # 品牌型号版本名称 2021款 35 TFSI 进取动感型
            result_name = result_data['brand_model_version']['name']
            print('result_name:', result_name)
            # 车类型id 其它
            result_standard_type = result_data['standard_type']
            temp_car_data = {"image": result_front_image, "brand_model_id": result_brand_model_id,
                             "brand_model": result_brand_model, "car_rank": result_category_type,
                             "car_versions": result_name, "car_norm": result_standard_type}
            if result_brand_model_id == '':
                GetOldCarSeries().get_old_car_detail()
            else:
                return temp_car_data
        else:
            logging.error('b抱歉没有查到关于二手车的信息哦！获取二手车失败的原因：' + result['message'])
            result["message"] = json.dumps("message")
            return result["message"]


if __name__ == "__main__":
    print(GetOldCarSeries().get_old_car_detail())
    # result=Get_Car_Series().car_detail(1)
    # data_dname=result['id']
