# coding=utf-8
import re
from bs4 import BeautifulSoup

from crawler.http_utility import HttpUtility

# 使用的解析器
features = "lxml"


# 第二页地址 http://www.lbldy.com/movie/page/2/

class WebSitParser:
    def __init__(self, url):
        self.url = url
        pass

    # 获取电影列表
    def parse_list(self, page=1):
        url = self.url
        if page != 0:
            url = self.url + "page/%d/" % page
        print(url, end="\n")

        h = HttpUtility(url)
        html = h.get()
        soup = BeautifulSoup(html, features)
        list = soup.find(id="center").find_all(class_="postlist")

        # 没有数据的时候结束
        if list is None or len(list) == 0:
            return
        for l in list:
            self.parse_about(l)
        # 递归获取数据
        self.parse_list(page + 1)
        pass

    # 获取电影简介
    def parse_about(self, about):
        name = about.h4.a["title"]
        url = about.h4.a["href"]
        self.parse_detail(url)
        pass

    # 获取电影详情
    def parse_detail(self, url):
        h = HttpUtility(url)
        html = h.get()
        soup = BeautifulSoup(html, features)

        detail = soup.find(id="center").find(class_="col").find(class_="post")
        # 名字
        name = detail.h2.string
        name = name[name.index("《") + 1:name.index("》")]
        # 更新时间
        time = detail.find(class_="postmeat").text
        time = time[time.index("：") + 1:time.index("|")]
        # 状态
        status = detail.find(class_="postmeat").span.text
        # 图片
        imgs = detail.find_all("img")
        img = ""
        if len(imgs) > 0:
            # print(imgs[0])
            img = imgs[0]["src"]

        # 下载地址
        ed2k, yunpan = self.get_download_url(detail.find("div", class_="entry"))

        print(name, time, status, img, ed2k, yunpan, end="\n \n \n")
        pass

    def get_download_url(self, div):

        list = []

        list_p = div.find_all("p")

        # 先获取最后一个
        list_p = list_p[::-1]

        for p in list_p:
            a = p.a

            if a is None:
                break
            else:
                href = a["href"].replace("http://www.lbldy.com", "")
                # print(href)
                if len(href.strip()) < 10:
                    continue
                if href.find("pan.baidu.com") > 0:
                    href = p
                list.append(href)
                pass
        print(list)
        return "", ""

    def save(self):
        pass