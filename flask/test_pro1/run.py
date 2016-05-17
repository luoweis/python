#!/usr/bin/env python
#-*- coding=utf-8 -*-
from app import app
from flask.ext.script import Manager

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

luoweis = Manager(app)

if __name__ =='__main__':
	luoweis.run()