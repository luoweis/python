#!/usr/bin/env python
# -*- coding=utf-8 -*-
import urllib
import urllib2 
url = "http://blog.csdn.net/cqcre"
# #url = "http://www.baidu.com"
# req = urllib2.Request(url)
# try:
# 	html_content = urllib2.urlopen(req)
# 	print html_content.read()
# except urllib2.HTTPError, e:
# 	print e.code
# 	print e.reason
# # 403
# # Forbidden
# #返回代码403 说明服务器禁止访问
'''
HTTPError的父类是URLError，根据编程经验，父类的异常应当写到子类异常的后面，
如果子类捕获不到，那么可以捕获父类的异常
'''
# req = urllib2.Request(url)
# try:
# 	html_content = urllib2.urlopen(req)
# 	print html_content.read()
# except urllib2.HTTPError, e:
# 	print e.code#只打印出403错误
# except urllib2.URLError,e:
# 	print e.reason
# else:
# 	print "OK"
# #只返回403错误
'''
如果捕获到了HTTPError，则输出code，
不会再处理URLError异常。如果发生的不是HTTPError，则会去捕获URLError异常，输出错误原因
'''
#加入 hasattr属性提前对属性进行判断
#hasattr用于确定一个对象是否具有某个属性
#hasattr(object, name) -> bool
#判断object中是否有name属性，返回一个布尔值
req = urllib2.Request(url)
try:
	html_content = urllib2.urlopen(req)
	print html_content
except urllib2.HTTPError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason
except urllib2.URLError,e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason	
else:
	print "OK"
