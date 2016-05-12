#!/usr/bin/env python
#-*- coding=utf-8 -*-
#如果需要用到Cookie，只用这个opener(urlopen)是不能达到目的的，
#所以我们需要创建更一般的opener来实现对Cookie的设置。
'''
cookielib模块的主要作用是提供可存储cookie的对象，
以便于与urllib2模块配合使用来访问Internet资源
利用本模块的CookieJar类的对象来捕获cookie并在后续连接请求时重新发送，
比如可以实现模拟登录功能。
该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar
它们的关系：CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar
'''
import urllib2
import cookielib
url = "http://www.baidu.com"
#1
# #声明CookieJar对象实例保存cookie
# cookie = cookielib.CookieJar()
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib2.build_opener(handler)
# #此处的open方法同urllib2的urlopen方法，也可以传入request
# req = urllib2.Request(url)
# res = opener.open(req)
# for item in cookie:
# 	print "Name = " +item.name
# 	print "Value = " +item.value

'''
Name = BAIDUID
Value = 24447063344AF34CDF551F5ACE59BB22:FG=1
Name = BIDUPSID
Value = 24447063344AF34CDF551F5ACE59BB22
Name = H_PS_PSSID
Value = 1465_18288_17946_19570_19806_19559_19807_19843_19902_15551_12083
Name = PSTM
Value = 1463038156
Name = BDSVRTM
Value = 0
Name = BD_HOME
Value = 0
'''
#以上方法是将cookie保存到了cookie这个变量中
#下面我们将提取的cookie保存到本地文件中
#2
#设置保存cookie的文件，同级目录下的cookie.txt
# filename = 'cookie.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib2.build_opener(handler)
# #创建一个请求，原理同urllib2的urlopen
# req = urllib2.Request(url)
# res = opener.open(req)
# #保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)
#ignore_discard的意思是即使cookies将被丢弃也将它保存下来
#ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入

#从文件中获取cookie并访问
#3
#创建MozillaCookieJar实例对象
# cookie = cookielib.MozillaCookieJar()
# #从文件中读取cookie内容到变量
# cookie.load('/root/pachong/cookie.txt', ignore_discard=True, ignore_expires=True)
# #创建请求的request
# req = urllib2.Request(url)
# #利用urllib2的build_opener方法创建一个opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()
#这种方式的用处：
#我们的 cookie.txt 文件中保存的是某个人登录百度的cookie，
#那么我们提取出这个cookie文件内容，就可以用以上方法模拟这个人的账号登录百度。
#4
#利用cookie模拟网站登录
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
            'stuid':'201200131012',
            'pwd':'23342321'
        })
#登录教务系统的URL
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()
