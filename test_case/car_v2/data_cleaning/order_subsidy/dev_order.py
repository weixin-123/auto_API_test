#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/24
@File    : dev_order.py
"""
from common.log_color import LogingColor
from test_case.car_v2.data_cleaning.status_cleaning.dev_sql import DevSql

dev_db = DevSql()
logging = LogingColor()

begin_time = '2018-01-01'
end_time = '2020-11-20'


class DevOrderData:

    # 查询线上：订单分期金额
    # 查询补贴详情
    def dev_order(self, repay_member_id):
        logging.info("——————————查询数据库——————————")
        sql = "select order_code,pay_methods,subsidy_date,periods,subsidy_status,subsidy_money " \
              "from `life_car_order_subsidy` WHERE member_id = '%s' and" \
              " subsidy_date between '%s' and '%s' order by subsidy_date desc" % (repay_member_id,begin_time,end_time)
        result = dev_db.query_sql('car-v2', sql)[0]
        if result is None:
            logging.error("查询数据库失败，看下sql是不是写得有问题，还是数据库连错了~~~~~~~~")
            return "False"
        else:
            return result



if __name__ == '__main__':
    res=DevOrderData().dev_order(1066309)
    print(res[0])
