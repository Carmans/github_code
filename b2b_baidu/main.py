#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 13:24
# @Author  : Zhang Fei
# @Site    :
# @File    : b2b_Spide.py
# @Software: PyCharm

from PIL import Image
import requests
import json
import xlwt
import math
import os



def url_open(url):
    # 请求头
    headers = {
        "Referer": "https://b2b.baidu.com/land?url=https%3A%2F%2Fwww.zhaosw.com%2Fproduct%2Fdetail%2F7284259%3Fbdb2b8a2d%3D2583082754473465781&query=%E4%BC%91%E9%97%B2%E9%A3%9F%E5%93%81&category=%E9%A3%9F%E5%93%81%E7%94%9F%E9%B2%9C%3B%E9%A5%BC%E5%B9%B2%E8%86%A8%E5%8C%96%3B%E5%A4%B9%E5%BF%83%E9%A5%BC%E5%B9%B2",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }

    # 请求数据
    data = requests.get(url, headers=headers).content.decode('utf-8')

    # 请求结果转换为字典
    jsondata = json.loads(data)

    return jsondata


def get_result_nums(jsondata):
    # 提取返回数量
    dispNum = jsondata['data']['dispNum']
    # 提取当前页数
    pageNum = jsondata['data']['pageNum']
    # 数据解析[提取商品信息] 首次返回30条数据
    productList = jsondata['data']['productList']

    return dispNum, pageNum, productList


def get_item_data(dispNum, pageNum, productList):
    # 构建空列表 存储商品详情页的请求地址
    url = []

    # 提取总返回的页数
    for p in range(math.ceil(dispNum / 30)):
        # 构造url
        url = 'https://b2b.baidu.com/s/a?ajax=1&csrf_token={}'.format(csrf_token) + '&logid={}'.format(
            logid) + '&' + '_={}'.format(temp) + '&o=0&q={}'.format(
            key) + '&p={}'.format(
            p + 1) + '&sa=&mk=全部结果&f=[]&s=30&adn=0&resType=product&fn={"select_param0":"品牌","select_param1":"产品类别","select_param2":"口味"}'

        data = url_open(url)
        # 请求结果转换为字典
        jsondata = json.loads(data)
        # 提取商品列表信息到list列表
        temp = jsondata['data']['productList']
        productList.extend(temp)


def get_jUrl(productList):
    # 构建空列表 存储商品详情页的请求地址
    jUrl = []
    # 提取商品id信息
    for i in range(len(productList)):
        temp = productList[i]['jUrl']
        jUrl.append(temp)


def get_item_data(jUrl):
    for i in range(len(jUrl)):
        # 请求数据
        data = url_open(jUrl[i])

        # 解析数据
        str1 = "window.data =";
        str2 = 'window.status =';
        # # 提取返回的结果的数据信息
        data = data[data.index(str1):]
        data = data[:data.index(str2)].replace('window.data =', '').replace(';', '')
        data = json.loads(data)

        return data




def save_excel(img_url):
    for each in img_url:
        print('each is ', each)
        filename = "".join('%s' % i for i in (each.split('/')[5:9]))
        print('文件名是：', filename)
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


# 处理图片， 输出为指定尺寸的
def produceImage(file_in, file_out):
    width = 210
    height = 210
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)


def download_pic(picList):
    for j in range(len(picList)):
        # 下载图片
        os.makedirs('./image/', exist_ok=True)
        r = requests.post(picList[j], headers=headers)
        with open('./image/{}_'.format(i) + '{}_'.format(sku) + '{}.jpg'.format(j), 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)

        # 图片缩放为指定大小
        produceImage('./image/{}_'.format(i) + '{}_'.format(sku) + '{}.jpg'.format(j),
                     './image/{}_'.format(i) + '{}_'.format(sku) + '{}.jpg'.format(j))

        j += 1


if __name__ == '__main__':
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

    download_pic()
