# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 19:22
# @Author  : Zhang Fei
# @Site    :
# @File    : b2b_baidu.py
# @Software: PyCharm
# 爱采购主表商品主页数据采集

from PIL import Image
import requests
import json
import xlwt
import math
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


# 处理图片， 输出为指定尺寸的
def produceImage(file_in, file_out):
    width = 210
    height = 210
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)


print('=======================请求商品详情页内容==================================')
for i in range(len(jUrl)):
    print(' 1   i的值为: %s:' % i)
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

    # 卖家信息
    # 联系人
    contactName = data['sellerInfo']['contactName']
    # 联系地址
    externalAddress = data['sellerInfo']['externalAddress']

    # 获取商品详情信息
    item = data['item']

    # 商品价格信息
    priceList = item['priceList']
    print('商品价格信息: %s ' % priceList)

    # 商品标题
    fullName = item['fullName']
    print('商品标题: %s ' % fullName)

    # 商品详情信息
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

    print('  2     i的值为: %s:' % i)
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

    print('商品69码: %s ' % sku)
    print('商品品牌为: %s ' % brand)

    # 提取商品图片相关的信息
    picList = item['picList']
    print('提取商品图片相关的信息: %s ' % picList)

    # 临时打印图片相关信息
    print(type(picList))
    print(len(picList))

    print('   3     i的值为: %s:' % i)
    # todo  urllib.error.HTTPError: HTTP Error 403: Forbidden 爬虫请求被拒
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

    print('   4    i的值为: %s:' % i)
    # 爬取的数据写入到excel内
    print('=======================数据写入excel,图片保存到文件夹开始==================================')

    # 创建workbook（其实就是excel，后来保存一下就行）
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建表
    worksheet = workbook.add_sheet('{}'.format(key))
    # 往单元格内写入内容:写入表头
    worksheet.write(0, 0, label="厂商名称")
    worksheet.write(0, 1, label="品牌")
    worksheet.write(0, 2, label="子品牌")
    worksheet.write(0, 3, label="商品品类1级")
    worksheet.write(0, 4, label="商品品类2级")
    worksheet.write(0, 5, label="商品名称")
    worksheet.write(0, 6, label="商品条形码")
    worksheet.write(0, 7, label="单品规格")
    worksheet.write(0, 8, label="单品计量")
    worksheet.write(0, 9, label="单品计量单位")
    worksheet.write(0, 10, label="销售规格")
    worksheet.write(0, 11, label="销售规格系数")
    worksheet.write(0, 12, label="销售指导价格")
    worksheet.write(0, 14, label="商品描述")
    worksheet.write(0, 15, label="商品详细描述")
    worksheet.write(0, 16, label="备注")
    worksheet.write(0, 17, label="箱码")
    worksheet.write(0, 18, label="箱重")
    worksheet.write(0, 19, label="箱重单位")
    worksheet.write(0, 20, label="箱容")
    worksheet.write(0, 21, label="箱容单位")
    worksheet.write(0, 22, label="保质期")

    i += 1
    print(i)
    # 写入数据到excel
    worksheet.write(i, 0, label=name)
    worksheet.write(i, 1, label=brand)
    worksheet.write(i, 2, label="")
    worksheet.write(i, 3, label="商品品类1级")
    worksheet.write(i, 4, label="商品品类2级")
    worksheet.write(i, 5, label="商品名称")
    worksheet.write(i, 6, label=sku)
    worksheet.write(i, 7, label="单品规格")
    worksheet.write(i, 8, label="单品计量")
    worksheet.write(i, 9, label="单品计量单位")
    worksheet.write(i, 10, label="销售规格")
    worksheet.write(i, 11, label="销售规格系数")
    worksheet.write(i, 12, label="销售指导价格")
    worksheet.write(i, 14, label="商品描述")
    worksheet.write(i, 15, label="商品详细描述")
    worksheet.write(i, 16, label="备注")
    worksheet.write(i, 17, label="箱码")
    worksheet.write(i, 18, label="箱重")
    worksheet.write(i, 19, label="箱重单位")
    worksheet.write(i, 20, label="箱容")
    worksheet.write(i, 21, label="箱容单位")
    worksheet.write(i, 22, label=Shelf_life)

    # 保存文件为excel
    workbook.save('爱采购爬虫.xls')

    print('=======================数据写入excel,图片保存到文件夹结束==================================')

    # 测试阶段,爬取一个商品进行测试
    # break

print('===================================================================')
