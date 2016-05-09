#!/usr/bin/env python
#-*- coding=utf-8 -*-
'''
urllib2属于一个进阶的爬虫爬取模块，扩展了很多方法
random的choice()方法
模仿用户，模仿使用浏览器访问网页的行为
解读我们请求的Header信息的重要性，（不是服务器的头信息）
代码的复用，封装，异常处理
'''
import urllib
#urllib的升级版本
import urllib2
#csdn 博客的网页
# url = "http://blog.csdn.net/wushge11/article/details/51352359"
# #html_content = urllib.urlopen(url).read()
# #print html_content

# print  urllib.urlopen(url).getcode()
#返回403
#会返回一个403的错误页面，表示该url不让抓取
# <html>
# <head><title>403 Forbidden</title></head>
# <body bgcolor="white">
# <center><h1>403 Forbidden</h1></center>
# <hr><center>nginx</center>
# </body>
# </html>
'''
http://www.taobao.com/robots.txt
参看淘宝的robots.txt文本
User-agent: Baiduspider#禁止百度的爬虫
Disallow: /
Disallow: /product
Disallow: /market
Allow: /article
Allow: /wenzhang
Allow: /tbsitemap
Allow: /oshtml


http://www.jd.com/robots.txt

User-agent: *
Disallow: /?*#所有动态页面
Disallow: /pop/*.html
Disallow: /pinpai/*.html?*
User-agent: EtaoSpider
Disallow: /
User-agent: YisouSpider
Disallow: /
User-agent: HuihuiSpider
Disallow: /
User-agent: 360Spider
Disallow: /
User-agent: GwdangSpider
Disallow: /
User-agent: WochachaSpider
Disallow: /
'''

# url = 'http://blog.csdn.net/wushge11/article/details/51352359'
# html_content = urllib2.urlopen(url).read()
# print html_content
#urllib2.HTTPError: HTTP Error 403: Forbidden
#网站对蜘蛛进行了限制
#通过模仿正常用户进行抓取
url = 'http://blog.csdn.net/yangzhenping'
#首先定义一个请求
req = urllib2.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36")
req.add_header("GET",url)
req.add_header("Host","blog.csdn.net")
#Referer的重要性，有的网站如果链接不是从内部referer过来的话会屏蔽掉
req.add_header("Referer","http://blog.csdn.net/experts.html")
#注意此处传入的是req而不是url
html_content = urllib2.urlopen(req).read()
print html_content
'''
成功拿到网页的内容
    <title>每一天都有新的希望
        - 博客频道 - CSDN.NET</title>
'''
