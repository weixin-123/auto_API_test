#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/09/23
@File    : request.py
"""
from json import loads, dumps
from json.decoder import JSONDecodeError
from demjson import encode

from requests import post, get

from common.read_base_config import ReadBaseConfig
from common.read_user_config import ReadUserConfig


class HttpRequest:
    """
    使用范例:
    from common.request import HttpRequest
    param = dict()
    param['key'] = 'value'
    HttpRequest.post("/test", json.dumps(param), 'app')
    HttpRequest.post("/test", param, 'admin')
    """

    @classmethod
    def post(cls, interface_url="", params=None, service_name=""):
        """
        可使用：商户后台，总后台，销巴商家APP，销巴生活APP，官网，内部调用inner
        :param interface_url:
        :param params: 如果使用Json.dumps自动以application/json方式请求；如果类型为dict以from-data请求
        :param service_name:store_admin:商户后台,store_app:商家APP,admin:总后台,app:销巴生活,website:官网,inner:内部调用接口
        :return:
        """
        # 获取api的url
        base_url = ReadBaseConfig().get_data('http_dev', "base_url")

        # 组装headers
        headers = dict()

        if params:
            try:
                # 如果能转成功代表是JSON类型使用
                loads(params)
                headers['Content-Type'] = 'application/json;charset=UTF8'
                headers['version'] = '2.0.3'
                headers['device'] = 'android'
            except TypeError:
                if type(params) == dict:
                    # 不传默认为from-data请求
                    pass
                else:
                    raise ValueError("您传入的[params]有误")
        service_name = str(service_name).lower()
        if service_name == "inner":
            headers['Auth-Type'] = 'inner'
        elif service_name == '':
            pass
        else:
            headers['Authorization'] = cls.get_login_token(service_name)

        # 调用接口
        print("@@@Post请求调用")
        print("请求URL：" + base_url + interface_url)
        print("请求头:" + encode(headers).encode("GBK").decode("unicode_escape"))
        print("请求参数:" + encode(params).encode("GBK").decode("unicode_escape"))
        result = post(base_url + interface_url, data=params, headers=headers)
        result_json = cls.result_processor(result)
        # result_json = result.json()

        return result_json

    @classmethod
    def get(cls, interface_url="", params=None, service_name=""):
        """
        可使用：商户后台，总后台，销巴商家APP，销巴生活APP，官网，内部调用inner
        :param interface_url:
        :param params: 如果使用Json.dumps自动以application/json方式请求；如果类型为dict以from-data请求
        :param service_name:store_admin:商户后台,store_app:商家APP,admin:总后台,app:销巴生活,website:官网,inner:内部调用接口
        :return:
        """
        # 获取api的url
        base_url = ReadBaseConfig().get_data('http_dev', "base_url")

        # 组装headers
        headers = dict()

        if params:
            try:
                # 如果能转成功代表是JSON类型使用
                loads(params)
                headers['Content-Type'] = 'application/json;charset=UTF8'

            except TypeError:
                if type(params) == dict:
                    # 不传默认为from-data请求
                    headers['Content-Type'] = 'application/json;charset=UTF8'
                else:
                    raise ValueError("您传入的[params]有误")
        service_name = str(service_name).lower()
        if service_name == "inner":
            headers['Auth-Type'] = 'inner'
        elif service_name == '':
            pass
        else:
            headers['Authorization'] = cls.get_login_token(service_name)

        # 调用接口
        print("@@@Get请求调用")
        print("请求URL：" + base_url + interface_url)
        print("请求头:" + encode(headers).encode("GBK").decode("unicode_escape"))
        print("请求参数:" + encode(params).encode("GBK").decode("unicode_escape"))
        print(params)
        result = get(base_url + interface_url, data=dumps(params), headers=headers)
        result_json = cls.result_processor(result)

        return result_json

    @classmethod
    def result_processor(cls, result):
        """
        :param result:
        :return:
        """
        request_time = result.elapsed.total_seconds()
        try:
            assert request_time <= 555555
            # assert request_time <= 15
        except AssertionError:
            print("请求响应时间：" + str(request_time))
            raise AssertionError("请求响应时间过长！")

        try:
            # 因为要测试异步事务，加入500(先不手动抛出异常)
            # assert result.status_code in [200, 401, 400, 403, 500, 502, 504]
            assert result.status_code == 200
        except AssertionError:
            print("请求响应状态码：" + str(result.status_code))
            print("返回数据:" + str(result.text[:2000]))
            raise AssertionError("请求出错！")

        try:
            result_json = result.json()
            # print("返回数据:" + str(result_json))
            print("返回数据:" + encode(result_json).encode("GBK").decode("unicode_escape"))
            return result_json
        except JSONDecodeError:
            print("返回数据:" + str(result.text[:2000]))

    @classmethod
    def get_login_token(cls, service_name):
        """
        :param service_name:
        :return: JWT token
        """
        # store_admin:商户后台,store_app:商家APP,admin:总后台,app:销巴生活,website:官网,inner:内部调用接口
        if service_name in ['store_admin', 'store_app', 'admin', 'app', 'website']:
            pass
        else:
            raise ("传入的service_name：" + service_name + "，在base_config.ini文件[http]未读取到")

        token = ReadUserConfig().get_header_token(service_name)
        return token


if __name__ == '__main__':
    test_url = '/activity/staff/turntable/express/info'
    data = {"record_id": "4"}
    # 调用接口
    response = HttpRequest.post(test_url, data, service_name="admin")
    print(response)
