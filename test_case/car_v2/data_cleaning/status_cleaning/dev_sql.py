#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 15:00
# @Author  : lijian
# @File    : online_sql.py
# @Software: PyCharm
import pymysql

from common.log_color import LogingColor

logging = LogingColor()


class DevSql:

    def __init__(self):
        self.db = None
        self.cursor = None

    @classmethod
    def select_db(cls, db_name):

        host ="rm-bp130dahx82uk26a0.mysql.rds.aliyuncs.com"
        username ="local_user"
        password = "dev123456!"
        port = 3306
        database = db_name
        config = {
            'host': str(host),
            'user': username,
            'passwd': password,
            'port': int(port),
            'db': database,
            'charset': 'utf8'
        }
        return config

    def connect_database(self, db_name):

        config = self.select_db(db_name)

        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
        except ConnectionError as ex:
            raise ConnectionError("数据库连接异常！" + str(ex))

    def execute_sql(self, db_name, sql_text):
        self.connect_database(db_name)
        self.cursor.execute(sql_text)
        logging.info("执行SQL：" + sql_text)
        self.db.commit()
        return self.cursor

    def query_sql(self, db_name, sql_test):
        logging.info("查询sql：" + sql_test)
        self.connect_database(db_name)
        cursor = self.db.cursor()
        cursor.execute(sql_test)
        result = cursor.fetchall()
        # 关闭游标与连接
        self.close_cursor()
        self.close_db()
        logging.info("查询数据库结果：" + str(result))
        return result

    def close_db(self):

        self.db.close()

    def close_cursor(self):

        self.cursor.close()


if __name__ == '__main__':
    # 实例化对象
    test = OnlineSql()
