#!/usr/bin/env python
# -*-coding:utf-8-*-

import urllib2

proxy_handler = urllib2.ProxyHandler({"http": "110.52.235.93:9999"})
nullproxy_handler = urllib2.ProxyHandler({})

proxySwitch = True

if proxySwitch:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)

request = urllib2.Request("http://www.baidu.com")

response = opener.open(request)

print(response.read())


