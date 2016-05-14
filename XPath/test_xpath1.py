#!/usr/bin/env python
#-*- coding=utf-8 -*-
from lxml import etree
# text = '''
# <div>
#     <ul>
# 		<li class="item-0"><a href="link1.html">first item</a></li>
# 		<li class="item-1"><a href="link2.html">second item</a></li>
# 		<li class="item-inactive"><a href="link3.html">third item</a></li>
# 		<li class="item-1"><a href="link4.html">fourth item</a></li>
# 		<li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
# </div>
# '''
#html = etree.HTML(text)#lxml 因为继承了 libxml2 的特性，具有自动修正 HTML 代码的功能
html = etree.parse('hello.html')#从文件读取
#result = etree.tostring(html)
result = etree.tostring(html, pretty_print=True)#从文件读取
print(result)
#首先我们使用 lxml 的 etree 库，然后利用 etree.HTML 初始化，然后我们将其打印出来
'''

<html><body><div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </li></ul>
</div>
</body></html>
不仅补全了 li 标签，还添加了 body，html 标签。

'''