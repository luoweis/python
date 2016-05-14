#!/usr/bin/env python
# -*- coding=utf-8 -*-
import sys
import re
import step1
import redis
reload(sys)
sys.setdefaultencoding( "utf-8" )
#解决UnicodeEncodeError: 'ascii' codec can't encode characters in position

class step_2:
	def __init__(self):
		self.url = 'https://www.zhihu.com'
		self.url_question = {}
		#连接redis数据库所需要的参数
		self.RedisHost = "127.0.0.1"
		self.RedisPort = 2305
		self.RedisPassword = "991120"
		self.Redisdb = 0
	def get_question_path2(self):
		run = step1.step_1()
		res = run.get_question_path()
		for item in res:
			if '#'in item[0]:
				pattern = re.compile(r'#[\S]+')#使用正则过滤#后的内容只保留question主体路径部分
				self.url_question[self.url+re.sub(pattern,'',item[0])]=item[1]
			elif 'http' in item[0]:
				self.url_question[item[0]]=item[1]
			else:
				pass
		#return self.url_question
	def write_to_redis(self):
		#创建redis对象
		red = redis.Redis(host=self.RedisHost,port=self.RedisPort,db=self.Redisdb,password=self.RedisPassword)
		res = red.get('name')
		print res

run = step_2()
run.write_to_redis()
# dic = run.get_question_path2()
# for k ,v in dic.items():
# 	print k,v
