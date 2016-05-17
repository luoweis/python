#!/usr/bin/env python
#-*- coding=utf-8 -*-
from flask import Flask 
from flask import request
from flask import redirect
from flask import abort
from flask.ext.script import Manager
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')
app = Flask(__name__)
manager = Manager(app)
@app.route('/')
def index():
	return '<h1>早安中国</h1>'
	#return redirect('http://www.baidu.com')#重定向
@app.route('/user/<int:userid>')
def user(userid):
	users = {1000:'shiluowei',1001:'sunxin'}
	if userid in users:
		username = users[userid]
	else:
		username = ''
	if not username:
		abort(404)
	return '<h1>你好，%s!</h1>' % username

@app.route('/agent')
def agent():
	user_agent = request.headers.get('User_Agent')
	return '<p>Your browser is %s' % user_agent


if __name__ =="__main__":
	#app.run(debug=True,host='0.0.0.0')
	#app.run(host='0.0.0.0')
	manager.run()
	#python main.py runserver -h 0.0.0.0 -p080 -d

