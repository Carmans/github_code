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


#请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

# URL参数
key = '休闲食品'
csrf_token = 'a51821a6d744d5064082fa91d3b26915'
logid = '2583038114855184162'
temp = '1593492141433'
p=0

# 构造url
url = 'https://b2b.baidu.com/s/a?ajax=1&csrf_token={}'.format(csrf_token) + '&logid={}'.format(
    logid) + '&' + '_={}'.format(temp) + '&o=0&q={}'.format(
    key) + '&p={}'.format(p+1)+'&sa=&mk=全部结果&f=[]&s=30&adn=0&resType=product&fn={"select_param0":"品牌","select_param1":"产品类别","select_param2":"口味"}'

#请求数据
data = requests.get(url, headers=headers).content.decode('utf-8')



print('=======================返回结果==================================')
#响应结果内容
print("响应体内容的数据类型为 %s " % type(data))
print(data)


# #提取返回结果总页数和当前页数
# dispNum='\'dispNum\':(.*?)'
# dispNum=re.compile(dispNum,re.S).findall(data)
# print(dispNum)

print('=======================转化为字典==================================')
#请求结果转换为字典
jsondata = json.loads(data)

print("转换为json对象之后的数据类型为 %s " % type(jsondata))
print("转换为json对象之后的数据为 %s " % jsondata)

print('=======================提取页数==================================')
#提取返回数量
dispNum = jsondata['data']['dispNum']
print('返回数量: %s' % dispNum)

#提取当前页数
pageNum = jsondata['data']['pageNum']
print('当前页数: %s' % pageNum)


print('=======================提取商品信息==================================')
#数据解析[提取商品信息]
productList = jsondata['data']['productList']
print(type(productList))
print(productList)


#构建空列表
itemId=[]

id='"id":(.*?)'

#提取总返回的页数
for p in range(math.ceil(408 / 30)):
    # 构造url
    url = 'https://b2b.baidu.com/s/a?ajax=1&csrf_token={}'.format(csrf_token) + '&logid={}'.format(
        logid) + '&' + '_={}'.format(temp) + '&o=0&q={}'.format(
        key) + '&p={}'.format(
        p + 1) + '&sa=&mk=全部结果&f=[]&s=30&adn=0&resType=product&fn={"select_param0":"品牌","select_param1":"产品类别","select_param2":"口味"}'
    # 请求结果转换为字典
    jsondata = json.loads(data)
    temp = jsondata['data']['productList']
    id=re.compile(id,re.S).findall(jsondata)
    id = jsondata['data']['productList']['id']
    productList.extend(temp)
    itemId.extend(id)


print('=======================最终结果输出==================================')
#打印商品结果
print(type(productList))
print(len(productList))
print(productList)


#打印爬取的子页面最终结果
print(type(itemId))
print(len(itemId))
print(itemId)

