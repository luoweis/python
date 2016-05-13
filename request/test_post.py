#!/usr/bin/env python
#-*- coding=utf-8 -*-
import requests
import json
# #基本的post方法
# #最基本的传参方法可以利用 data 这个参数,post使用data参数，get使用params参数
# payload = {'name': 'shiluowei', 'passwd': '123456'}
# headers = {'User-Agent': 'Mozilla/5.0 (Linux; U) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.71 Safari/534.30'}
# r = requests.post("http://httpbin.org/post", data=payload,headers=headers)
# print r.text
# print r.url

'''
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "name": "shiluowei", 
    "passwd": "123456"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, compress", 
    "Content-Length": "28", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Linux; U) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.71 Safari/534.30"
  }, 
  "json": null, 
  "origin": "115.29.34.74", 
  "url": "http://httpbin.org/post"
}

http://httpbin.org/post
'''
'''
有时候我们需要传送的信息不是表单形式的，需要我们传JSON格式的数据过去，
所以我们可以用 json.dumps() 方法把表单数据序列化。
'''
# url = 'http://httpbin.org/post'
# payload = {'name': 'shiluowei', 'passwd': '123456'}
# headers = {'User-Agent': 'Mozilla/5.0 (Linux; U) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.71 Safari/534.30'}
# r = requests.post(url,data=json.dumps(payload),headers=headers)
# print r.text

'''
{
  "args": {}, 
  "data": "{\"passwd\": \"123456\", \"name\": \"shiluowei\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, compress", 
    "Content-Length": "41", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Linux; U) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.71 Safari/534.30"
  }, 
  "json": {
    "name": "shiluowei", 
    "passwd": "123456"
  }, 
  "origin": "115.29.34.74", 
  "url": "http://httpbin.org/post"
}
'''
url = 'http://httpbin.org/post'
file = {'file':open('test.txt','rb')}
headers = {'User-Agent': 'Mozilla/5.0 (Linux; U) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.71 Safari/534.30'}
r = requests.post(url,files=file,headers=headers)
print r.text

'''
{
  "args": {}, 
  "data": "", 
  "files": {
    "file": "hello python\n"
  }, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, compress", 
    "Content-Length": "157", 
    "Content-Type": "multipart/form-data; boundary=75a2d58b7094479082ff7630d2d95501", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Linux; U) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.71 Safari/534.30"
  }, 
  "json": null, 
  "origin": "115.29.34.74", 
  "url": "http://httpbin.org/post"
}
'''
#requests 是支持流式上传的，这允许你发送大的数据流或文件而无需先把它们读入内存。
#要使用流式上传，仅需为你的请求体提供一个类文件对象即可
# with open('massive-body') as f:
#     requests.post('http://some.url/streamed', data=f)