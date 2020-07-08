# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 19:22
# @Author  : Zhang Fei
# @Site    :
# @File    : b2b_baidu.py
# @Software: PyCharm
# 爱采购主表商品主页数据采集



# import os
# import requests
# from PIL import Image
#
# def scale(filename, width=None, height=None):
#     """
#     指定宽或高，得到按比例缩放后的宽和高
#     :param filename:图片的绝对路径
#     :param width:目标宽度
#     :param height:目标高度
#     :return:按比例缩放后的宽和高
#     """
#     img = Image.open(filename)
#     if width != None and height != None:
#         return width, height
#     if width == None and height == None:
#         return img.size[0], img.size[1]
#     if width != None and height == None:
#         height = width * img.size[1] / img.size[0]
#         return width, height
#     if width == None and height != None:
#         width = height * img.size[0] / img.size[1]
#         return width, height


# filename = os.path.join(os.getcwd(), '2.jpg')
# filename = os.path.join(os.getcwd(), '6928872808309_0.jpg')
# print(scale(filename))  # (400, 225)
# print(scale(filename, width=221, height=221))  # (123, 456)
# print(scale(filename, width=221))  # (200, 112.5)
# print(scale(filename, height=221))  # (80.0, 45)




