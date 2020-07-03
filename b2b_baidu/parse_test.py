import re
import json

data = '''window.inquiryData = {
    ts: "1593505381",
    sign: "223500c7ee4fcb60c4b5e395e49206ec".trim()
        },
    window.data = {"query":"","iswapurl":"0","provider":{"name":"\u6881\u6eaa\u533a\u7389\u85fb\u6c47\u98df\u54c1\u5546\u884c","status":"\u8425\u4e1a\u4e2d","regCap":"","regAddr":"\u65e0\u9521\u5e02\u91d1\u6865\u526f\u98df\u54c1\u5e02\u573a8\u53f7\u697c886-888\u53f7","regData":"2016-11-17","entType":"\u4e2a\u4f53\u5de5\u5546\u6237","scope":"\u98df\u54c1\u9500\u552e\uff1b\u751f\u9c9c\u98df\u7528\u519c\u4ea7\u54c1\u3001\u6c34\u679c\u3001\u65e5\u7528\u767e\u8d27\u7684\u96f6\u552e\u3002\uff08\u4f9d\u6cd5\u987b\u7ecf\u6279\u51c6\u7684\u9879\u76ee\uff0c\u7ecf\u76f8\u5173\u90e8\u95e8\u6279\u51c6\u540e\u65b9\u53ef\u5f00\u5c55\u7ecf\u8425\u6d3b\u52a8\uff09","jumpUrl":"https:\/\/xin.baidu.com\/detail\/compinfo?pid=xlTM-TogKuTwWARI2Ivm-4jFbGJEDbrabgmd&source=1034","logo":"https:\/\/b2b.baidu.com\/static\/m\/files\/shop\/logo_default.jpg"},"tpProvider":{"name":"\u6881\u6eaa\u533a\u7389\u85fb\u6c47\u98df\u54c1\u5546\u884c","address_v2":"\u6c5f\u82cf\u65e0\u9521","from":"\u641c\u597d\u8d27\u7f51"},"resType":"","tpath":"","tp":{"name":"\u641c\u597d\u8d27\u7f51","logo":"https:\/\/b2b-amis.cdn.bcebos.com\/f9451d54885c.png","abilities":[{"title":"\u5f00\u5e97\u5165\u9a7b","slogan":"\u7531\u7231\u91c7\u8d2d\u6388\u6743\uff0c\u53ef\u63d0\u4f9b\u4ee3\u7406\u5165\u9a7b\u7231\u91c7\u8d2d\u5f00\u5e97\u670d\u52a1","jumpUrl":"https:\/\/b2b.baidu.com\/feedback?from=index_banner&ver=2"},{"title":"\u514d\u8d39\u5efa\u7ad9","slogan":"\u53cc\u5e97\u94fa\u3001\u53cc\u5b98\u7f51\u3001\u5fae\u4fe1\u5e97\u94fa\u3001\u5c0f\u7a0b\u5e8f\u5e97\u94fa\uff0c\u4e00\u952e\u5efa\u7ad9\uff0c\u5e2e\u52a9\u4f01\u4e1a\u8f7b\u677e\u89e6\u7f51","jumpUrl":"http:\/\/www.912688.com\/hhtonline\/"},{"title":"\u6548\u679c\u63a8\u5e7f","slogan":"\u5168\u7f51\u6d77\u91cf\u6d41\u91cf\u66dd\u5149\uff0c\u7cbe\u51c6\u83b7\u5ba2\uff0c\u8be2\u76d8\u63a8\u9001\u7cbe\u51c6\u53ef\u9760\uff0c\u56db\u9762\u516b\u65b9\u94fa\u8d27\u5546\u673a\uff0c\u8ba2\u5355\u8f7b\u677e\u627e\u4e0a\u95e8","jumpUrl":"https:\/\/www.912688.com\/reg1.html"}]},"item":{"id":"1aeddaf890855cca8adf86fca15c19a6","fullName":"\u6cf0\u56fd\u8fdb\u53e3 Ownace\u5965\u5a1c\u65af \u6930\u5b50\u5377\u539f\u5473\/\u9999\u8349\u547368g \u9e21\u86cb\u5377\u4f11\u95f2\u98df\u54c1","xzhid":"1571975304939142","priceList":[{"price":"11.00","priceCurrency":"\u5143","minValue":"1","maxValue":"50000","unitCode":"\u888b"}],"picUrl":null,"picList":["https:\/\/t7.baidu.com\/it\/u=2243713230,537944838&fm=199&app=68&f=JPEG?w=750&h=750&s=5C383ED74881F4D2112AA5F50300906B","https:\/\/t9.baidu.com\/it\/u=3764009045,2989960398&fm=199&app=68&f=JPEG?w=750&h=669&s=342EFE16555041C60C7EB17E0300403B","https:\/\/t9.baidu.com\/it\/u=2921129060,408301125&fm=199&app=68&f=JPEG?w=750&h=750&s=81C6EEB2454BF2EC0445C67603001076","https:\/\/t8.baidu.com\/it\/u=555595516,3752379879&fm=199&app=68&f=JPEG?w=750&h=750&s=3AAA7A23110F44EA1CD481DA0000A0B1"],"videoList":[],"fhLocation":"\u6c5f\u82cf\u7701 \u65e0\u9521\u5e02","contact_info":"TRmj1becNA0C*u0abU9Q9rjbuQEi5I-gApvr87S0*0AvnwKH-KBYm2RoZ*exyqNug8oZV0ufcbG542fmh0XLFEcoZGLNNoyrO2jcVk65IFh","hasQQ":0,"hasPhone":1,"contact":"\u6797\u5e0c","category":"\u98df\u54c1\u751f\u9c9c;\u997c\u5e72\u81a8\u5316;\u5176\u4ed6\u997c\u5e72\u81a8\u5316","brandName":"Ownace","homePage":"https:\/\/b2b-32951788404cf48.912688.com","view_times":"2","inquiry_times":"0","from":{"name":"\u641c\u597d\u8d27\u7f51","icon":"https:\/\/b2b-amis.cdn.bcebos.com\/f9451d54885c.png"},"url":"https:\/\/www.912688.com\/supply\/277729003.html?bdb2b8a2d=2583146728204533620","jumpUrl":"https:\/\/b2b.baidu.com\/b2bsearch\/jump?url=https%3A%2F%2Fwww.912688.com%2Fsupply%2F277729003.html&query=1aeddaf890855cca8adf86fca15c19a6&logid=2583146728204533620&srcId=27729&brand=Ownace&category=%E9%A3%9F%E5%93%81%E7%94%9F%E9%B2%9C%3B%E9%A5%BC%E5%B9%B2%E8%86%A8%E5%8C%96%3B%E5%85%B6%E4%BB%96%E9%A5%BC%E5%B9%B2%E8%86%A8%E5%8C%96&sv_cr=0&uign=62e50a63e2cf74b2d51b6f4e63c30ad&iid=1aeddaf890855cca8adf86fca15c19a6&timeSignOri=1593505381&xzhid=1571975304939142&miniId=8468&land=1&ii_pos=0","from_site_url":"https:\/\/www.912688.com","detail_v2":"<p><img src=\"https:\/\/t8.baidu.com\/it\/u=3640239181,3145147197&fm=199&app=68&f=JPEG?w=660&h=434&s=7FA53666094A744F48FBC67C0200403B\"\/><br\/><br\/><img src=\"https:\/\/t9.baidu.com\/it\/u=880944236,1720418684&fm=199&app=68&f=JPEG?w=660&h=144&s=58E43C72C533C0310AF04BEE0200B032\"\/><br\/><img src=\"https:\/\/t8.baidu.com\/it\/u=621424585,3389326163&fm=199&app=68&f=JPEG?w=750&h=92\"\/><br\/><img src=\"https:\/\/t8.baidu.com\/it\/u=3235587142,1740483296&fm=199&app=68&f=JPEG?w=695&h=831&s=5C00CC16C40A7EEA4AF8495F0300B0F2\"\/><br\/><br\/><br\/><br\/><img src=\"https:\/\/t8.baidu.com\/it\/u=2663684038,3719160608&fm=199&app=68&f=JPEG?w=695&h=933&s=3996E716591A46CE02F5E9680300E071\"\/><br\/><br\/><br\/><br\/><img src=\"https:\/\/t9.baidu.com\/it\/u=1815504872,1009997630&fm=199&app=68&f=JPEG?w=660&h=660&s=58383ED66881F4D2132785E50300506B\"\/><br\/><br\/><img src=\"https:\/\/t8.baidu.com\/it\/u=1518606226,3220649995&fm=199&app=68&f=JPEG?w=695&h=403&s=F1D11B700628690B62569843030060F9\"\/><br\/><br\/><img src=\"https:\/\/t8.baidu.com\/it\/u=3145209514,2998846673&fm=199&app=68&f=JPEG?w=695&h=482&s=5B86C70E4BD34CD61CE550E70300F07B\"\/><br\/><br\/><img src=\"https:\/\/t9.baidu.com\/it\/u=401643203,3700405846&fm=199&app=68&f=JPEG?w=695&h=588&s=342EFE16435241C604F2357C03004079\"\/><br\/><br\/><img src=\"https:\/\/t9.baidu.com\/it\/u=2413846274,1216461778&fm=199&app=68&f=JPEG?w=695&h=865&s=01E66EB24D46F2CE0645CA7603001076\"\/><br\/><br\/><img src=\"https:\/\/t9.baidu.com\/it\/u=2174524550,3051585395&fm=199&app=68&f=JPEG?w=660&h=660&s=F4383ED748514FC21086717403009069\"\/><br\/><br\/><img src=\"https:\/\/t7.baidu.com\/it\/u=529387554,2696624389&fm=199&app=68&f=JPEG?w=695&h=1406&s=C6C3B952151841CC18FC664A0300E0F4\"\/><br\/><br\/><br\/><br\/><br\/><img src=\"https:\/\/t8.baidu.com\/it\/u=161258488,1351894175&fm=199&app=68&f=JPEG?w=660&h=601&s=0F20960B460F61E94679D1CC0300707A\"\/><br\/><br\/><img src=\"https:\/\/t7.baidu.com\/it\/u=3352316127,1596057944&fm=199&app=68&f=JPEG?w=660&h=487&s=6795778E4E5F74C85A6DAC670300307B\"\/><br\/><img src=\"https:\/\/t9.baidu.com\/it\/u=255649919,2478798421&fm=199&app=68&f=JPEG?w=660&h=264&s=C55055990284EB05EE14F14B03007060\"\/><br\/><img src=\"https:\/\/t9.baidu.com\/it\/u=2138149799,388797502&fm=199&app=68&f=JPEG?w=660&h=102\"\/><br\/><img src=\"https:\/\/t8.baidu.com\/it\/u=546619510,4068166142&fm=199&app=68&f=JPEG?w=750&h=95\"\/><\/p><p>\u65e0\u9521\u7389\u85fb\u6c47\u5546\u8d38\u6709\u9650\u516c\u53f8\u516c\u53f8\u4e00\u76f4\u4ee5\u201c\u54c1\u8d28\u4fdd\u8bc1\u3001\u670d\u52a1\u4e13\u4e1a\u3001\u987e\u5ba2\u6ee1\u610f\u201d\u4e3a\u7ecf\u8425\u5b97\u65e8\uff0c\u4ee5\u201c\u6c42\u4ec1\u4e3a\u5927\u3001\u6c42\u5229\u4e3a\u5c0f\u3001\u771f\u6b63\u670d\u52a1\u4e3a\u4eba\u6c11\u201d\u4e3a\u7ecf\u8425\u7406\u5ff5\uff0c\u5f00\u62d3\u8fdb\u53d6\uff0c\u52a1\u5b9e\u521b\u65b0\uff0c\u5728\u505a\u597d\u7ecf\u8425\u7684\u57fa\u7840\u4e0a\uff0c\u8fd8\u4ee5\u6253\u9020\u5730\u65b9\u7279\u8272\u54c1\u724c\u4e3a\u5df1\u4efb\u3002\u5728\u591a\u5e74\u7684\u7ecf\u8425\u4e2d\uff0c\u575a\u6301\u201c\u57f9\u517b\u9ad8\u7d20\u8d28\u5458\u5de5\uff0c\u4e0d\u65ad\u4f18\u5316\u751f\u4ea7\u6280\u672f\uff0c\u7528\u54c1\u8d28\u548c\u670d\u52a1\u8ba9\u5ba2\u6237\u56de\u5934\u201d\u7684\u7ecf\u8425\u539f\u5219\uff1b\u5b9e\u884c\u54c1\u8d28\u4e3a\u5148\u3001\u5feb\u901f\u52a0\u5de5\uff0c\u4f9d\u9760\u4e13\u4e1a\u80fd\u529b\u83b7\u53d6\u516c\u5e73\u56de\u62a5\u7684\u7ecf\u8425\u7b56\u7565\u3002\u575a\u6301\u5feb\u901f\u9500\u552e\u3001\u5408\u7406\u5b9a\u4ef7\uff0c\u8981\u6c42\u9500\u552e\u4eba\u5458\u4e0e\u5ba2\u6237\u5fc3\u5bf9\u5fc3\u8054\u7edc\u3001\u9762\u5bf9\u9762\u4ea4\u6d41\u3002\u540c\u65f6\uff0c\u516c\u53f8\u575a\u6301\u89c4\u8303\u7ecf\u8425\uff0c\u4e0d\u8ffd\u6c42\u9ad8\u5229\u6da6\u7387\uff0c\u575a\u5b88\u4ef7\u503c\u5e95\u7ebf\u3001\u62d2\u7edd\u5229\u76ca\u8bf1\u60d1\uff0c\u575a\u6301\u4ee5\u4e13\u4e1a\u80fd\u529b\u4ece\u5e02\u573a\u83b7\u53d6\u516c\u5e73\u56de\u62a5\uff0c\u662f\u83b7\u5f97\u6210\u529f\u7684\u57fa\u77f3\u3002\u6b22\u8fce\u5404\u754c\u670b\u53cb\u8385\u4e34\u53c2\u89c2\u3001\u6307\u5bfc\u548c\u4e1a\u52a1\u6d3d\u8c08\u3002<br\/><img src=\"https:\/\/t9.baidu.com\/it\/u=3218649455,3672016017&fm=199&app=68&f=JPEG?w=660&h=241&s=C090AF3A8D20C011185C3DCA03007030\"\/><br\/><br\/><img src=\"https:\/\/t8.baidu.com\/it\/u=2729103178,1654697829&fm=199&app=68&f=JPEG?w=660&h=287&s=96CF48B2CCB80C8A6A4928FB0300503E\"\/><br\/><br\/><\/p>","qid":"2583146728204533620","last_update":"1586573282","lginfo":"","meta":[{"k":"\u552e\u5356\u65b9\u5f0f","v":"\u5305\u88c5"},{"k":"\u662f\u5426\u8fdb\u53e3","v":"\u662f"},{"k":"\u6e05\u771f\u98df\u54c1","v":"\u5426"},{"k":"\u539f\u4ea7\u56fd\/\u5730\u533a","v":"\u6cf0\u56fd"},{"k":"\u5546\u54c1\u6761\u5f62\u7801","v":"628055316268"},{"k":"\u54c1\u724c","v":"Ownace"},{"k":"\u539f\u6599\u4e0e\u914d\u6599","v":"\u89c1\u5305\u88c5"},{"k":"\u4fdd\u8d28\u671f","v":"180\u5929"},{"k":"\u751f\u4ea7\u65e5\u671f","v":"\u89c1\u5305\u88c5\uff08\u4e0d\u65ad\u66f4\u65b0\uff09"},{"k":"\u50a8\u85cf\u65b9\u6cd5","v":"\u653e\u4e8e\u9634\u51c9\u5e72\u71e5\u5904"},{"k":"\u51c0\u91cd","v":"68g"},{"k":"\u5305\u88c5\u89c4\u683c","v":"68g"},{"k":"\u53ef\u552e\u5356\u5730","v":"\u5168\u56fd"}],"cpaMember":0,"cpaDuration":null,"spotCertify":0,"prodTag":"\u4f11\u95f2\u98df\u54c1","sid":"7863916259743830430","productStock":0,"allowPurchase":0,"wiseQrcodeUrl":"https:\/\/b2b.baidu.com\/m\/land?id=1aeddaf890855cca8adf86fca15c19a6","wiseShopQrcodeUrl":"https:\/\/b2b.baidu.com\/m\/shop\/index?xzhid=1571975304939142&name=%E6%A2%81%E6%BA%AA%E5%8C%BA%E7%8E%89%E8%97%BB%E6%B1%87%E9%A3%9F%E5%93%81%E5%95%86%E8%A1%8C"},"sellerInfo":{"address_v2":"\u6c5f\u82cf\u65e0\u9521"}};
window.inquiryData = {
    ts: "1593505381",
    sign: "223500c7ee4fcb60c4b5e395e49206ec".trim()
        }'''

# print(type(data))
# print(data)


# dict_ret ='window.data=\{(.*?)\};window.inquiryData'
# dict_ret ='/^\{(.*?)\};$/'
# dict_ret ='window.data=\{(.*?)'






# str1 = "Hello.python";
str2 = "window.data =";
str3= 'window.inquiryData =';

print(data.index(str2));  # 结果5
# print(data[:data.index(str3):])  # 获取 "."之前的字符(不包含点)  结果 Hello
# print(data[data.index(str2):]);  # 获取 "."之前的字符(包含点) 结果.python

detail_data=data[:data.index(str3):].replace('window.data =','')

print(type(detail_data))
#
print(detail_data)

# detail_data=list(detail_data)

# print(json.loads(detail_data))

# print(detail_data)




#提取商品标签信息的正则表达式
# dict_ret = '"meta":\[(.*?)\]'
#提取返回的页面信息
# dict_ret = '"detail_v2":\"(.*?)\,"'
# alltit = re.compile(dict_ret, re.S).findall(detail_data)
#
# print(alltit)
# print(type(alltit))







# detail_data=json.loads(detail_data)
#
# print(detail_data)
#
#
# print(type(detail_data))

# detail_data.replace('window.data =','')