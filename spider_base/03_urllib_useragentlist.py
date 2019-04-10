#!/usr/bin/env python
#-*-coding:utf-8-*-

import urllib2
import random

# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
# Accept-Encoding: gzip, deflate, br  这个是压缩，不要写
# Accept-Language: zh-CN,zh;q=0.9
# Cache-Control: max-age=0
# Connection: keep-alive
# Cookie: BAIDUID=09C87472DCC231433D4949C397ED6431:FG=1; BIDUPSID=09C87472DCC231433D4949C397ED6431; PSTM=1554779433; delPer=0; BD_HOME=0; H_PS_PSSID=1442_21083_28774_28722_28557_28839_28584_26350_28604_28626_22157; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598
# Host: www.baidu.com
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36

url = "http://www.baidu.com/"

ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
]

# 随机选择一个
user_agent = random.choice(ua_list)

request = urllib2.Request(url)

request.add_header("User-Agent",user_agent)

print(request.get_header("User-agent"))
