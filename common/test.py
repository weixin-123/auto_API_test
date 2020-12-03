#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/12
@File    : test.py
"""
from faker import Faker
f = Faker('zh_CN')
# print(f.date_between(start_date=30d, end_date=2y))
print(f.date_between(start_date=-30, end_date=2))
print(f.ssn())
print(f.pyfloat(left_digits=5,  right_digits=2, positive=False))
