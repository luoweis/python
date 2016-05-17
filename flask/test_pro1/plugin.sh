#!/bin/bash

venv/bin/pip install flask
venv/bin/pip install flask-login
venv/bin/pip install flask-openid
venv/bin/pip install flask-mail
venv/bin/pip install flask-sqlalchemy
venv/bin/pip install sqlalchemy-migrate
venv/bin/pip install flask-whooshalchemy
venv/bin/pip install flask-wtf
venv/bin/pip install flask-babel
venv/bin/pip install guess_language
venv/bin/pip install flipflop
venv/bin/pip install coverage


mkdir app
mkdir app/static
mkdir app/templates
mkdir tmp

touch app/__init__.py