#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/24
@File    : online_order.py
"""
from common.log_color import LogingColor
from test_case.car_v2.data_cleaning.status_cleaning.online_sql import OnlineSql

online_db = OnlineSql()
logging = LogingColor()

start_time = '2020.08.01 00:00:00'
end_time = '2020.11.20 17:00:00'

class OnlineOrderData:

    # 查询线上  还款会员用户id
    def query_online_repay_member_id(self):
        sql_status = "SELECT repay_member_id from life_car_installment_repayments t1 JOIN " \
                     "(SELECT RAND() * (SELECT MAX(id) FROM life_car_contract_installment) AS nid) t2 " \
                     "ON t1.id > t2.nid LIMIT 1"
        online_member_id = online_db.query_sql('car', sql_status)[0][0]
        print(online_member_id)
        if online_member_id is None:
            OnlineOrderData().query_online_repay_member_id()
        else:
            # print('online_member_id:', online_member_id)
            return online_member_id

    # 查询线上  # real_channel '还款类型：1银行卡 2余额宝'
    # # bill_date 账单日期
    # # period 第几期
    # # status 还款状态
    # # bill_amount 账单金额
    # # repayment_amount 还款金额
    def query_online_order_detail(self, repay_member_id):
        sql = "SELECT real_channel,bill_date,period,status,bill_amount " \
              "from life_car_installment_repayments" \
              " where repay_member_id = '%s' and bill_date between '%s' and '%s' order by bill_date desc" % (repay_member_id,start_time,end_time)
        sql_data = online_db.query_sql('car', sql)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        else:
            return sql_data

    # 查询线上  订单号
    def query_online_order_id(self, online_repay_member_id):
        sql = "SELECT ordersn from life_car_orders where member_id = '%s'" % online_repay_member_id
        sql_data = online_db.query_sql('car', sql)
        print(sql_data)
        if sql_data == "" or sql_data is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        else:
            return sql_data[0][0]


if __name__ == '__main__':
    # online_repay_member_id = OnlineOrderData().query_online_repay_member_id()
    a = OnlineOrderData().query_online_order_id(1066309)
    #OnlineOrderData().query_online_order_id(online_repay_member_id)[0]
    print(a)


