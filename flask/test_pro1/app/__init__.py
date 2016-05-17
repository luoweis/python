#!/usr/bin/env python
#-*- coding=utf-8 -*-
from flask import Flask
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.config.from_object('config')

from app import views