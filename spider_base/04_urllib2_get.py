#!/usr/bin/env python
#-*-coding:utf-8-*-

import urllib
import urllib2

url = "http://www.baidu.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

keyword = raw_input("请输入要查询的字符串：")

wd = {"wd":keyword}

wd = urllib.urlencode(wd)

print(wd)

fullurl = url + "?" + wd

request = urllib2.Request(fullurl, headers=headers)

response = urllib2.urlopen(request)

# print(response.read())



