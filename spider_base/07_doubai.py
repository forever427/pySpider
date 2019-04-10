#!/usr/bin/env python
# -*-coding:utf-8-*-

import urllib
import urllib2

url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1"
headers = {
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "Accept-Language" : "zh-CN,zh;q=0.9",
    "Connection" : "keep-alive",
    "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

fromdata = {
    "sort" : "U",
    "range" : "0,10",
    "tags" : "电影",
    "start" : "0",
    "genres" : "动作"
}

data = urllib.urlencode(fromdata)

request = urllib2.Request(url, data=data, headers=headers)

response = urllib2.urlopen(request)

print(response.read())


