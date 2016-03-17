#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#抓取网易公开课下载链接 http://bbs.csdn.net/topics/390361293
#Ver :1.0
#Python 3.5.1 + BeautifulSoup 4
#eg: python 抓取网易公开课.py http://v.163.com/special/opencourse/paradigms.html
 
from bs4 import BeautifulSoup
import re
import urllib.request
import sys,os
import urllib
 
#显示百分比
def rpb(blocknum, blocksize, totalsize):
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:percent = 100
    print ("%.2f%%"% percent)
     
def downlaod(url):
    #获取页面
    html = urllib.request.urlopen(url).read()
    #用美汤来装载
    soup = BeautifulSoup(html,"html.parser")
    #获取课程信息，名称，简介等
    title = soup.find('div',{"class" : "m-cdes"})
    print (title.h2.string)
    print (title.findAll('p')[0].string)
    print (title.findAll('p')[1].string)
    print (title.findAll('p')[2].string)
 
    #获取课程详细列表信息
    detail=soup.findAll('tr',{"class" : "u-even"})
    for i in detail:
        #获取课程名称
        name=i.find('td',{"class" : "u-ctitle"}) 
        fileName=name.contents[0].strip().rstrip(',') + name.a.string.strip().rstrip(',')
        #获取课程下载链接
        downInfo=i.find('td',{"class" : "u-cdown"})
        downLink=downInfo.a['href']
         
        print (fileName)
        print (downLink)
         
        #使用urlretrieve下载该文件
        if not os.path.exists(fileName):
            urllib.request.urlretrieve(downLink,fileName+".mp4",rpb)
     
def main(argv):
    if len(argv)>=2:
         downlaod(argv[1])
 
if __name__=="__main__":
     main(sys.argv)
