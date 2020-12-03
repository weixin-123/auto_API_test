#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/09/15
@File    : connect_db.py
"""
import pymysql
import logging
from common.read_base_config import ReadBaseConfig

R = ReadBaseConfig()


class DoMysql:
    """
       为了增强代码可读性，推荐使用execute_select来执行查询语句
       """

    def __init__(self):
        self.db = None
        self.cursor = None

    @classmethod
    def select_db(cls, db_name):
        """
        :param db_name: 数据库名称
        :return: 选择数据库以及获取数据库配置信息
        """
        database_name = R.get_data('configuration', 'use_database_config')
        host = R.get_data(database_name, "host")
        username = R.get_data(database_name, "username")
        password = R.get_data(database_name, "password")
        port = R.get_data(database_name, "port")
        charset = R.get_data(database_name, "charset")
        database = db_name
        config = {
            'host': str(host),
            'user': username,
            'passwd': password,
            'port': int(port),
            'db': database,
            'charset': charset
        }
        return config

    def connect_database(self, db_name):
        """
        connect to database
        :return:
        """
        config = self.select_db(db_name)
        try:
            # 打开数据库连接   动态参数
            self.db = pymysql.connect(**config)
            # 使用cursor()方法获取操作游标
            self.cursor = self.db.cursor()
        except ConnectionError as ex:
            raise ConnectionError("数据库连接异常！" + str(ex))

    def query_sql(self, db_name, sql_test, state='all'):
        logging.info("查询sql：" + sql_test)
        self.connect_database(db_name)
        cursor = self.db.cursor()
        # 执行语句
        cursor.execute(sql_test)
        # 打印结果
        if state == 1:
            res = cursor.fetchone()  # 返回的是元组数据类型
        else:
            res = cursor.fetchall()  # 返回的是列表 针对多行数据 列表嵌套元组
        # 关闭游标与连接
        self.db.close()
        logging.info("查询数据库结果：" + str(res))
        return res

    def execute_no_query(self, db_name, sql_text):
        """
        :param db_name: 数据库名称
        :param sql_text: 查询语句，update/delete/add
        """
        # 连接数据库
        self.connect_database(db_name)
        # sql 重置索引语句
        # 执行sql语句
        self.cursor.execute(sql_text)
        print("执行SQL：" + sql_text)
        # 提交到数据库执行
        self.db.commit()
        self.cursor.close()
        # 关闭数据库连接
        self.db.close()

    def roll_back(self, db_name):
        config = self.select_db(db_name)
        try:
            # 创建一个数据库连接   动态参数
            self.db = pymysql.connect(**config)
            conn = self.db
            # 创建一个游标
            self.cursor = self.db.cursor()
            self.db.rollback()
            self.cursor.close()
            conn.commit()
            self.db.close()
        except ConnectionError as ex:
            raise ConnectionError("数据库回滚失败！" + str(ex))


if __name__ == '__main__':
    # # 索引重置
    # a = DoMysql().query_sql('car-v2',
    #                         "SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA='car-v2' AND TABLE_NAME='life_car_brands'")
    # index = a[0][0]  # 索引
    # print(index)
    # after_index = DoMysql().execute_no_query('car-v2', f"ALTER TABLE life_car_brands AUTO_INCREMENT = {index}")
    # print(after_index)
    index1 = 563
    a = DoMysql().execute_no_query('car-v2', f"ALTER TABLE life_car_brands AUTO_INCREMENT = {index1}")
    b = DoMysql().query_sql('car-v2',
                            "SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA='car-v2' AND TABLE_NAME='life_car_brands'")
    index = b[0][0]  # 索引
    print(index)
