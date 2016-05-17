#!/usr/bin/env python
#-*- coding=utf-8 -*-
from app import app
from flask import  render_template, session, redirect, url_for,flash
from .forms import NameForm#导入forms中的表单
from flask.ext.bootstrap import Bootstrap
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

bootstrap = Bootstrap(app)

@app.errorhandler(404)#注意此处不是@app.route()
def page_not_found(e):
	return render_template('404.html'),404
@app.errorhandler(403)
def internal_server_error(e):
	return render_template('403.html'),403
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	#局部变量 name 用来存放表单中输入的有效名字，如果没有输入，其值为 None。
	form = NameForm()
	if form.validate_on_submit():
		#提交表单后，如果数据能被所有验证函数接受， 那么 validate_on_submit() 方法的返回值为 True
		#这个函数的返回值决定是重新渲染表单还是处理表单提交的数据。
		'''
		用户第一次访问程序时， 服务器会收到一个没有表单数据的 GET 请求，所以 validate_on_
		submit() 将返回 False。 if 语句的内容将被跳过，通过渲染模板处理请求，并传入表单对
		象和值为 None 的 name 变量作为参数。用户会看到浏览器中显示了一个表单。
		用户提交表单后， 服务器收到一个包含数据的 POST 请求。 validate_on_submit() 会调用
		name 字段上附属的 Required() 验证函数。如果名字不为空，就能通过验证， validate_on_
		submit() 返回 True。现在，用户输入的名字可通过字段的 data 属性获取。在 if 语句中，
		把名字赋值给局部变量 name，然后再把 data 属性设为空字符串，从而清空表单字段。最
		后一行调用 render_template() 函数渲染模板，但这一次参数 name 的值为表单中输入的名
		字，因此会显示一个针对该用户的欢迎消息。
		'''
		#name = form.name.data
		#form.name.data = ''
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<int:userid>')
def user(userid):
	user_dict = {1000:'shiluowei',1001:'sunxin'}
	if userid in user_dict:
		username = user_dict[userid]
	else:
		username = ''
	# if username:
	# 	abort(404)
	return render_template('hello.html',
		name = username)

