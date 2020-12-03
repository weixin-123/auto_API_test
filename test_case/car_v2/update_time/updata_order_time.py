#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/20
@File    : updata_order_time.py
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 09:28
# @Author  : lijian
# @File    : update_time.py
# @Software: PyCharm
import json

from common.log_color import LogingColor
# from test_case.app.update_time.query_car_sql import QueryCarSql
# from test_case.car_service.sql.update_sql import UpdateSql

from test_case.car_v2.login_step.use_sql import UseSql
from test_case.car_v2.update_time.time_change import TimeChange

# quer_sql = QueryCarSql()
# update_sql = UpdateSql()
log = LogingColor()
time_change = TimeChange()


class UpdateTime:
    # 结算日期：每月改为相同的一天
    def update_every_day(self, ordersn):
        # 查询优惠类型
        offers_type = UseSql().quer_offers_type(ordersn)
        if offers_type == 2:
            log.error("订单类型为【全增积分】不能更新补贴详情")
            return "Over"
        else:
            # 当前时间
            time = time_change.change_day_time_format(0)
            sql_data = UseSql().quer_perk_details(ordersn)[0]
            print("sql_data:",sql_data)
            temp_data = json.loads(sql_data)
            for i in temp_data['periods_details']:
                i['subsidy_date'] = time
            json_data = json.dumps(temp_data)
            # print("json_data",json_data)
            # 0:00-6:00
            UseSql().update_perk_details(json_data, ordersn)

    # 结算日期：每月改为部分相同
    def update_day(self, ordersn, n):
        offers_type = UseSql().quer_offers_type(ordersn)
        if offers_type == 2:
            log.error("订单类型为【全增积分】不能更新补贴详情")
            return "Over"
        else:
            time = time_change.change_day_time_format(0)
            sql_data = UseSql().quer_perk_details(ordersn)
            temp_data = json.loads(sql_data)
            i = 0
            for i in range(n):
                temp_data['periods_details'][i]['subsidy_date'] = time
            json_data = json.dumps(temp_data)
            UseSql().update_perk_details(json_data, ordersn)

    # 结算日期：每月改为每天
    def update_day_jia(self, ordersn):
        offers_type = UseSql().quer_offers_type(ordersn)
        if offers_type == 2:
            log.error("订单类型为【全增积分】不能更新补贴详情")
            return "Over"
        else:
            sql_data = UseSql().quer_perk_details(ordersn)
            temp_data = json.loads(sql_data)
            j = 0
            for i in temp_data['periods_details']:
                time = time_change.change_day_time_format(j)
                i['subsidy_date'] = time
                j = j + 1
            json_data = json.dumps(temp_data)
            UseSql().update_perk_details(json_data, ordersn)


if __name__ == "__main__":
    # UpdateTime().update_day_jia(302011171140573642)
    # UpdateTime().update_every_day(302011171140573642)
    # 订单号、修改多少天
    # UpdateTime().update_day(302011171140573642, 5)
    UpdateTime().update_every_day(212011161341014721)
