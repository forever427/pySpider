#!/usr/bin/env python
# -*-coding:utf-8-*-

import re

str = "jkjkl3242jkl32ad"

pattern = re.compile(r"\d+")

print(pattern.match(str))
print(pattern.match(str,5).group(0))
print(pattern.match(str,5).start(0))
print(pattern.match(str,5).end(0))
print(pattern.match(str,5).span(0))

str = "Hello world hello world"
# re.I是指忽略大小写进行匹配
# re.S 是指进行一个全文匹配
pattern = re.compile(r"([a-z]+) ([a-z]+)",re.I)

print(pattern.match(str).group(0))
print(pattern.match(str).group(1))
print(pattern.match(str).group(2))
print(pattern.match(str).groups())






