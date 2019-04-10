#!/usr/bin/env python
# -*-coding:utf-8-*-

# http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule

# {"translateResult":[[{"tgt":"I'm from China","src":"我来自中国"}]],"errorCode":0,"type":"zh-CHS2en","smartResult":{"entries":["","I come from China.\r\n","I am from China.\r\n"],"type":1}}

import urllib
import urllib2

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc"
headers = {
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "Accept-Language" : "zh-CN,zh;q=0.9",
    "Connection" : "keep-alive",
    "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}
key = raw_input("Enter the words needs translated:")

fromdata = {
    "i" : key,
    "from" : "AUTO",
    "to" : "AUTO",
    "smartresult" : "dict",
    "client" : "fanyideskweb",
    "salt" : "15548151076833",
    "sign" : "303cd71231b4ff2683d847649519e377",
    "ts" : "1554815107683",
    "bv" : "94d71a52069585850d26a662e1bcef22",
    "doctype" : "json",
    "version" : "2.1",
    "keyfrom" : "fanyi.web",
    "action" : "FY_BY_CLICKBUTTION"
}

data = urllib.urlencode(fromdata)

print(data)

request = urllib2.Request(url, data=data, headers=headers)

print(urllib2.urlopen(request).read())

