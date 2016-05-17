#!/usr/bin/env python
#-*- coding=utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

#创建表单的类
class NameForm(Form):#需要import进views.py中 'from .forms import NameForm'
	name = StringField('输入你的名字?', validators=[Required()])#判断输入内容是否为空
	submit = SubmitField('Submit')
'''
StringField 构造函数中的可选参数 validators 指定一个由验证函数组成的列表，在接受
用户提交的数据之前验证数据。验证函数 Required() 确保提交的字段不为空。
'''