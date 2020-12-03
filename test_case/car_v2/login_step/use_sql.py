#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/12
@File    : use_sql.py
"""
from common.log_color import LogingColor

logging = LogingColor()
from common.connect_db import DoMysql


class UseSql:
    def use_sql_select_one(self, phone):
        """
        查询注册的电话号码是否存在
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "select id from life_member where username in ('%s')" % phone
        sql_data = DoMysql().query_sql("app", sql)

        if sql_data == ():
            logging.info("%s不是销巴会员" % phone)
            return 'false'
        else:
            logging.info("%s是销巴会员，重新生成手机号" % phone)
            return 'true'

    def use_sql_select_two(self, phone):
        """
        通过username查询对应商家的id
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "select id from life_car_merchants where member_username ='%s' " % phone
        sql_data = DoMysql().query_sql("car-v2", sql)[0][0]
        return sql_data

    def use_sql_select_three(self, phone):
        """
        查询商户id
        """
        logging.info("----------查询数据库----------")
        sql = "select id from life_car_merchants where member_username ='%s' " % phone
        sql_data = DoMysql().query_sql("car-v2", sql)[0][0]
        return sql_data


    def use_sql_select_four(self,standard_type_id):
        """
        查询车类型
        :param standard_type_id:
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "select name from life_car_types where id ='%s' " % standard_type_id
        sql_data = DoMysql().query_sql("car-v2", sql)[0][0]
        return sql_data

    def use_sql_select_five(self, module_type_id, result_name):
        """
        查询新车指导价
        :param brand_id:
        :return:
        """
        logging.info("----------查询数据库----------")
        if module_type_id == 60:
            """
            新车
            """
            sql = "select official_price from life_car_brand_model_versions where name ='%s'" % result_name
            sql_data = DoMysql().query_sql("car-v2", sql)[0][0]
            return sql_data
        else:
            """
            二手车
            """
            sql = "select official_price from life_car_sources where name ='%s'" % result_name
            sql_data = DoMysql().query_sql("car-v2", sql)[0][0]
            return sql_data

    def use_sql_select_six(self, member_username):
        """
        查询商户id
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "select id from life_car_merchants where member_username ='%s'" % member_username
        sql_data = DoMysql().query_sql("car-v2", sql)[0][0]
        return sql_data

    def use_sql_select_seven(self,phone):
        """
        充值业务
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "select id,account_id from life_member where username ='%s'" % phone
        sql_data = DoMysql().query_sql("app", sql)[0]
        # accountId = sql_data[0]
        # memberId = sql_data[1]
        return sql_data

    def quer_offers_type(self,ordersn):
        """
        获取订单类型
        :param ordersn:
        :return:
        """
        logging.info("----------查询数据库----------")
        sql = "select offers_type from life_car_order where order_code ='%s'" % ordersn
        sql_data = DoMysql().query_sql("car-v2", sql)[0]
        return sql_data

     # 查询补贴详情
    def quer_perk_details(self, order_sn):
        logging.info("——————————查询数据库——————————")
        sql = "select perk_details from `life_car_order` WHERE order_code in('%s')" % order_sn
        result = DoMysql().query_sql("car-v2", sql)[0]
        if result != {}:
            return result
        else:
            return "数据查询不到"

    # 更改补贴到账时间
    def update_perk_details(self, perk_details, orderno):
        sql = "UPDATE life_car_order set perk_details='%s'  where order_code='%s'" % (perk_details, orderno)
        DoMysql().execute_no_query('car-v2', sql)
        return "success"



if __name__ == "__main__":
    # res = Use_Sql().use_sql_select_one("000")
    # temp_res=res[0]
    # temp_res1=res[0][0]
    # print(res)
    # print(temp_res)
    # print(temp_res1)
    # data = Use_Sql().use_sql_select_two('000')
    # print(data)
    # data = UseSql().use_sql_select_four(5)
    # print(data)
    # data = UseSql().use_sql_select_five(5, 60)
    # data_two = UseSql().use_sql_select_five(5, 61)
    # print(data)
    # print(data_two)
    data = UseSql().quer_perk_details(212011161341014721)
    print(data[0])
