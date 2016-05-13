#!/usr/bin/env python
#-*- coding=utf-8 -*-
#函数封装一个传入url和Header的方法，来抓取url的内容
import urllib2
import random

agents = [
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
"Mozilla/5.0 (Linux; U) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.71 Safari/534.30",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17",
]

url = 'http://blog.csdn.net/yangzhenping'

def get_content(url,input_agents):
	random_agent = random.choice(input_agents)
	req = urllib2.Request(url)
	req.add_header("User-Agent",random_agent)
	req.add_header("GET",url)
	req.add_header("Host","blog.csdn.net")
	req.add_header("Referer","http://blog.csdn.net/experts.html")
	html_content = urllib2.urlopen(req).read()
	#print req.headers.items()
	return html_content




print get_content(url,agents)
