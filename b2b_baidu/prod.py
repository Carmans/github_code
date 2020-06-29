#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 19:22
# @Author  : Zhang Fei
# @Site    :
# @File    : b2b_baidu.py
# @Software: PyCharm

import requests
import re


class B2bSpider:
    def __init__(self, search_name):
        self.search = search_name
        self.url_temp = "https://b2b.baidu.com/s?q=" + search_name
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }

    # 构造URL列表
    def get_url_list(self):  # 1.构造url列表




    # 发送请求，获取响应
    def parse_url(self, url):



    # 保存html字符串
    def save_excel(self, html_str, page_num):  # 保存html字符串

    # 实现主要逻辑
    def run(self):
        # 1.构造url列表

        # 2.遍历，发送请求，获取响应

        # 3.保存


if __name__ == '__main__':
    b2bSpider = B2bSpider("休闲食品")
    b2bSpider.run()
