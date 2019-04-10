#!/usr/bin/env python
#-*-coding:utf-8-*-

import urllib2

# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
# Accept-Encoding: gzip, deflate, br  这个是压缩，不要写
# Accept-Language: zh-CN,zh;q=0.9
# Cache-Control: max-age=0
# Connection: keep-alive
# Cookie: BAIDUID=09C87472DCC231433D4949C397ED6431:FG=1; BIDUPSID=09C87472DCC231433D4949C397ED6431; PSTM=1554779433; delPer=0; BD_HOME=0; H_PS_PSSID=1442_21083_28774_28722_28557_28839_28584_26350_28604_28626_22157; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598
# Host: www.baidu.com
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36

# 爬虫和反爬虫的第一步，模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

request = urllib2.Request("http://www.baidu.com/",headers=headers)

response = urllib2.urlopen(request)

html = response.read()

# 状态码
print(response.getcode())
# 获取数据的实际URL，防止重定向
print(response.geturl())
# 返回HTTP响应报头
print(response.info())
# print(html)
