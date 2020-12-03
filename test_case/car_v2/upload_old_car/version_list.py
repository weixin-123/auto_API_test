#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/16
@File    : version_list.py
"""
from common.request import get
from common.log_color import LogingColor

logging = LogingColor()

class Brand_List:
    """
    通过车系返回的id获取车型
    """
    def brand_list(self,id):
        url = "/car-v2/app/buy-car/brand"
        result = get(url, None, service_name="app")
        if result["message"] == "success":
            logging.info('品牌列表获取成功')
            return

        else:
            logging.error('品牌列表获取失败的原因：' + result['message'])
            return result["message"]
