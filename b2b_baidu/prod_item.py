#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 13:24
# @Author  : Zhang Fei
# @Site    : 
# @File    : b2b_Spide.py
# @Software: PyCharm


import requests
import re

# https://b2b.baidu.com/s?q=

# key = '建筑机械'
# url = 'https://b2b.baidu.com/s?q=' + key
#
# data = requests.get(url).text

# tit = '"fullName":"(.*?)"'
# alltit = re.compile(tit, re.S).findall(data)
# for item in alltit:
#     print(eval('u"' + str(item) + '"'))
#     # eval 将字符串str当成有效的表达式子来求值并返回计算结果
#     print('--------------')


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 19:22
# @Author  : Zhang Fei
# @Site    :
# @File    : b2b_baidu.py
# @Software: PyCharm

import requests
import json
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

# url='https://b2b.baidu.com/land?url=https%3A%2F%2Fwww.zhaosw.com%2Fproduct%2Fdetail%2F7284259%3Fbdb2b8a2d%3D4066725781120284134&query=%E4%BC%91%E9%97%B2%E9%A3%9F%E5%93%81&category=%E9%A3%9F%E5%93%81%E7%94%9F%E9%B2%9C%3B%E9%A5%BC%E5%B9%B2%E8%86%A8%E5%8C%96%3B%E5%A4%B9%E5%BF%83%E9%A5%BC%E5%B9%B2'

key = '休闲食品'
url = 'https://b2b.baidu.com/s?q={}'.format(key)

data = requests.get(url, headers=headers)


# print(data.text)
#
# print(data.status_code)

print(data.content.decode())


# dict_ret = json.loads(data.content.decode())

# dict_ret['window.data']


# print(dict_ret)

# 正则匹配返回的数据内容
# location = '"window.data"'
# alltit = re.compile(location, re.S).findall(dict_ret)
#
# print(alltit)


# print(data.text)
# print(data.encoding)

# print(data.url)
# print(data.encoding)
# print(data.content.decode('utf-8'))

# 正则匹配返回结果
tit = '"fullName":"(.*?)"'
# location = '"location":"(.*?)"'
alltit = re.compile(tit, re.S).findall(data)
# print(alltit)
# # alltit = re.compile(location, re.S).findall(data)
for item in alltit:
    print('标题: ' + eval('u"' + str(item) + '"'))
# print('地址: ' + eval('u"' + str(item) + '"'))
# eval 将字符串str当成有效的表达式子来求值并返回计算结果
print('--------------')


# print(url.ecode('utf-8'))

# r=requests.get(url,headers=headers)
#
#
# print(r.status_code)
# print(r.request.url)


# class B2bSpider:
#     def __init__(self, search_name):
#         self.search = search_name
#         self.url_temp = "https://b2b.baidu.com/s?q=" + search_name
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
#         }
#
#     #构造URL列表
#
#
#     #实现主要逻辑
#     def run(self):
#
#
# if __name__ == '__main__':
#     b2bSpider = B2bSpider("休闲食品")
#     b2bSpider.run()
