记录学习flask web框架的过程

开发环境使用virtualenv
*pip install flask
初始化
from flask import Flask
app = Flask(__name__)
Flask 类的构造函数只有一个必须指定的参数，即程序主模块或包的名字
在使用自身的时候，就是main，比如你执行：
python test.py
此时在test.py里面的name就是main
如果你在test2中import test,那么name就是文件名


路由和视图函数

在 Flask 程序中定义路由的最简便方式，是使用程序实例提供的 app.route 修饰器，把修
饰的函数注册为路由。
修饰器是 Python 语言的标准特性，可以使用不同的方式修改函数的行为。惯
常用法是使用修饰器把函数注册为事件的处理程序。
函数称为视图函数（ view function）

路由中的动态部分默认使用字符串，不过也可使用类型定义。例如，路由 /user/<int:id>
只会匹配动态片段 id 为整数的 URL。 Flask 支持在路由中使用 int、 float 和 path 类型。
path 类型也是字符串，但不把斜线视作分隔符，而将其当作动态片段的一部分。

线程是可单独管理的最小指令集。进程经常使用多个活动线程，有时还会共
享内存或文件句柄等资源。 多线程 Web 服务器会创建一个线程池，再从线
程池中选择一个线程用于处理接收到的请求。

重定向响应可以使用
3 个值形式的返回值生成， 也可在 Response 对象中设定。不过，由于使用频繁， Flask 提
供了 redirect() 辅助函数，用于生成这种响应

还有一种特殊的响应由 abort 函数生成，用于处理错误
如果 URL 中动态参数 id 对应的用户不存在，就返回状态码 404
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


Flask扩展
使用Flask-Script支持命令行选项
*pip install flask-script

from flask.ext.script import Manager
manager = Manager(app)

Jinja2模板引擎

templates
默认情况下， Flask 在程序文件夹中的 templates 子文件夹中寻找模板
@app.route('/user/<name>')
def user(name):
return render_template('user.html', name=name)
render_template 函
数的第一个参数是模板的文件名。 随后的参数都是键值对，表示模板中变量对应的真实
值。在这段代码中，第二个模板收到一个名为 name 的变量。
前例中的 name=name 是关键字参数，这类关键字参数很常见，但如果你不熟悉它们的话，
可能会觉得迷惑且难以理解。 左边的“ name”表示参数名，就是模板中使用的占位符；右
边的“ name”是当前作用域中的变量，表示同名参数的值

Jinja2 能识别所有类型的变量， 甚至是一些复杂的类型，例如列表、字典和对象。在模板
中使用变量的一些示例如下：
<p>A value from a dictionary: {{ mydict['key'] }}.</p>
<p>A value from a list: {{ mylist[3] }}.</p>
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
<p>A value from an object's method: {{ myobj.somemethod() }}.</p>


强大方式是模板继承

<html>
<head>
{% block head %}
<title>{% block title %}{% endblock %} - My Application</title>
{% endblock %}
</head>
<body>
{% block body %}
{% endblock %}
</body>
</html>

使用Flask-Bootstrap集成Twitter Bootstrap

*pip install flask-bootstrap
初始化 Flask-Bootstrap
from flask.ext.bootstrap import Bootstrap
# ...
bootstrap = Bootstrap(app)

初始化 Flask-Bootstrap 之后，就可以在程序中使用一个包含所有 Bootstrap 文件的基模板。
这个模板利用 Jinja2 的模板继承机制，让程序扩展一个具有基本页面结构的基模板，其中
就有用来引入 Bootstrap 的元素。

自定义错误页面
如果你在浏览器的地址栏中输入了不可用的路由，那么会显示一个状态码为 404 的错误页
面。现在这个错误页面太简陋、平庸，而且样式和使用了 Bootstrap 的页面不一致。
像常规路由一样， Flask 允许程序使用基于模板的自定义错误页面。最常见的错误代码有
两个： 404， 客户端请求未知页面或路由时显示； 500，有未处理的异常时显示。

@app.errorhandler(404)
def page_not_found(e):
return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
return render_template('500.html'), 500
和视图函数一样，错误处理程序也会返回响应。它们还返回与该错误对应的数字状态码。


url_for() 辅助函数
在模板中直接编写简单路由的 URL 链接不难，但对于包含可变部分的动态路由，在模板
中构建正确的 URL 就很困难。而且，直接编写 URL 会对代码中定义的路由产生不必要的
依赖关系。如果重新定义路由，模板中的链接可能会失效。
使用程序 URL 映射中保存的信息生成 URL。
url_for('index', _external=True)
使用 url_for() 生成动态地址时，将动态部分作为关键字参数传入。例如， url_for
('user', name='john', _external=True) 的返回结果是 http://localhost:5000/user/john。
传入 url_for() 的关键字参数不仅限于动态路由中的参数。函数能将任何额外参数添加到
查询字符串中。例如， url_for('index', page=2) 的返回结果是 /?page=2


静态文件

如何在程序的基模板中放置 favicon.ico 图标


web表单
*pip install flask-wtf
#!/usr/bin/env python
#-*- coding=utf-8 -*-
from flask import Flask, render_template, session, redirect, url_for
#from flask import request#能够返回User-Agent
from flask import abort
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

luoweis = Manager(app)
bootstrap = Bootstrap(app)

#创建表单的类
class NameForm(Form):
	name = StringField('输入你的名字?', validators=[Required()])#判断输入内容是否为空
	submit = SubmitField('Submit')
'''
StringField 构造函数中的可选参数 validators 指定一个由验证函数组成的列表，在接受
用户提交的数据之前验证数据。验证函数 Required() 确保提交的字段不为空。
'''

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

if __name__ =='__main__':
	luoweis.run()


-------------------index.html----------------------------------------
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}
{% block title %}首页{% endblock %}

{% block page_content %}
<div class="page-header">
	<h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
</div>
{{ wtf.quick_form(form) }}
{% endblock %}

----------------------------------------------------


Flash消息

---------------------------------------------------------

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

----------------------------------------------------------------------------
base.html

{% extends "bootstrap/base.html"  %}

{% block title %}{% endblock %}
{% block head %}
{{ super() }}
<link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">
{% endblock %}
{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">luoweis</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/">主页</a></li>
            </ul>
            <ul class="nav navbar-nav">
                <li><a href="#">用户</a></li>
            </ul>
        </div>
    </div>
</div>
{% endblock %}

{% block content %}
<div class="container">
	{% for message in get_flashed_messages() %}
	<div class="alert alert-warning">
		<button type="button" class="close" data-dismiss="alert">&times;</button>
		{{ message }}
	</div>
	{% endfor %}
	{% block page_content %}{% endblock %}
</div>
{% endblock %}

---------------------------------------------------------------------------
数据库
apt-get install  libxml2 libxml2-dev python-dev libpcre3 libpcre3-dev python-MySQLdb python-setuptools
现在还需要执行：
apt-get install libmysqld-dev libmysqlclient-dev
pip install mysql-python



抽象层，也称为对象关系映射（ Object-Relational Mapper， ORM）或对象文档映射（ Object-Document Mapper，
ODM）， 在用户不知觉的情况下把高层的面向对象操作转换成低层的数据库指令。
ORM 和 ODM 对生产率的提升远远超过了这一丁点儿的性能降低， 所以性能降低这个理由不足以说服用户完全放弃
ORM 和 ODM。 真正的关键点在于如何选择一个能直接操作低层数据库的抽象层，以防特定的操作需要直接使用数据库原生指令优化。
数据库框架是 Flask-SQLAlchemy（ http://pythonhosted.org/
Flask-SQLAlchemy/），这个 Flask 扩展包装了 SQLAlchemy（ http://www.sqlalchemy.org/）框架。

使用Flask-SQLAlchemy管理数据库

pip install flask-sqlalchemy
数据库引擎 URL
MySQL mysql://username:password@hostname/database
Postgres postgresql://username:password@hostname/database
SQLite（ Unix） sqlite:////absolute/path/to/database
SQLite（ Windows） sqlite:///c:/absolute/path/to/database

程序使用的数据库 URL 必须保存到 Flask 配置对象的 SQLALCHEMY_DATABASE_URI 键中。配
置对象中还有一个很有用的选项， 即 SQLALCHEMY_COMMIT_ON_TEARDOWN 键，将其设为 True
时，每次请求结束后都会自动提交数据库中的变动。


大型程序的结构
使用包和模块组织大型程序的方式
|-flasky
	|-app/
		|-templates/
		|-static/
		|-main/
			|-__init__.py
			|-errors.py
			|-forms.py
			|-views.py
		|-__init__.py
		|-email.py
		|-models.py
	|-migrations/
	|-tests/
		|-__init__.py
		|-test*.py
	|-venv/
	|-requirements.txt
	|-config.py
	|-manage.py
这种结构有 4 个顶级文件夹：
• Flask 程序一般都保存在名为 app 的包中；
• 和之前一样， migrations 文件夹包含数据库迁移脚本；
• 单元测试编写在 tests 包中；
• 和之前一样， venv 文件夹包含 Python 虚拟环境。
同时还创建了一些新文件：
• requirements.txt 列出了所有依赖包，便于在其他电脑中重新生成相同的虚拟环境；
• config.py 存储配置；
• manage.py 用于启动程序以及其他的程序任务。