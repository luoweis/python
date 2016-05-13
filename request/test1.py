#!/usr/bin/env python
#-*- coding=utf-8 -*-
import requests

# #url = 'http://www.163.com'
#url = 'http://www.baidu.com'
#req = requests.get(url)#最基本的请求可以使用get方法
# print req.status_code
# print req.encoding
#print req


#requests库提供了http所有的基本请求方式
# r = requests.post("http://httpbin.org/post")
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")

# #需要加参数的话，使用params参数
# items = {'key1':'value1','key2':'value2'}
# req = requests.get(url,params=items)
# print req.url
# #返回了以下的连接
# #http://www.baidu.com/?key2=value2&key1=value1
#
#请求json文件，使用json()方法解析
#本地一个json为后缀的文件
# req = requests.get("test.json")
# #print req.text
# print req.json()

# #添加 headers，可以传 headers 参数
# payload = {'key1': 'value1', 'key2': 'value2'}
# headers = {'content-type': 'application/json'}
# r = requests.get("http://httpbin.org/get", params=payload, headers=headers)
# print r.url
# #http://httpbin.org/get?key2=value2&key1=value1
