#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : weixin
@Time    : 2020/11/18
@File    : doller_change.py
"""
import re
use_index = {'万': 10000, '千': 0.1, '百': 0.01}

def get_price0(s):
    nums = re.findall("\d+",s)
    print('nums', nums)
    danwei = re.findall("\d+(\w)",s)
    print(danwei)
    numlen = len(nums)
    print(numlen)
    danweilen = len(danwei)
    print(danweilen)

    price = 0
    for i in range(numlen - 1):
        price +=use_index[danwei[i]] * int(nums[i])
    # 只需要判断位数是否相等，相等就直接乘，不相等就乘上一位单位
    if numlen == danweilen:
        price += use_index[danwei[-1]] * int(nums[-1])
    else:
        price += use_index[danwei[-1]] * int(nums[-1]) / 10
    return int(price)


if __name__ == '__main__':
    price = get_price0("38万")
    print(price)
