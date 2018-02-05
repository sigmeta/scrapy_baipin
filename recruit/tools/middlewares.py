# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy import signals
#from recruit.settings import IPPOOL
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class MyProxySpiderMiddleware(HttpProxyMiddleware):
    IPPOOL = ['125.46.0.62:53281']

    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        thisip = random.choice(self.IPPOOL)
        print("this is ip: " + thisip)
        request.meta["proxy"] = "http://" + thisip
