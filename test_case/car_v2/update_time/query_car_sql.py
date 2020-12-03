#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 10:45
# @Author  : lijian
# @File    : query_car_sql.py
# @Software: PyCharm

# 自定义包
from common.connect_db import MyDB
from common.log_color import LogingColor

mydb = MyDB()
logging = LogingColor()


class QueryCarSql:

    def __init__(self):
        pass

    # life_car_sources表（查询待审核的数据）
    def query_life_car_sources_status(self, merchant_id):
        logging.info("——————————查询数据库——————————")
        sql = "select id from `life_car_sources` WHERE merchant_id in('%s') and status='0' " % merchant_id
        result = mydb.query_sql('car-v2', sql)[0]
        if result is None or result == '':
            return '查询数据失败，根据id查询life_car_brand_model_versions表，查询不到数据！！'
        else:
            return result[0]
        # life_car_sources表（查询待审核的数据）

    def query_life_car_status(self, id):
        logging.info("——————————查询数据库——————————")
        sql = "select status from `life_car_sources` WHERE id in('%s')" % id
        result = mydb.query_sql('car-v2', sql)[0]
        if result is None or result == '':
            return '查询数据失败，根据id查询life_car_sources表，查询不到数据！！'
        else:
            return result[0]
    # 查询汽车信息：品牌型号版本
    def query_life_car_brand_model_versions(self, id):
        logging.info("——————————查询数据库——————————")
        sql = "select brand_model_id,name,official_price,standard_type_id,xb_perk_price,images,category_type_id from `life_car_brand_model_versions` WHERE id in('%s')" % id
        result = mydb.query_sql('car-v2', sql)[0]
        if result is None or result == '':
            return '查询数据失败，根据id查询life_car_brand_model_versions表，查询不到数据！！'
        else:
            return result

        # 查询二手车信息：品牌型号版本
    def query_life_car_sources_info(self, carid):
        logging.info("——————————查询数据库——————————")
        sql = "select official_price from `life_car_sources` WHERE id in('%s')" % carid
        result = mydb.query_sql('car-v2', sql)[0]
        if result is None or result == '':
            return '查询数据失败，根据id查询life_car_brand_model_versions表，查询不到数据！！'
        else:
            return result[0]
    # 查询汽车信息：品牌型号名称
    def query_life_car_brand_models(self, id):
        logging.info("——————————查询数据库——————————")
        sql = "select name,cover_image from `life_car_brand_models` WHERE id in('%s')" % id
        result = mydb.query_sql('car-v2', sql)[0]
        return result

    # 查询汽车信息：品牌型号名称
    def query_life_car_merchants(self, id):
        logging.info("——————————查询数据库——————————")
        sql = "select company_full_name,name from `life_car_merchants` WHERE id in('%s')" % id
        result = mydb.query_sql('car-v2', sql)[0]

        if result[0] is not None:
            return result[0]
        else:
            return result[1]

    # 查询汽车信息：汽车类别
    def query_life_car_types(self, id):
        logging.info("——————————查询数据库——————————")
        sql = "select name from `life_car_types` WHERE id in('%s')" % id
        result = mydb.query_sql('car-v2', sql)[0][0]
        return result

    # 查询汽车订单：订单id
    def query_life_car_order(self, order_code):
        logging.info("——————————查询数据库——————————")
        sql = "select id from `life_car_order` WHERE order_code in('%s')" % order_code
        result = mydb.query_sql('car-v2', sql)[0][0]
        return result

    # 查询汽车订单：购车人信息
    def query_life_car_order_info(self, order_id):
        logging.info("——————————查询数据库——————————")
        sql = "select name,id_number,offers_type,car_info,phone from `life_car_order` WHERE id in('%s')" % order_id
        result = mydb.query_sql('car-v2', sql)[0]
        return result

    # 查询汽车订单：购车人信息
    def query_life_car_order_type(self, order_id):
        logging.info("——————————查询数据库——————————")
        sql = "select module_type_id,car_id,offers_type from `life_car_order` WHERE id in('%s')" % order_id
        result = mydb.query_sql('car-v2', sql)[0]
        return result

    # 查询二手车信息
    def query_life_car_sources(self, order_id):
        logging.info("——————————查询数据库——————————")
        sql = "select official_price,perk_price,return_points_price from `life_car_sources` WHERE id in('%s')" % order_id
        result = mydb.query_sql('car-v2', sql)[0]
        return result

    # 查询新车信息
    def query_life_car_price(self, order_id):
        logging.info("——————————查询数据库——————————")
        sql = "select official_price,xb_perk_price,return_points_price from `life_car_brand_model_versions` WHERE id in('%s')" % order_id
        result = mydb.query_sql('car-v2', sql)[0]
        return result

    def query_life_car_version_id(self, id):
        logging.info("——————————查询数据库——————————")
        sql = "select brand_model_version_id from `life_car_sources` WHERE id in('%s')" % id
        result = mydb.query_sql('car-v2', sql)[0]
        if result is None or result == '':
            return '查询数据失败，根据id查询life_car_brand_model_versions表，查询不到数据！！'
        else:
            return result[0]
    # 查询商家id
    def query_life_id(self, member_username):
        logging.info("——————————查询数据库——————————")
        sql = "select id from `life_car_merchants` WHERE member_username in('%s')" % member_username
        result = mydb.query_sql('car-v2', sql)[0]

        if result[0] is not None:
            return result[0]
        else:
            return "数据查询不到"

    def query_user(self,phone):
        sql = "select id from life_member where username in ('%s')" % phone
        result = mydb.query_sql('app', sql)
        if result == ():
            return 'false'
        else:
            return "true"
    #查询补贴详情
    def quer_perk_details(self,order_sn):
        logging.info("——————————查询数据库——————————")
        sql = "select perk_details from `life_car_order` WHERE order_code in('%s')" % order_sn
        result = mydb.query_sql('car-v2', sql)[0]

        if result[0] is not None:
            return result[0]
        else:
            return "数据查询不到"
    #查询优惠类型
    def quer_offers_type(self,order_sn):
        logging.info("——————————查询数据库——————————")
        sql = "select offers_type from `life_car_order` WHERE order_code in('%s')" % order_sn
        result = mydb.query_sql('car-v2', sql)[0]

        if result[0] is not None:
            return result[0]
        else:
            return "数据查询不到"

if __name__ == "__main__":

    phone = 13332100001
    car_id = QueryCarSql().query_life_car_sources_info(83)
    print(car_id)