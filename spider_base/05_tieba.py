#!/usr/bin/env python
# -*-coding:utf-8-*-

import urllib
import urllib2


# http://tieba.baidu.com/f?kw=%E6%B2%B3%E5%8D%97%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6&ie=utf-8&pn=50

def loadPage(url,filname):
    """

    :param url:
    :param filname:
    :return:
    """
    print("正在下载"+filname)
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }

    request = urllib2.Request(url, headers=headers)
    return urllib2.urlopen(request).read()

def writePage(html,filename):
    """
    :param html:
    :return:
    """
    print("正在保存"+filename)
    # 文件写入
    filename = "./html/" + filename
    f = open(filename.decode('utf-8'), 'w')
    f.write(html)
    f.close()
    # with open(filename.decode('utf-8'),"w+") as f:
    #     f.write(html)
    print("="*20)


def tiebaSpider(url, beginPage, endPage):
    """
    :param url: url
    :param beginPage:起始页
    :param endPage: 终止页
    """

    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = "第"+str(page)+"页.html"
        fullurl = url + "=utf-8&pn=" + str(pn)
        # print(fullurl)
        html = loadPage(fullurl, filename)
        # print(html)
        writePage(html,filename)
    print("全部下载完成！")


if __name__ == '__main__':
    kw = raw_input("请输入要爬取的贴吧名称：")
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)
