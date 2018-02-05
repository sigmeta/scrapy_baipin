# -*- coding: utf-8 -*-

from selenium import webdriver
from scrapy.http import FormRequest
from recruit.db import DbHandler
from recruit.extract_func import ExtractItems
import re
import os
import scrapy
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():

    rootdir = 'C:/bd_spider/9recruit-scrapy-bd-v4.0/recruit/data/bdsz'

    try:
        for dirpath, dirnames, filenames in os.walk(rootdir):
            for filepath in filenames:
                # 读取json文件
                f = open(rootdir + r'/' + filepath, 'r')
                content = f.read().encode('utf-8')
                f.close()
                data = json.loads(content)
                # 交给exteactItems去解析具体字段
                recruit_lists = ExtractItems.extractdata(data)
                for recruit in recruit_lists:
                    # 写入数据库库
                    DbHandler.write2db(recruit)

        print "finished"
    except Exception as e:
        print "exteact offline json err: " + str(e)

if __name__ == "__main__":
    main()
