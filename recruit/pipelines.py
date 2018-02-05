# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import datetime
from recruit.tools import conf, FileIO
from recruit.extract_func import ExcelHandler
from recruit.items import RecruitItem
from scrapy.exceptions import DropItem
from recruit.spiders.BDSpider import RecruitSpider
#from recruit.db import DbHandler


class RecruitPipeline(object):

    total_num = 0
    excel_line_num = 0

    def process_item(self, item, spider):

        if isinstance(item, RecruitItem):


            print
            # DbHandler.write2db(item)

        else:
            return item


'''使用redis实现item中url去重'''
# class DuplicatesPipeline(object):
#     def process_item(self, item, spider):
#         if Redis.exists('url:%s' % item['url']):
#             raise DropItem("Duplicate item found: %s" % item)
#         else:
#             Redis.set('url:%s' % item['url'], 1)
#             return item







# class JsonWriterPipeline(object):
#     def __init__(self):
#         self.file = codecs.open('lagou_data1.json', 'w', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line.decode('unicode_escape'))
#         return item
