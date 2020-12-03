#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/12
@File    : random_data.py
"""
import random
import string


class Random_Data:
    # 随机生成商户
    @classmethod
    def random_merchant(cls):
        id_card_list = ["普通个人", "个人门店", "直营店", "服务中心",
                        "商家", "代理人"]
        temp_num = random.choice(id_card_list)
        return temp_num

    # 随机生成电话号码
    @classmethod
    def random_phone(cls):
        num_start = ['134361']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 5))
        res = start + end
        return res

    # 随机生成城市地区
    @classmethod
    def random_city_code(cls):
        list1 = {"province": {"name": "澳门特别行政区", "code": "820000"}, "city": {"name": "风顺堂区", "code": "820005"}}
        list2 = {"province": {"name": "重庆市", "code": "500000"}, "city": {"name": "重庆市市辖区", "code": "500100"}}
        list3 = {"province": {"name": "安徽省", "code": "340000"}, "city": {"name": "合肥市", "code": "340100"}}
        list4 = {"province": {"name": "北京市", "code": "110000"}, "city": {"name": "北京市", "code": "110100"}}
        list5 = {"province": {"name": "山西省", "code": "140000"}, "city": {"name": "晋中市", "code": "140700"}}
        list6 = {"province": {"name": "浙江省", "code": "330000"}, "city": {"name": "温州市", "code": "330300"}}
        list7 = {"province": {"name": "黑龙江省", "code": "230000"}, "city": {"name": "鹤岗市", "code": "230400"}}
        list8 = {"province": {"name": "辽宁省", "code": "210000"}, "city": {"name": "抚顺市", "code": "210400"}}
        list9 = {"province": {"name": "新疆维吾尔自治区", "code": "650000"}, "city": {"name": "博尔塔拉蒙古自治州", "code": "652700"}}
        list10 = {"province": {"name": "香港特别行政区", "code": "810000"}, "city": {"name": "荃湾区", "code": "810010"}}
        list11 = {"province": {"name": "宁夏回族自治区", "code": "640000"}, "city": {"name": "中卫市", "code": "640500"}}
        city_code_list = [list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11]
        city_code = random.choice(city_code_list)
        return city_code

    # 生成身份证照片
    @classmethod
    def random_card_image(cls, data):
        """
        上传身份证照片
        :return:
        """
        list1 = ["2020111114322442462327.jpeg"]
        list2 = ["2020111114322733720672.jpeg"]
        if data == "card_front":
            return list1
        else:
            """
            身份证背面
            """
            return list2

    # 随机生成营业执行
    @classmethod
    def random_business_license(cls):
        """
        上传营业执照
        :return:
        """
        list1 = ["2020111114322733720672.jpeg"]
        list2 = ["2020111114322733720672.jpeg", "2020111114322442462327.jpeg"]
        list3 = ["2020111114322733720672.jpeg", "2020111114322442462327.jpeg", "2020111214385043541543.jpeg"]
        business_license_list = [list1, list2, list3]
        business_license = random.choice(business_license_list)
        return business_license

    # 随机生成车架号
    @classmethod
    def vehicle_identification_num(cls):
        first_list = ['1341524', '1572315', '1822548', '1802647', '1894152']
        second_list = ['shlqw', 'shled', 'akmdw', 'qwklc', 'dwlcf']
        third_list = ['48523', '89654', '63204', '53203', '52100']
        vehicle_identification_num = random.choice(first_list) + random.choice(second_list) + random.choice(
            third_list)
        return vehicle_identification_num

    # 随机选取车类型
    @classmethod
    def module_type_id(cls):
        """
        60:新车、61:二手车
        :return:
        """
        list1 = [60, 61]
        module_type_id = random.choice(list1)

        return module_type_id

    # 随机生成车型
    @classmethod
    def brand_model_version_id(cls):
        list1 = [52772, 44380, 48157]
        brand_model_version_id = random.choice(list1)
        return brand_model_version_id

    # 随机生成images
    @classmethod
    def random_images(cls, brand_model_version_id):
        if brand_model_version_id == 52772:
            images = {
                "front": "http://car-used-goods.qiniudns.shall-buy.com/2020112114224874061232.png",
                "front_left": "http://car-used-goods.qiniudns.shall-buy.com/2020112114224524303865.png",
                "front_right": "http://car-used-goods.qiniudns.shall-buy.com/2020112114231879020955.png",
                "left": "http://car-used-goods.qiniudns.shall-buy.com/2020112114224994392762.png",
                "right": "http://car-used-goods.qiniudns.shall-buy.com/2020112114225783779066.png",
                "rear": "http://car-used-goods.qiniudns.shall-buy.com/2020112114230391318893.png",
                "central_control": "http://car-used-goods.qiniudns.shall-buy.com/2020112114225254009547.png",
                "dashboard": "http://car-used-goods.qiniudns.shall-buy.com/2020112114225967105145.png",
                "seat_front": "http://car-used-goods.qiniudns.shall-buy.com/2020112114231569333614.png",
                "seat_rear": "http://car-used-goods.qiniudns.shall-buy.com/2020112114225419778887.png",
                "other": []
            }
            return images
        elif brand_model_version_id == 44380:
            images = {
                "central_control": "http://car-used-goods.qiniudns.shall-buy.com/2020112115272289487620.jpeg",
                "front": "http://car-used-goods.qiniudns.shall-buy.com/2020112115270214026009.jpeg",
                "front_left": "http://car-used-goods.qiniudns.shall-buy.com/2020112115270513270761.jpeg",
                "front_right": "http://car-used-goods.qiniudns.shall-buy.com/2020112115270969469824.jpeg",
                "left": "http://car-used-goods.qiniudns.shall-buy.com/2020112115271336324296.jpeg",
                "right": "http://car-used-goods.qiniudns.shall-buy.com/2020112115271677066998.jpeg",
                "rear": "http://car-used-goods.qiniudns.shall-buy.com/2020112115271967972705.jpeg",
                "dashboard": "http://car-used-goods.qiniudns.shall-buy.com/2020112115272463214182.jpeg",
                "seat_front": "http://car-used-goods.qiniudns.shall-buy.com/2020112115272775363274.jpeg",
                "seat_rear": "http://car-used-goods.qiniudns.shall-buy.com/2020112115272959038742.jpeg",
                "other": []
            }
            return images
        elif brand_model_version_id == 48157:
            images = {
                "central_control": "http://car-used-goods.qiniudns.shall-buy.com/2020112116165554746552.jpeg",
                "front": "http://car-used-goods.qiniudns.shall-buy.com/2020112116164150744983.jpeg",
                "front_left": "http://car-used-goods.qiniudns.shall-buy.com/2020112116164383472243.jpeg",
                "front_right": "http://car-used-goods.qiniudns.shall-buy.com/2020112116164693415165.jpeg",
                "left": "http://car-used-goods.qiniudns.shall-buy.com/2020112116164810303207.jpeg",
                "right": "http://car-used-goods.qiniudns.shall-buy.com/2020112116165134777569.jpeg",
                "rear": "http://car-used-goods.qiniudns.shall-buy.com/2020112116165379568675.jpeg",
                "dashboard": "http://car-used-goods.qiniudns.shall-buy.com/2020112116165822801149.jpeg",
                "seat_front": "http://car-used-goods.qiniudns.shall-buy.com/2020112116170288244459.jpeg",
                "seat_rear": "http://car-used-goods.qiniudns.shall-buy.com/2020112116171358919245.jpeg",
                "other": []
            }
            return images


if __name__ == '__main__':
    # print(Random_Data().random_phone())
    # print(Random_Data().random_merchant())
    # print(Random_Data().random_city_code())
    print(Random_Data().random_business_license())
    # print(Random_Data().random_images(48157))
