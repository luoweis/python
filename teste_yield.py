#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author="luoweis"
def step(x):
	print "step%s" % x

def test(max):
	x = 1
	while x < max:
		yield step(x)
		x=x+1


x = test(10)

x.next()
x.next()