#!/usr/bin/env python
#-*- coding=utf-8 -*-
import requests
import json
# url = 'http://www.baidu.com'
# r = requests.get(url)
# print r.cookies
#可以利用 cookies 变量来向服务器发送 cookies 信息
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print r.text
'''
{
  "cookies": {
    "cookies_are": "working"
  }
}
'''