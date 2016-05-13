#!/usr/bin/env python
#-*- coding=utf-8 -*-
__auth = 'luoweis'
import urllib2
import re
import random
import chardet#检测网页编码格式，防止出现乱码

page = 1

url = 'http://www.qiushibaike.com/hot/page/' + str(page)
#url = 'http://www.163.com'
#伪造的User-Agent
agents = [
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
"Mozilla/5.0 (Linux; U) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.71 Safari/534.30",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17",
]


def get_content(url,input_agents):
	random_agent = random.choice(input_agents)
	try:
		req = urllib2.Request(url)
		req.add_header("User-Agent",random_agent)
		#req.add_header("GET",url)
		#req.add_header("Host","blog.csdn.net")
		#req.add_header("Referer","http://blog.csdn.net/experts.html")
		html_content = urllib2.urlopen(req).read()
		res = chardet.detect(html_content)
		encoding = res["encoding"]
		if encoding =='utf-8':
			return html_content
		if encoding == 'GB2312':
			html_content = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')#对gbk格式转换成utf8
			return html_content
		else:
			print ("编码格式有误 网页编码格式为：%s" % (encoding))
	except urllib2.URLError,e:
		if hasattr(e,'code'):
			print e.code
		if hasattr(e,'reason'):
			print e.reason

html_content = get_content(url,agents)
#print html_content
#将抓取的网页内容进行正则匹配
#re.findall 是找寻所有匹配的内容
pattern = re.compile('<div.*?author.*?">.*?<a.*?<img.*?</a>.*?<a.*?href="(.*?)".*?target.*?title="(.*?)">.*?'+
	'.*?content">(.*?)</div>.*?',re.S)#正则表达式是关键之处
items = re.findall(pattern,html_content)
#print items
prefix='http://www.qiushibaike.com'
for item in items:
	print item[0],item[1],item[2]

'''
测试结果：
/users/27744140/ 看了三年才有账号 

lz带五岁儿子第一次坐船，旅游观光那种，儿子趴着栏杆看大海，lz全程拽着儿子衣服后，怕出现危险!<br/><br/>儿子:“爸爸 ! 你很害怕坐船吗？ 不要这么紧张呀 !…… ”


/users/12995077/ 清眸、、 

今天是奶奶九十岁生日，从小跟着奶奶长大，不求别的，在大糗百为奶奶求个祝福，您的健康是我最大的幸福……


/users/31583217/ 都是逼哪里来美丑 

一个真正的课代表，敢于面对老师质疑的目光，勇于面对同学们希冀的眼神，愣是把30本作业说成60本！<br/>有了你学习变得轻松了许多。
'''
