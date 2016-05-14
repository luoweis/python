#!/usr/bin/env python
# -*- coding=utf-8 -*-
import requests
import sys
import random
import re
from lxml import etree
reload(sys)
sys.setdefaultencoding( "utf-8" )
#解决UnicodeEncodeError: 'ascii' codec can't encode characters in position
class step_1:
	def __init__(self):
		self.url = 'https://www.zhihu.com/#signin'
		self.agent_pool = [
			{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36"},
			{"User-Agent":"Mozilla/5.0 (Linux; U) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.71 Safari/534.30"},
			{"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17"},
		]
		self.cookie = {"q_c1":"25a25fa20cca476a89a253d4df9bdfcc|1462780370000|1462780370000",
		"d_c0":"ACAApPIz5QmPTjkk8UbQ_mX0sisSA8o8drI=|1462780370",
		"_za":"5ba7f449-fe2f-4150-9d5b-6ab30bdd826a", 
		"l_n_c":"1",
		"_xsrf":"756f4188bea0bd3f0df5f31c1e35ac95",
		"l_cap_id":"Njk3YzI4MDI1MGJhNDA3NjlhYWE3MDI0ZTg2MGI1M2Q=|1463211593|681ff4917c2fa460a55420c19c86db7efb75f84f",
		"cap_i":"YzQ3YmVjNTI5ZDIyNDRlNzgwNGM0YTJmOTU0OTIwNTI=|1463211593|8d7bfc9bb3cd3e2e8a703d429342847d0c6e1fc1", 
		"_zap":"43083fa7-f709-4fbc-9716-537de3d28b49", 
		"__utmt":"1", 
		"login":"NjBlYTgwYWIzYTEwNDg5MzllNDYxZDk2NjY4YjQ1NGY=|1463211632|6dd1ff29e738d22237e02e01d61658efa2e6b6a6",
		"z_c0":"Mi4wQUJCTTdkSU5YUWtBSUFDazhqUGxDUmNBQUFCaEFsVk5jR05lVndCT2VYak1KUGFWWFUxa1UyRzNjWlY0WDBxc2hB|1463211632|03e7361a284ceca15831293e746f0bf089a49129",
		"__utma":"51854390.107561612.1462780372.1462780372.1463211596.2",
		"__utmb":"51854390.4.10.1463211596",
		"__utmc":"51854390",
		"__utmz":"51854390.1462780372.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
		"__utmv":"51854390.100-2|2=registration_date=20160124=1^3=entry_date=20160124=1",
		}
		self.save_file = 'test.html'
	def get_question_path(self):#从知乎首页中抓取question链接
		random_agent = random.choice(self.agent_pool)
		res = requests.get(self.url,cookies=self.cookie,headers=random_agent,verify=False)
		html_code = res.status_code#返回状态码
		if html_code ==200:
			html_get = res.text
			#re.findall 是找寻所有匹配的内容
			pattern = re.compile('<h2.*?href="(.*?)">(.*?)<.*?</h2>',re.S)#正则表达式是关键之处
			items = re.findall(pattern,html_get)
			return items
