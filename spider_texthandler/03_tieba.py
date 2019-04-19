#!/usr/bin/env python
# -*-coding:utf-8-*-
import urllib
import urllib2
import re
from lxml import etree


class tiebaImgSpider:
    def __init__(self):
        self.url = "http://tieba.baidu.com"
        self.kw = raw_input("请输入要爬取的贴吧名称：")
        self.beginPage = int(raw_input("请输入起始页："))
        self.endPage = int(raw_input("请输入结束页："))
        self.key = urllib.urlencode({"kw": self.kw})
        self.fullurl = self.url + "/f?" + self.key

    def tiebaSpider(self):
        for page in range(self.beginPage, self.endPage + 1):
            pn = (page - 1) * 50
            fullurl = self.fullurl + "&ie=utf-8&pn=" + str(pn)
            print(fullurl)
            html = self.loadPage(fullurl)
            self.dealhtml(html)
            # print(html)

        print("已完成！")

    def loadPage(self, fullurl):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }
        request = urllib2.Request(fullurl, headers=headers)
        html = urllib2.urlopen(request)
        return html.read()

    def dealhtml(self, html):
        # etree_xml = etree.HTML(html)
        # print(html)
        # links = etree_xml.xpath('//li[@class="j_thread_list clearfix"]/div[@class="t_con cleafix"]/div/div/div/a/@href')
        pattern = re.compile(r'div class=.threadlist_lz clearfix.*?rel=\"noreferrer\" href=\"(.*?)\" .*?</div>',re.S)
        links = pattern.findall(html)
        for link in links:
            lz_html = self.loadPage(self.url + link)
            lz_xml = etree.HTML(lz_html)
            imagelinks = lz_xml.xpath('//cc//img[@class="BDE_Image"]/@src')
            # print(lz_html)
            # pattern = re.compile('img class=\"BDE_Image\" src=\"(.*?)\".*?br', re.S)
            # imagelinks = pattern.findall(lz_html)
            print("=" * 30)
            print(self.url + link)

            for imagelink in imagelinks:
                print(imagelink)
                img = self.loadPage(imagelink)
                self.writeImg(img, imagelink[-8:])

    def writeImg(self, img, imgName):
        with open('./img/' + imgName, 'wb') as f:
            f.write(img)



if __name__ == '__main__':
    tieba_img_spider = tiebaImgSpider()
    tieba_img_spider.tiebaSpider()
