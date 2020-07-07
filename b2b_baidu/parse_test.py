# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 19:22
# @Author  : Zhang Fei
# @Site    :
# @File    : b2b_baidu.py
# @Software: PyCharm
# 爱采购主表商品主页数据采集

import urllib.request
import os

url = "https://t8.baidu.com/it/u=4090963933,2936018835&fm=199&app=68&f=JPEG?w=750&h=750&s=ABA6E507121F55EB72691C690300107B="  # 图片路径。
dir = os.getcwd();  # 当前工作目录。
urllib.request.urlretrieve(url, dir + '\\result.jpeg')  # 下载图片。