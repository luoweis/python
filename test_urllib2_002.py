#!/usr/bin/env python
#-*- coding=utf-8 -*-
import urllib2
#urllib2的方法
url = 'http://blog.csdn.net/yangzhenping'
#首先定义一个请求
# req = urllib2.Request(url)#此处可以传递Headers参数，类型是字典
# req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36")
# req.add_header("GET",url)
# req.add_header("Host","blog.csdn.net")
# #Referer的重要性，有的网站如果链接不是从内部referer过来的话会屏蔽掉
# req.add_header("Referer","http://blog.csdn.net/experts.html")
# #注意此处传入的是req而不是url
# html_content = urllib2.urlopen(req).read()
# print html_content
url_headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
	"GET":url,
	"Host":"blog.csdn.net",
	"Referer":"http://blog.csdn.net/experts.html"
}
req = urllib2.Request(url,headers=url_headers)#注意此处的写法headers=url_headers
html_content = urllib2.urlopen(req).read()
#print html_content
#可以成功拿到网站信息
print req.headers.items()
'''
正式咱们传入的头信息内容
[('Host', 'blog.csdn.net'), ('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'), ('Re
ferer', 'http://blog.csdn.net/experts.html'), ('Get', 'http://blog.csdn.net/yang
zhenping')]
'''
