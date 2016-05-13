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

content = get_content(url,agents)
print content
#将抓取的网页内容进行正则匹配
