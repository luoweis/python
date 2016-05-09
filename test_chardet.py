#!/usr/bin/env python
#-*- coding=utf-8 -*-
#采用第三方模块 chardet 需要到网上下载
#https://pypi.python.org/pypi/chardet
import urllib
#字符集检测
import chardet
urls = [
"http://www.163.com",
"http://www.umaiw.com/",
"http://www.umyidian.com/"
]
# html_content = urllib.urlopen(url).read()

# res = chardet.detect(html_content)
#{'confidence': 0.99, 'encoding': 'GB2312'}有99%的概率编码格式是gb2312，是一个字典类型
#print res["encoding"]
#这个第三方模块还是单独检测某个字符串
#print chardet.detect("我是施罗伟")
#{'confidence': 0.9690625, 'encoding': 'utf-8'}
#可以将这个模块封装成函数方法
def automatic_detect(url):
	'''info'''
	html_content = urllib.urlopen(url).read()
	res = chardet.detect(html_content)
	encoding = res["encoding"]
	return encoding

# print url,automatic_detect(url)
#后期可以使用多线程的方式同时处理多个url
for url in urls:
	print url,automatic_detect(url)
