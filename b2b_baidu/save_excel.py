#采集的数据保存到excel
import xlwt

features= {'word': '路边', 'age': 18}

# 创建workbook（其实就是excel，后来保存一下就行）
workbook = xlwt.Workbook(encoding='utf-8')
# 创建表
worksheet = workbook.add_sheet('sheet1')
# 往单元格内写入内容:写入表头
worksheet.write(0, 0, label="word")
worksheet.write(0, 1, label="frequency")
# 往单元格内写入内容:写入内容
i = 1
for word in features:
    worksheet.write(i, 0, label=features[word])
    worksheet.write(0, 1, label=features[age])
    i = i + 1
workbook.save('Excel_Workbook.xls')



# 将爬取结果输出到excel内进行保存
# workbook = xlwt.Workbook(encoding='utf-8')
#
# worksheet = workbook.add_sheet('{}'.format(key))  # 创建一个Excel,在其中创建一个名为first的sheet

# worksheet.write(0, 0, label="word")
# worksheet.write(0, 1, label="frequency")

#
# for item in temp:
#     print(item)
    # print(len(item))
    # print(item['id'])
    # worksheet.write(j, i, label=item[item_1])
    # for num in range(len(item[0])):
    #     # 行、列、值
    #     worksheet.write(item[0], num, item[1][num])

# # print(item_1)
#     # print(item[item_1])
#     print(len(item_1))
# 遍历商品详情信息,提取商品主页的具体信息


# for item_1 in item:
#     print(item_1)
#     i += 1
#

# 往单元格内写入内容:写入表头
# i=0
# j=0
#
# # j += 1
# for item_1 in item:
#     print(item_1)
#     print(item[item_1])
#     # print(len(item_1))
#     # worksheet.write(0, i, label=item_1)
#     # j += 1
#     # worksheet.write(j, i, label=item[item_1])
#     i += 1


# 保存文件为excel
# workbook.save('爱采购爬虫.xls')




# coding=utf-8
import xlwt
import xlrd


# 创建excel文件
filename = xlwt.Workbook()
# 给工作表命名，test
sheet = filename.add_sheet("test")
# 写入内容，第4行第3列写入‘张三丰’
hello = u'张三丰'
hello1 = u'张四丰'
sheet.write(0, 0, hello)
sheet.write(0, 1, hello1)
# 指定存储路径，如果当前路径存在同名文件，会覆盖掉同名文件
filename.save("./test1.xls")