#!/usr/bin/env python
#-*- coding=utf-8 -*-
import requests
import json
#现在随处可见 https 开头的网站，Requests可以为HTTPS请求验证SSL证书，
#就像web浏览器一样。要想检查某个主机的SSL证书，你可以使用 verify 参数
#12306的网站是https开头的
#想跳过刚才 12306 的证书验证，把 verify 设置为 False 即可
url = 'https://kyfw.12306.cn/otn/'
#url = 'https://github.com'
r = requests.get(url, verify=False)
print r.text