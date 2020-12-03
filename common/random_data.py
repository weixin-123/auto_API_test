#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/09/29
@File    : random_data.py
"""
import string
import random
import time

class RandomData:

    # 随机生成手机号
    @classmethod
    def phone_num(cls):
        num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187',
                     '188',
                     '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 8))
        res = start + end + '\n'
        return res

    # 随机姓名
    @classmethod
    def people_name(cls):
        first_name_list = [
            '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
            '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
            '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
            '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
            '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
            '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
            '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
        n = random.randint(0, len(first_name_list) - 1)
        f_name = first_name_list[n]
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
        val = f'{head:x}{body:x}'
        tran_str = bytes.fromhex(val).decode('gb2312')
        random_name = f_name + tran_str
        return random_name

    # 随机生成常用联系地址
    @classmethod
    def address(cls):
        city_list = ['北京市', '上海市', '天津市', '重庆市', '河北省', '邯郸市', '湖南省'
                     ]
        area_list = ['滨海新区', '两江新区', '天府新区', '江北新区', '湘江新区'
                     ]
        town_list = ['光福古镇', '乌镇', '和顺古镇', '南泉镇', '朱仙镇'
                     ]
        place_list = ['小区', '公寓', '别墅']
        # 在unicode码中, 汉字的范围是(0x4E00, 9FBF)
        address_name = chr(random.randint(0x4e00, 0x9fbf)) + chr(random.randint(0x4e00, 0x9fbf)) + random.choice(
            place_list)
        num = ''.join(random.sample(string.digits, 1)) + '单元'
        temp_address = random.choice(city_list) + random.choice(area_list) + random.choice(
            town_list) + address_name + num
        return temp_address

    # 随机生成城市地址
    @classmethod
    def city(cls):
        city_list = ['北京市', '上海市', '天津市', '重庆市', '河北省', '邯郸市', '湖南省']
        city_address = str(random.choice(city_list))
        return city_address
        # 随机抓取身份证号

    # 随机抓取有真实身份证号（一般开发是做了严格的身份校验的）
    @classmethod
    def id_card(cls):
        id_card_list = ["130928198905281793", "130532197901235712", "513221197102183838", "610523198305134774",
                        "230111197104266110", "510422198603243893", "130426198908106712", "500101198401133397",
                        "140825197508173636", "350822197101183592",
                        "451002198204238859", "542527198208281552", "440605197607137950", "610111198603217730",
                        "632223197605233250", "150981198409254695", "510704198104183738", "410181197101202157",
                        "522425198109113949", "36100119860426330X",
                        "44092319850718266X", "451121199004236209", "370725197904172667", "500382198806242961"]
        temp_num = random.choice(id_card_list)
        return temp_num

    # 随机生成比现在时间早的时间
    @classmethod
    def before_time(cls):
        a1 = (1976, 1, 1, 0, 0, 0, 0, 0, 0)
        a2 = (2000, 12, 31, 23, 59, 59, 0, 0, 0)
        start = time.mktime(a1)  # 生成开始时间戳
        end = time.mktime(a2)  # 生成结束时间戳
        # 随机生成10个日期字符串
        for i in range(1):
            t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
            date_touple = time.localtime(t)  # 将时间戳生成时间元组
            date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
            return date

    # 随机生成比现在时间晚的时间
    @classmethod
    def later_time(cls):
        a1 = (2021, 10, 1, 0, 0, 0, 0, 0, 0)
        a2 = (2025, 12, 31, 23, 59, 59, 0, 0, 0)
        start = time.mktime(a1)  # 生成开始时间戳
        end = time.mktime(a2)  # 生成结束时间戳
        # 随机生成10个日期字符串
        for i in range(1):
            t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
            date_touple = time.localtime(t)  # 将时间戳生成时间元组
            date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
            return date

if __name__ == '__main__':
    print(RandomData.phone_num())
    print(RandomData.people_name())
    print(RandomData.address())
    print(RandomData.city())
    print(RandomData.id_card())
    print(RandomData.before_time())
    print(RandomData.later_time())
