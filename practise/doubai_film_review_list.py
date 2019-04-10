#!/usr/bin/env python
# -*-coding:utf-8-*-

import urllib
import urllib2


def doubaiSpider(url, beginPage, endPage):
    for page in range(beginPage, endPage + 1):
        start = (page - 1) * 20
        filename = str(page) + ".html"
        fullurl = url + str(start)
        # 开始下载HTML页面
        html = loadPage(filename, fullurl)
        # 开始保存HTML页面
        writePage(filename, html)
    print("全部保存成功，程序退出！")


def loadPage(filename, url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }

    print("正在下载" + filename + "。。。")
    request = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(request)
    print(filename + "下载完毕！")
    return html.read()


def writePage(filename, html):
    print("正在保存" + filename + "。。。")
    filename = "./html/" + filename
    f = open(filename.decode('utf-8'), 'w')
    f.write(html)
    f.close()
    print(filename + "保存完成！")
    print("=" * 30)


if __name__ == '__main__':
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入结束页："))

    url = "https://movie.douban.com/review/best/?start="
    doubaiSpider(url, beginPage, endPage)
