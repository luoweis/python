#!/usr/bin/env python
# -*- coding=utf-8 -*-
#以get明文的方式传递数据
import urllib
import urllib2
 
values={}
values['username'] = "1016903103@qq.com"
values['password']="XXXX"
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data #字符串合并
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
