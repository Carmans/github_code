#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 13:24
# @Author  : Zhang Fei
# @Site    :
# @File    : b2b_Spide.py
# @Software: PyCharm
import json

data=''''{
	"query": "",
	"iswapurl": "0",
	"provider": {
		"name": "梁溪区玉藻汇食品商行",
		"status": "营业中",
		"regCap": "",
		"regAddr": "无锡市金桥副食品市场8号楼886-888号",
		"regData": "2016-11-17",
		"entType": "个体工商户",
		"scope": "食品销售；生鲜食用农产品、水果、日用百货的零售。（依法须经批准的项目，经相关部门批准后方可开展经营活动）",
		"jumpUrl": "https:\/\/xin.baidu.com\/detail\/compinfo?pid=xlTM-TogKuTwWARI2Ivm-4jFbGJEDbrabgmd&source=1034",
		"logo": "https:\/\/b2b.baidu.com\/static\/m\/files\/shop\/logo_default.jpg"
	},
	"tpProvider": {
		"name": "梁溪区玉藻汇食品商行",
		"address_v2": "江苏无锡",
		"from": "搜好货网"
	},
	"resType": "",
	"tpath": "",
	"tp": {
		"name": "搜好货网",
		"logo": "https:\/\/b2b-amis.cdn.bcebos.com\/f9451d54885c.png",
		"abilities": [{
			"title": "开店入驻",
			"slogan": "由爱采购授权，可提供代理入驻爱采购开店服务",
			"jumpUrl": "https:\/\/b2b.baidu.com\/feedback?from=index_banner&ver=2"
		}, {
			"title": "免费建站",
			"slogan": "双店铺、双官网、微信店铺、小程序店铺，一键建站，帮助企业轻松触网",
			"jumpUrl": "http:\/\/www.912688.com\/hhtonline\/"
		}, {
			"title": "效果推广",
			"slogan": "全网海量流量曝光，精准获客，询盘推送精准可靠，四面八方铺货商机，订单轻松找上门",
			"jumpUrl": "https:\/\/www.912688.com\/reg1.html"
		}]
	},
	"item": {
		"id": "1aeddaf890855cca8adf86fca15c19a6",
		"fullName": "泰国进口 Ownace奥娜斯 椰子卷原味\/香草味68g 鸡蛋卷休闲食品",
		"xzhid": "1571975304939142",
		"priceList": [{
			"price": "11.00",
			"priceCurrency": "元",
			"minValue": "1",
			"maxValue": "50000",
			"unitCode": "袋"
		}],
		"picUrl": null,
		"picList": ["https:\/\/t7.baidu.com\/it\/u=2243713230,537944838&fm=199&app=68&f=JPEG?w=750&h=750&s=5C383ED74881F4D2112AA5F50300906B", "https:\/\/t9.baidu.com\/it\/u=3764009045,2989960398&fm=199&app=68&f=JPEG?w=750&h=669&s=342EFE16555041C60C7EB17E0300403B", "https:\/\/t9.baidu.com\/it\/u=2921129060,408301125&fm=199&app=68&f=JPEG?w=750&h=750&s=81C6EEB2454BF2EC0445C67603001076", "https:\/\/t8.baidu.com\/it\/u=555595516,3752379879&fm=199&app=68&f=JPEG?w=750&h=750&s=3AAA7A23110F44EA1CD481DA0000A0B1"],
		"videoList": [],
		"fhLocation": "江苏省 无锡市",
		"contact_info": "TRmj1becNA0C*u0abU9Q9rjbuQEi5I-gApvr87S0*0AvnwKH-KBYm2RoZ*exyqNug8oZV0ufcbG542fmh0XLFEcoZGLNNoyrO2jcVk65IFh",
		"hasQQ": 0,
		"hasPhone": 1,
		"contact": "林希",
		"category": "食品生鲜;饼干膨化;其他饼干膨化",
		"brandName": "Ownace",
		"homePage": "https:\/\/b2b-32951788404cf48.912688.com",
		"view_times": "2",
		"inquiry_times": "0",
		"from": {
			"name": "搜好货网",
			"icon": "https:\/\/b2b-amis.cdn.bcebos.com\/f9451d54885c.png"
		},
		"url": "https:\/\/www.912688.com\/supply\/277729003.html?bdb2b8a2d=2583146728204533620",
		"jumpUrl": "https:\/\/b2b.baidu.com\/b2bsearch\/jump?url=https%3A%2F%2Fwww.912688.com%2Fsupply%2F277729003.html&query=1aeddaf890855cca8adf86fca15c19a6&logid=2583146728204533620&srcId=27729&brand=Ownace&category=%E9%A3%9F%E5%93%81%E7%94%9F%E9%B2%9C%3B%E9%A5%BC%E5%B9%B2%E8%86%A8%E5%8C%96%3B%E5%85%B6%E4%BB%96%E9%A5%BC%E5%B9%B2%E8%86%A8%E5%8C%96&sv_cr=0&uign=62e50a63e2cf74b2d51b6f4e63c30ad&iid=1aeddaf890855cca8adf86fca15c19a6&timeSignOri=1593505381&xzhid=1571975304939142&miniId=8468&land=1&ii_pos=0",
		"from_site_url": "https:\/\/www.912688.com",
		"detail_v2": "<p><img src="
		https: \ /\/t8.baidu.com\/it\/u=3640239181,3145147197&fm=199&app=68&f=JPEG?w=660&h=434&s=7FA53666094A744F48FBC67C0200403B"\/><br\/><br\/><img src="https:\/\/t9.baidu.com\/it\/u=880944236,1720418684&fm=199&app=68&f=JPEG?w=660&h=144&s=58E43C72C533C0310AF04BEE0200B032"\/><br\/><img src="https:\/\/t8.baidu.com\/it\/u=621424585,3389326163&fm=199&app=68&f=JPEG?w=750&h=92"\/><br\/><img src="https:\/\/t8.baidu.com\/it\/u=3235587142,1740483296&fm=199&app=68&f=JPEG?w=695&h=831&s=5C00CC16C40A7EEA4AF8495F0300B0F2"\/><br\/><br\/><br\/><br\/><img src="https:\/\/t8.baidu.com\/it\/u=2663684038,3719160608&fm=199&app=68&f=JPEG?w=695&h=933&s=3996E716591A46CE02F5E9680300E071"\/><br\/><br\/><br\/><br\/><img src="https:\/\/t9.baidu.com\/it\/u=1815504872,1009997630&fm=199&app=68&f=JPEG?w=660&h=660&s=58383ED66881F4D2132785E50300506B"\/><br\/><br\/><img src="https:\/\/t8.baidu.com\/it\/u=1518606226,3220649995&fm=199&app=68&f=JPEG?w=695&h=403&s=F1D11B700628690B62569843030060F9"\/><br\/><br\/><img src="https:\/\/t8.baidu.com\/it\/u=3145209514,2998846673&fm=199&app=68&f=JPEG?w=695&h=482&s=5B86C70E4BD34CD61CE550E70300F07B"\/><br\/><br\/><img src="https:\/\/t9.baidu.com\/it\/u=401643203,3700405846&fm=199&app=68&f=JPEG?w=695&h=588&s=342EFE16435241C604F2357C03004079"\/><br\/><br\/><img src="https:\/\/t9.baidu.com\/it\/u=2413846274,1216461778&fm=199&app=68&f=JPEG?w=695&h=865&s=01E66EB24D46F2CE0645CA7603001076"\/><br\/><br\/><img src="https:\/\/t9.baidu.com\/it\/u=2174524550,3051585395&fm=199&app=68&f=JPEG?w=660&h=660&s=F4383ED748514FC21086717403009069"\/><br\/><br\/><img src="https:\/\/t7.baidu.com\/it\/u=529387554,2696624389&fm=199&app=68&f=JPEG?w=695&h=1406&s=C6C3B952151841CC18FC664A0300E0F4"\/><br\/><br\/><br\/><br\/><br\/><img src="https:\/\/t8.baidu.com\/it\/u=161258488,1351894175&fm=199&app=68&f=JPEG?w=660&h=601&s=0F20960B460F61E94679D1CC0300707A"\/><br\/><br\/><img src="https:\/\/t7.baidu.com\/it\/u=3352316127,1596057944&fm=199&app=68&f=JPEG?w=660&h=487&s=6795778E4E5F74C85A6DAC670300307B"\/><br\/><img src="https:\/\/t9.baidu.com\/it\/u=255649919,2478798421&fm=199&app=68&f=JPEG?w=660&h=264&s=C55055990284EB05EE14F14B03007060"\/><br\/><img src="https:\/\/t9.baidu.com\/it\/u=2138149799,388797502&fm=199&app=68&f=JPEG?w=660&h=102"\/><br\/><img src="https:\/\/t8.baidu.com\/it\/u=546619510,4068166142&fm=199&app=68&f=JPEG?w=750&h=95"\/><\/p><p>无锡玉藻汇商贸有限公司公司一直以“品质保证、服务专业、顾客满意”为经营宗旨，以“求仁为大、求利为小、真正服务为人民”为经营理念，开拓进取，务实创新，在做好经营的基础上，还以打造地方特色品牌为己任。在多年的经营中，坚持“培养高素质员工，不断优化生产技术，用品质和服务让客户回头”的经营原则；实行品质为先、快速加工，依靠专业能力获取公平回报的经营策略。坚持快速销售、合理定价，要求销售人员与客户心对心联络、面对面交流。同时，公司坚持规范经营，不追求高利润率，坚守价值底线、拒绝利益诱惑，坚持以专业能力从市场获取公平回报，是获得成功的基石。欢迎各界朋友莅临参观、指导和业务洽谈。<br\/><img src="https:\/\/t9.baidu.com\/it\/u=3218649455,3672016017&fm=199&app=68&f=JPEG?w=660&h=241&s=C090AF3A8D20C011185C3DCA03007030"\/><br\/><br\/><img src="https:\/\/t8.baidu.com\/it\/u=2729103178,1654697829&fm=199&app=68&f=JPEG?w=660&h=287&s=96CF48B2CCB80C8A6A4928FB0300503E"\/><br\/><br\/><\/p>","qid":"2583146728204533620","last_update":"1586573282","lginfo":"","meta":[{"k":"售卖方式","v":"包装"},{"k":"是否进口","v":"是"},{"k":"清真食品","v":"否"},{"k":"原产国\/地区","v":"泰国"},{"k":"商品条形码","v":"628055316268"},{"k":"品牌","v":"Ownace"},{"k":"原料与配料","v":"见包装"},{"k":"保质期","v":"180天"},{"k":"生产日期","v":"见包装（不断更新）"},{"k":"储藏方法","v":"放于阴凉干燥处"},{"k":"净重","v":"68g"},{"k":"包装规格","v":"68g"},{"k":"可售卖地","v":"全国"}],"cpaMember":0,"cpaDuration":null,"spotCertify":0,"prodTag":"休闲食品","sid":"7863916259743830430","productStock":0,"allowPurchase":0,"wiseQrcodeUrl":"https:\/\/b2b.baidu.com\/m\/land?id=1aeddaf890855cca8adf86fca15c19a6","wiseShopQrcodeUrl":"https:\/\/b2b.baidu.com\/m\/shop\/index?xzhid=1571975304939142&name=%E6%A2%81%E6%BA%AA%E5%8C%BA%E7%8E%89%E8%97%BB%E6%B1%87%E9%A3%9F%E5%93%81%E5%95%86%E8%A1%8C"},"sellerInfo":{"address_v2":"江苏无锡"}
	}'''


print(type(data))

data=list(data)
print(list(data))
print(type(data))



data=json.dumps(data)
data=json.loads(data)
print(list(data))
print(type(data)


