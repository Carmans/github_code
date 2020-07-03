# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 19:22
# @Author  : Zhang Fei
# @Site    :
# @File    : b2b_baidu.py
# @Software: PyCharm
# 爱采购主表详情页数据采集

import requests
import json
import re

#构造请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

#商品id
prod_id='1aeddaf890855cca8adf86fca15c19a6'

#构造URL列表
url='https://b2b.baidu.com/land?id={}'.format(prod_id)

#请求数据
data = requests.get(url, headers=headers).content.decode('utf-8')

#查询返回的相应体的数据类型
print("响应体内容的数据类型为 %s " % type(data))
#查看返回的结果数据
print(data)

#解析数据
str1 = "window.data =";
str2= 'window.status =';

#提取关键的数据信息
# data=data[:data.index(str2):].replace('window.data =','')


print('--------------------------------------------------------------------------------')
#提取返回的结果的数据信息
data=data[data.index(str1):]
data=data[:data.index(str2)].replace('window.data =','')

data=list(data)

print(type(data))
print(data)