# 爱采购主表商品主页数据采集

import requests
import re
import json
import xlwt


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

# URL参数
key = '休闲食品'
csrf_token = 'a51821a6d744d5064082fa91d3b26915'
logid = '2583038114855184162'
temp = '1593492141433'

# 构造url
url = 'https://b2b.baidu.com/s/a?ajax=1&csrf_token={}'.format(csrf_token) + '&logid={}'.format(
    logid) + '&' + '_={}'.format(temp) + '&o=0&q={}'.format(
    key) + '&p=2&sa=&mk=全部结果&f=[]&s=30&adn=0&resType=product&fn={"select_param0":"品牌","select_param1":"产品类别","select_param2":"口味"}'

# data = requests.get(url)

#请求数据
data = requests.get(url, headers=headers)
ret = data.content.decode('utf-8')

print("响应体内容的数据类型为 %s " % type(ret))
print(ret)

#请求结果转换为字典
jsondata = json.loads(ret)

print("转换为json对象之后的数据类型为 %s " % type(jsondata))
print(jsondata)

# print(jsondata['data'])

#数据解析[提取商品信息]
temp = jsondata['data']['productList']

print(type(temp))

print(temp)

# 提取商品详情信息
# productList=jsondata.get('productList')


# productList = jsondata['productList']
#
# print(productList)
# print(type(productList))

