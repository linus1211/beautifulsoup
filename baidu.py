#!/usr/bin/env python3
# -*- coding=utf-8 -*-
'''
@通过BeautifulSoup下载百度贴吧图片
'''
import urllib
import urllib.request
from bs4 import BeautifulSoup
#url = 'http://tieba.baidu.com/p/3537654215'
url = "http://tieba.baidu.com/p/3864539969?da_from=ZGFfbGluZT1EVCZkYV9wYWdlPTEmZGFfbG9jYXRlPXAwMDY0JmRhX2xvY19wYXJhbT0xJmRhX3Rhc2s9dGJkYSZkYV9vYmpfaWQ9MjY5MzEmZGFfb2JqX2dvb2RfaWQ9NDcwNzAmZGFfdGltZT0xNDU4MjAxMDkw&da_sign=93838b46ca09ae36aec1c7011fa7d8dd&tieba_from=tieba_da" 
# 下载网页
html = urllib.request.urlopen(url)
content = html.read()
html.close()
 
# 使用BeautifulSoup匹配图片
html_soup = BeautifulSoup(content,"html.parser")
# 图片代码我们在[Python爬虫基础1--urllib]( http://blog.xiaolud.com/2015/01/22/spider-1st/ "Python爬虫基础1--urllib")里面已经分析过了
# 相较通过正则表达式去匹配,BeautifulSoup提供了一个更简单灵活的方式
all_img_links = html_soup.findAll('img', class_='BDE_Image')
 
# 接下来就是老生常谈的下载图片
img_counter = 1
for img_link in all_img_links:
  img_name = '%s.jpg' % img_counter
  urllib.request.urlretrieve(img_link['src'],img_name)
  img_counter += 1
  print(img_name)
print (img_counter)
