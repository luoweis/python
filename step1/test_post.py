#!/usr/bin/env python
# -*-  coding=utf-8 -*-
import urllib
import urllib2
#以post的方式传递需要的账户名和密码信息
values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = urllib.urlencode(values) #处理一下数据将字符串以URL编码，用于编码处理
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)#这里引用
response = urllib2.urlopen(request)
print response.read()
