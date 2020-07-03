
import requests
import json
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

id='1aeddaf890855cca8adf86fca15c19a6'

url='https://b2b.baidu.com/land?id={}'.format(id)


#请求数据
data = requests.get(url, headers=headers)
ret = data.content.decode('utf-8')

print("响应体内容的数据类型为 %s " % type(ret))
print(ret)

#请求结果转换为字典
# jsondata = json.loads(ret)
#
# print("转换为json对象之后的数据类型为 %s " % type(jsondata))
# print(jsondata)



# dict_ret='"(\{.*?\})"'

# dict_ret='"fullName":"(.*?)"'

dict_ret ='window.data=\{(.*?)\};window.inquiryData'
alltit = re.compile(dict_ret, re.S).findall(ret)


print(alltit)
print(type(alltit))



# print(data)




# alltit = re.compile(tit,re.S).findall(data)
# for item in alltit:
#         print(eval('u"'+str(item)+'"'))
#         #eval 将字符串str当成有效的表达式子来求值并返回计算结果
#         print('--------------')





# 转换为json对象
# jsondata=json.loads(data)
#
# print(jsondata)

# 提取商品详情信息
# productList=jsondata.get('productList')
#
# print(productList)








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
