# -*- coding: utf-8 -*-
import os
import ConfigParser
# os.getcwd()+
from recruit.items import RecruitItem
from recruit.tools import FileIO

pwd = os.getcwd()

# 从配置文件中读取存储路径
cf = ConfigParser.ConfigParser()
cf.read('D:/code/代码及文档整理/code/conf.ini'.decode("utf-8"))
# cf.read("../../../conf.ini")
try:
    if cf.get("weblist", "bdsz"):
        data_dir = (cf.get("scrawled_data_path", "bdsz_dp")).decode("utf-8")
except Exception as e:
    # 若配置文件中没有配置保存路径，采用以下路径
    data_dir = "E:\\Py\\bd\\recruit\\data\\"

print data_dir
FileIO.mkmydr(data_dir)

# for powerCMD
# data_dir = r'D:/code/scrapy_recruit_websites/9recruit-scrapy-bd-4/recruit/data/'

# id_url = data_dir + "id_url_zlsz.txt"
# id_url = data_dir + "id_url_zlxz.txt"
# id_url = data_dir + "id_url_zlsx.txt"

