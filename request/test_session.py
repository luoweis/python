#!/usr/bin/env python
#-*- coding=utf-8 -*-
import requests
import json
'''
每次请求其实都相当于发起了一个新的请求。
也就是相当于我们每个请求都用了不同的浏览器单独打开的效果。
也就是它并不是指的一个会话，即使请求的是同一个网址

'''
requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = requests.get("http://httpbin.org/cookies")
print(r.text)

'''
{
  "cookies": {}
}
很明显，这不在一个会话中，无法获取 cookies，那么在一些站点中，
我们需要保持一个持久的会话怎么办呢？就像用一个浏览器逛淘宝一样，
在不同的选项卡之间跳转，这样其实就是建立了一个长久会话
'''

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)

'''
{
  "cookies": {}
}

{
  "cookies": {
    "sessioncookie": "123456789"
  }
}
我们请求了两次，一次是设置 cookies，一次是获得 cookies
'''
#会话是一个全局的变量，那么我们肯定可以用来全局的配置了
# s = requests.Session()
# s.headers.update({'name1': 'shiluowei'})
# r = s.get('http://httpbin.org/headers', headers={'name2': 'sunxin'})
# print r.text
#s.headers.update 方法设置了 headers 的变量。然后我们又在请求中设置了一个 headers
#两个变量都传送过去了
'''
{
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, compress", 
    "Host": "httpbin.org", 
    "Name1": "shiluowei", 
    "Name2": "sunxin", 
    "User-Agent": "python-requests/2.2.1 CPython/2.7.6 Linux/3.13.0-32-generic"
  }
}
'''
#get方法传递的headers 一样会覆盖掉全局的配置
# s = requests.Session()
# s.headers.update({'name1': 'shiluowei'})
# r = s.get('http://httpbin.org/headers', headers={'name1': 'sunxin'})
# print r.text
'''
{
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, compress", 
    "Host": "httpbin.org", 
    "Name1": "sunxin",#被第二次传递的name1覆盖了 
    "User-Agent": "python-requests/2.2.1 CPython/2.7.6 Linux/3.13.0-32-generic"
  }
}
'''
#那如果不想要全局配置中的一个变量设置为 None 即可
s = requests.Session()
s.headers.update({'name1': 'shiluowei'})
r = s.get('http://httpbin.org/headers', headers={'name1': None})
print r.text