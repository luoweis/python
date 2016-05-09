#!/usr/bin/env python
# -*- coding=utf-8 -*-
#初学python爬虫技术使用urllib库
import urllib

#urlopen(url, data=None, proxies=None)
'''urlopen 的使用方法
url 链接
data 可以是post或get
proxies 代理
'''
url1 = "http://luoweis.testumaiw.com/home"
url2 = "http://www.163.com"
res1 = urllib.urlopen(url1)
res2 = urllib.urlopen(url2)
res1.close()#必须关闭打开的url，放置内存溢出

#print res.read()
#print res2.read()#出现乱码
#print res2.read().decode('gbk').encode('utf-8') 
#res2.close()#必须关闭打开的url
#中文字符乱码的问题解决
'''
中文乱码的问题：
注意事项：
网页中会指定编码格式，uft-8,GBK2312等，如何处理因为编码格式造成的报错呢
如网易的编码是gbk2312
<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
'''
#获取方法
#print help(res2)
#获取网页的头部信息
#print res2.info()
'''
Expires: Sat, 07 May 2016 08:29:40 GMT
Date: Sat, 07 May 2016 08:28:20 GMT
Server: nginx
Content-Type: text/html; charset=GBK#判断编码
Vary: Accept-Encoding,User-Agent,Accept
Cache-Control: max-age=80
X-Via: 1.1 hdwt39:8080 (Cdn Cache Server V2.0), 1.1 hwtxz43:7 (Cdn Cache Server V2.0)
Connection: close
'''
#获取查询的状态吗
print res2.getcode()
'''
代码 200 正常
301 永久重定向
404 网页不存在
403 禁止访问
500 服务器内部错误

'''
#获取传入的url参数
print res2.geturl()

