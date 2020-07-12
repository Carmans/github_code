# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 19:22
# @Author  : Zhang Fei
# @Site    :
# @File    : b2b_baidu.py
# @Software: PyCharm
# 爱采购商品详情页数据解析

def get_provider(data):
    # 供货方名称
    name = data['provider']['name']
    # 供货方状态
    status = data['provider']['status']
    # 注册资本
    regCap = data['provider']['regCap']
    # 所在地址
    regAddr = data['provider']['regAddr']
    # 范围
    scope = data['provider']['scope']
    # 企业类型
    entType = data['provider']['entType']
    # 店铺链接
    jumpUrl = data['provider']['jumpUrl']
    # LOGO
    logo = data['provider']['logo']

    return name,
    status,
    regCap,
    regAddr,
    scope,
    entType,
    jumpUrl,
    logo


def get_sellerInfo(data):
    # 联系人
    contactName = data['sellerInfo']['contactName']
    # 联系地址
    externalAddress = data['sellerInfo']['externalAddress']

    return contactName, externalAddress


def get_meta(data):
    # 获取商品详情信息
    item = data['item']
    # 商品价格信息
    priceList = item['priceList']

    # 商品69码
    meta = item['meta']
    # 商品条形码
    sku = ''
    # 品牌
    brand = ''
    # 保质期
    Shelf_life = ''
    # 原产地
    place_of_origin = ''
    # 是否进口
    is_import = ''
    # 可售卖地
    Sales_area = ''
    # 等级
    level = ''
    # 品种
    varieties = ''
    # 售卖方式
    Selling_way = ''
    # 包装系列
    Packaging_series = ''
    # 产品标准号
    Product_standard_No = ''
    # 生产许可证编号
    Production_license = ''
    # 生产日期
    created = ''
    # 储藏方法
    Storage_method = ''
    # 净含量（规格）
    specifications = ''
    # 货号
    product_no = ''
    # 包装规格
    Packing_specification = ''

    for z in range(len(meta)):
        if meta[z]['k'] == '商品条形码':
            sku = meta[z]['v']
        elif meta[z]['k'] == '品牌':
            brand = meta[z]['v']
        elif meta[z]['k'] == '保质期':
            Shelf_life = meta[z]['v']
        elif meta[z]['k'] == '原产地':
            place_of_origin = meta[z]['v']
        elif meta[z]['k'] == '是否进口':
            is_import = meta[z]['v']
        elif meta[z]['k'] == '可售卖地':
            Sales_area = meta[z]['v']
        elif meta[z]['k'] == '等级':
            level = meta[z]['v']
        elif meta[z]['k'] == '品种':
            varieties = meta[z]['v']
        elif meta[z]['k'] == '售卖方式':
            Selling_way = meta[z]['v']
        elif meta[z]['k'] == '包装系列':
            Packaging_series = meta[z]['v']
        elif meta[z]['k'] == '货号':
            product_no = meta[z]['v']
        elif meta[z]['k'] == '货号':
            product_no = meta[z]['v']
        elif meta[z]['k'] == '产品标准号':
            Product_standard_No = meta[z]['v']
        elif meta[z]['k'] == '生产许可证编号':
            Production_license = meta[z]['v']
        elif meta[z]['k'] == '生产日期':
            created = meta[z]['v']
        elif meta[z]['k'] == '储藏方法':
            Storage_method = meta[z]['v']
        elif meta[z]['k'] == '净含量':
            specifications = meta[z]['v']
        elif meta[z]['k'] == '包装规格':
            Packing_specification = meta[z]['v']
        else:
            print('1')
            break

    return priceList,
    sku,
    brand,
    Shelf_life,
    place_of_origin,
    is_import,
    Sales_area,
    level,
    varieties,
    Selling_way,
    Packaging_series,
    Product_standard_No,
    Production_license,
    created,
    Storage_method,
    specifications,
    product_no,
    Packing_specification


# 提取商品详情页图片信息
def get_pic(data):
    # 获取商品详情信息
    item = data['item']
    # 提取商品图片相关的信息
    picList = item['picList']
    return picList
