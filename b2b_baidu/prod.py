# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 19:22
# @Author  : Zhang Fei
# @Site    :
# @File    : b2b_baidu.py
# @Software: PyCharm
# 爱采购主表商品主页数据采集

import urllib.request
import requests
import re
import json
import xlwt
import math
import ast
import os

# 请求头
headers = {
    "Referer": "https://b2b.baidu.com/land?url=https%3A%2F%2Fwww.zhaosw.com%2Fproduct%2Fdetail%2F7284259%3Fbdb2b8a2d%3D2583082754473465781&query=%E4%BC%91%E9%97%B2%E9%A3%9F%E5%93%81&category=%E9%A3%9F%E5%93%81%E7%94%9F%E9%B2%9C%3B%E9%A5%BC%E5%B9%B2%E8%86%A8%E5%8C%96%3B%E5%A4%B9%E5%BF%83%E9%A5%BC%E5%B9%B2",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

# URL参数
csrf_token = 'a51821a6d744d5064082fa91d3b26915'
logid = '2583038114855184162'
temp = '1593492141433'
p = 0
# key = input('请输入要爬取的内容: ')
key = '休闲食品'

# 构造url
url = 'https://b2b.baidu.com/s/a?ajax=1&csrf_token={}'.format(csrf_token) + '&logid={}'.format(
    logid) + '&' + '_={}'.format(temp) + '&o=0&q={}'.format(
    key) + '&p={}'.format(
    p + 1) + '&sa=&mk=全部结果&f=[]&s=30&adn=0&resType=product&fn={"select_param0":"品牌","select_param1":"产品类别","select_param2":"口味"}'

# 请求数据
data = requests.get(url, headers=headers).content.decode('utf-8')

print('=======================打印返回结果==================================')
# 响应结果内容
print("响应体内容的数据类型为 %s " % type(data))
print(data)

print('=======================结果转转化为字典==================================')
# 请求结果转换为字典
jsondata = json.loads(data)

print("转换为json对象之后的数据类型为 %s " % type(jsondata))
print("转换为json对象之后的数据为 %s " % jsondata)

print('=======================提取返回条数和当前所处的页数==================================')
# 提取返回数量
dispNum = jsondata['data']['dispNum']
print('返回数量: %s' % dispNum)

# 提取当前页数
pageNum = jsondata['data']['pageNum']
print('当前页数: %s' % pageNum)

print('=======================提取商品信息==================================')
# 数据解析[提取商品信息]
productList = jsondata['data']['productList']
print(type(productList))
print(productList)

# 构建空列表 存储商品详情页的请求地址
jUrl = []

# 提取总返回的页数
for p in range(math.ceil(dispNum / 30)):
    # 构造url
    url = 'https://b2b.baidu.com/s/a?ajax=1&csrf_token={}'.format(csrf_token) + '&logid={}'.format(
        logid) + '&' + '_={}'.format(temp) + '&o=0&q={}'.format(
        key) + '&p={}'.format(
        p + 1) + '&sa=&mk=全部结果&f=[]&s=30&adn=0&resType=product&fn={"select_param0":"品牌","select_param1":"产品类别","select_param2":"口味"}'
    # 请求结果转换为字典
    jsondata = json.loads(data)
    temp = jsondata['data']['productList']
    productList.extend(temp)
    # id=re.compile(id,re.S).findall(jsondata)

# itemId.extend(id)

print('=======================最终结果输出==================================')
# 打印商品结果
print(type(productList))
print(len(productList))
print(productList)

print('=======================提取ID到最终列表==================================')
# 提取商品id信息
for i in range(len(productList)):
    temp = productList[i]['jUrl']
    # print(type(id))
    # print(id)
    # itemId[i]=print(id)
    jUrl.append(temp)

# # 打印爬取的子页面最终结果
print(type(jUrl))
print(len(jUrl))
print(jUrl)

print('=======================请求商品详情页内容==================================')
for i in range(len(jUrl)):
    # print(jUrl[i])
    # 请求数据
    data = requests.get(jUrl[i], headers=headers).content.decode('utf-8')
    # print(data)

    # 解析数据
    str1 = "window.data =";
    str2 = 'window.status =';
    # # 提取返回的结果的数据信息
    data = data[data.index(str1):]
    # print(data)
    data = data[:data.index(str2)].replace('window.data =', '').replace(';', '')

    print('==============================解析的结果数据============================')
    print(data)
    data = json.loads(data)
    print(type(data))

    # 供货方信息提取
    provider = data['provider']
    print(provider)

    # 卖家信息
    sellerInfo = data['sellerInfo']
    print(sellerInfo)

    # 获取商品详情信息
    item = data['item']

    # 商品价格信息
    priceList = item['priceList']
    print('商品价格信息: %s ' % priceList)

    # 商品标题
    fullName = item['fullName']
    print('商品标题: %s ' % fullName)

    # 商品69码
    meta = item['meta']
    # 存储69码
    sku = ''
    for i in range(len(meta)):
        if meta[i]['k'] == '商品条形码':
            sku = meta[i]['v']
            break
    print('商品69码: %s ' % sku)

    # 提取商品图片相关的信息
    picList = item['picList']
    print('提取商品图片相关的信息: %s ' % picList)

    # 临时打印图片相关信息
    print(type(picList))
    print(len(picList))

    # todo  urllib.error.HTTPError: HTTP Error 403: Forbidden 爬虫请求被拒
    for i in range(len(picList)):
        # 下载图片
        os.makedirs('./image/', exist_ok=True)
        r = requests.post(picList[i], headers=headers)
        with open('./image/{}_'.format(sku)+'{}.jpg'.format(i), 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                # 图片缩放为指定大小


                f.write(chunk)
        i += 1


    # 爬取的数据写入到excel内
    print('=======================数据写入excel,图片保存到文件夹开始==================================')



    print('=======================数据写入excel,图片保存到文件夹结束==================================')

    break

print('===================================================================')
