# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 19:22
# @Author  : Zhang Fei
# @Site    :
# @File    : b2b_baidu.py
# @Software: PyCharm
# 爱采购主表商品主页数据采集

import requests
import re
import json
import xlwt
import math
import ast


data = ''' window.pageQuery = {"id":"5724818bad838937b965ce2ba24531d8"};
            window.logId = '2583023372096820602';
            window.data = null;
            window.status = '0';
            window.msg = '';'''

# print(type(data))
# print(data)


# 解析数据
str1 = "window.data =";
str2 = 'window.status =';
# # 提取返回的结果的数据信息
data = data[data.index(str1):]
print(data)

print("=============================")
# data=data.replace('window.data =', '').replace(';', '')
# data=data.index(str2)
data = data[:data.index(str2)].replace('window.data =', '').replace(';', '')

print(data)
