# -*- coding: utf-8 -*-

from scrapy import cmdline

from recruit.spiders import BDSpider
#from recruit.db import DbHandler
cmdline.execute("scrapy crawl bdsz".split())

# comid = DbHandler.getcommpanyid()
# print comid



