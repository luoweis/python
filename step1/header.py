#!/usr/bin/env python
#-*- coding=utf-8 -*-
#通过header中的信息获取网页声明的编码格式
import urllib
url_list = ["http://www.163.com","http://www.jd.com","http://www.baidu.com","http://www.youku.com"]
for url in url_list:
    print url
    html_info = urllib.urlopen(url).info()
    # print html_info
    # print dir(html_info)
    #参看html_info中的方法
    '''
    ['__contains__', '__delitem__', '__doc__', '__getitem__', '__init__', '__iter__', '__len__', 
 '__module__', '__setitem__', '__str__', 'addcontinue', 'addheader', 'dict', 'encodingheader',
 'fp', 'get', 'getaddr', 'getaddrlist', 'getallmatchingheaders', 'getdate', 'getdate_tz', 
 'getencoding', 'getfirstmatchingheader', 'getheader', 'getheaders', 'getmaintype', 'getparam', 
 'getparamnames', 'getplist', 'getrawheader', 'getsubtype', 'gettype', 'has_key', 'headers',
  'iscomment', 'isheader', 'islast', 'items', 'keys', 'maintype', 'parseplist', 'parsetype', 
  'plist', 'plisttext', 'readheaders', 'rewindbody', 'seekable', 'setdefault', 'startofbody', 
  'startofheaders', 'status', 'subtype', 'type', 'typeheader', 'unixfrom', 'values']
    '''
    print html_info.getparam('charset')
    #直接输出http://www.163.com的编码格式为GBK
