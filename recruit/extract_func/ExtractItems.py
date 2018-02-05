# -*- coding: utf-8 -*-

from selenium import webdriver
from scrapy.http import FormRequest
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from recruit.items import RecruitItem
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from recruit.db import DbHandler
from recruit.tools import conf, FileIO
import re
import datetime
import scrapy
import json
import scrapy
import codecs
import datetime
import time
import xlwt
import sys
import urllib
import urllib2

'''将传过来的json文件进行解析，解析为单个招聘信息的具体条目，并封装到recruit对象中,返回recruit组成的列表'''


def extractdata(self, data):

    # 构造recruit的list，处理完后返回此list
    recruit_list = []

    comp_name=0
    job_name=0
    job_loca=0
    comp_scale=0
    requiredegree=0
    comp_field=0
    min_experience=0
    max_experience=0
    min_salary=0
    max_salary=0
    work_type=0
    job_desc=0
    hire_num=0
    welfare=0
    post_time=0
    comp_location=0
    comp_develop=0
    url=0
    source=0
    # 每个json 包含多个招聘列表信息。
    for i in range(0, len(data['data']['data']['disp_data'])):

        # 每次处理并封装一个recruit
        recruit = RecruitItem()
        each_recruit_info = data['data']['data']['disp_data'][i]
        url = each_recruit_info['url'].encode('utf-8')
        # print "----------" + url
        try:
            comp_name = each_recruit_info['officialname'].encode('utf-8')
            job_name = each_recruit_info['name'].encode('utf-8')
            job_loca = each_recruit_info['location'].encode('utf-8')
            requiredegree = each_recruit_info['education'].encode('utf-8')

            # 处理学历信息 0不限，1大专，2本科，3硕士，4博士
            if u"大专" in requiredegree:
                requiredegree = '1'
            elif u"本科" in requiredegree:
                requiredegree = '2'
            elif u"硕士" in requiredegree:
                requiredegree = '3'
            elif u"博士" in requiredegree:
                requiredegree = '4'
            else:
                requiredegree = '0'

        except Exception as e:
            print "parse-comp_basic: " + str(e)

        # 工作经验 数字化 /其中工作经验可能是list
        try:
            min_experience = '-1'
            max_experience = '-1'
            if isinstance(each_recruit_info['experience'].encode('utf-8').split(','), list):
                experience = each_recruit_info['experience'].encode('utf-8').split(',')[0].encode('utf-8')
                if experience == "经验1年以下":
                    min_experience = '0'
                    max_experience = '1'
                elif experience == "经验应届毕业生":
                    min_experience = '0'
                    max_experience = '0'
                elif experience.endswith("以上"):
                    min_experience = experience.split('年')[0].lstrip("经验")
                    max_experience = '-1'
                elif experience.endswith("以下"):
                    min_experience = '0'
                    max_experience = experience.split('年')[0].lstrip("经验")
                elif '-' in experience:
                    min_experience = experience.split('-')[0].lstrip("经验")
                    max_experience = experience.split('-')[1].rstrip("年")
                else:
                    min_experience = '-1'
                    max_experience = '-1'
            else:
                experience = each_recruit_info['experience'].encode('utf-8')
                if experience == "经验1年以下":
                    min_experience = '0'
                    max_experience = '1'
                elif experience == "经验应届毕业生":
                    min_experience = '0'
                    max_experience = '0'
                elif experience.endswith("以上"):
                    min_experience = experience.split('年')[0].lstrip("经验")
                    max_experience = '-1'
                elif experience.endswith("以下"):
                    min_experience = '0'
                    max_experience = experience.split('年')[0].lstrip("经验")
                elif '-' in experience:
                    min_experience = experience.split('-')[0].lstrip("经验")
                    max_experience = experience.split('-')[1].rstrip("年")
                else:
                    min_experience = '-1'
                    max_experience = '-1'

        except Exception as e:
            print "parse-exps: " + str(e)

        # 薪水解析，数字化

        min_salary = '-1'
        max_salary = '-1'
        salary = each_recruit_info['salary'].encode('utf-8')
        if '-' in salary:
            min_salary = salary.split('-')[0]
            max_salary = salary.split('-')[1]
            if max_salary == '1':
                min_salary = '-1'
                max_salary = '-1'
            elif max_salary == '99999999':
                max_salary = '-1'
        else:
            min_salary = '-1'
            max_salary = '-1'

        # 工作性质数字化
        work_type_str = each_recruit_info['type'].encode('utf-8')
        if "全职" in work_type_str:
            work_type = '0'
        elif "兼职" in work_type_str:
            work_type = '1'
        elif "实习" in work_type_str:
            work_type = '2'
        else:
            work_type = '0'

        job_desc = each_recruit_info['description'].encode('utf-8')

        # 招聘人数数字化
        try:
            hire_num = each_recruit_info['number'].encode('utf-8')

            if hire_num == '0':
                hire_num = '-1'
            elif '-' in hire_num:
                hire_num = hire_num.split('-')[1]
            elif hire_num == '若干人':
                hire_num = '-1'
            elif '人' in hire_num:
                hire_num = hire_num.split('人')[0].lstrip('招聘')
            elif hire_num == '':
                hire_num = '-1'
            elif hire_num == '不限':
                hire_num = '-1'

            hire_num = int(hire_num)
        except Exception as e:
            hire_num = '-1'
            print "parse-job_info: " + str(e)

        try:
            post_time_stamp = each_recruit_info['_update_time'].encode('utf-8')
            timearray = time.localtime(int(post_time_stamp))
            post_time = time.strftime("%Y-%m-%d", timearray)

            comp_scale = each_recruit_info['size'].encode('utf-8')
            if comp_scale is None:
                comp_scale = ''
            comp_location = each_recruit_info['companyaddress'].encode('utf-8')
            comp_develop = each_recruit_info['employertype'].encode('utf-8')
            # comp_link = each_recruit_info['officialname'].encode('utf-8')
            # comp_img_src = each_recruit_info['officialname'].encode('utf-8')
            comp_field = each_recruit_info['industry'].encode('utf-8')
            source = each_recruit_info['source'].encode('utf-8')
        except Exception as e:
            print "parse-comp_info: " + str(e)

        try:
            if isinstance(each_recruit_info['welfare'], list):
                welfares = each_recruit_info['welfare']
                welfare = ''
                for item in welfares:
                    welfare += item.encode('utf-8') + ','
            else:
                welfare = each_recruit_info['welfare'].encode('utf-8')
        except Exception as e:
            print "parse-ware: " + str(e)

        '''---------------------------------封装到recruit类中-----------------------------------'''

        recruit['comp_name'] = comp_name
        recruit['job_name'] = job_name
        recruit['job_loca'] = job_loca
        recruit['comp_scale'] = comp_scale
        recruit['requiredegree'] = requiredegree
        recruit['comp_field'] = comp_field
        recruit['min_experience'] = min_experience
        recruit['max_experience'] = max_experience
        recruit['min_salary'] = min_salary
        recruit['max_salary'] = max_salary
        recruit['work_type'] = work_type
        recruit['job_desc'] = job_desc
        recruit['hire_num'] = hire_num
        recruit['welfare'] = welfare
        recruit['post_time'] = post_time
        recruit['comp_location'] = comp_location
        recruit['comp_develop'] = comp_develop
        recruit['url'] = url
        recruit['source'] = source

        '''job_desc 太大，保存为txt，文件名为JobInfoId'''

        jobinfoid = DbHandler.write2db(recruit)
        job_desc_dir = conf.data_dir + 'job_desc' + r'/'
        FileIO.mkmydr(job_desc_dir)
        jobinfo_name = str(jobinfoid) + '.txt'
        try:
            FileIO.write(job_desc_dir + jobinfo_name, job_desc)
        except Exception as e:
            print 'job_desc file IO error'
        # 返回拼装的列表，每个列表对应一个json文件的招聘信息
        recruit_list.append(recruit)

    return recruit_list


