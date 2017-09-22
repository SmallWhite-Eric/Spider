#!/usr/bin/env python2
# -*- coding:utf-8 -*-
'''
    使用爬虫程序模拟登录CSDN
'''
import requests
import re

class CSDNSpider():
    # 构造函数
    def __init__(self):
        self.sess = requests.session()
        self.url = "https://passport.csdn.net/account/login"
        self.html = ""
        self.lt = ""
        self.execution = ""
        self._eventId = ""

    # 向csdn服务器发送请求
    def request(self):
        try:
            req = self.sess.get(self.url, verify=False)
            self.html = req.content
            # self.getParams(html)
        except Exception as e:
            print e.message

    # 从csdn源代码中获取参数
    def getParams(self):
        lt = re.findall('name="lt" value="(.*?)"', self.html)
        execution = re.findall('name="execution" value="(.*?)"', self.html)
        _eventId = re.findall('name="_eventId" value="(.*?)"', self.html)
        if len(lt) > 0:
            self.lt = lt[0]
        if len(execution) > 0:
            self.execution = execution[0]
        if len(_eventId) > 0:
            self._eventId = _eventId[0]

    # 发送post请求
    def postData(self):
        url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
        data = {
            "username": "1556575195",
            "password": "092744gd",
            "lt": self.lt,
            "execution": self.execution,
            "_eventId": self._eventId
        }
        try:
            r = self.sess.post(url, data=data)
        except Exception as e:
            print e.message

    # 再次请求
    def requestAgain(self):
        self.sess.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Host": "my.csdn.net",
            "Referer": "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
        try:
            res = self.sess.get('http://my.csdn.net/')
            return res.content
        except Exception as e:
            print e.message

    # 模拟登录
    def simulation_on(self):
        try:
            self.request()
            self.getParams()
            self.postData()
            html = self.requestAgain()
            return html
        except Exception as e:
            e.message


if __name__ == '__main__':
    spider = CSDNSpider()
    print spider.simulation_on()
