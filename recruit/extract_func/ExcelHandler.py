# -*- coding: utf-8 -*-

from selenium import webdriver
from recruit.items import RecruitItem
import json
import scrapy
import codecs
import datetime
import time
import xlwt
import sys
import urllib
import urllib2


def write2excel(recruit, extract_date, line_num):

    """write  to  excel file"""
    excel_file = xlwt.Workbook(encoding='utf-8')
    table = excel_file.add_sheet('comp_info', cell_overwrite_ok=True)
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'SimSun'  # 指定“宋体”
    style.font = font




    ''' ---------------------------写入excel文件------------------------------'''
    table.write(line_num, 0, recruit['comp_name'], style)
    table.write(line_num, 1, recruit['job_name'], style)
    table.write(line_num, 2, recruit['job_loca'], style)
    table.write(line_num, 3, recruit['requiredegree'], style)
    table.write(line_num, 4, recruit['comp_scale'], style)
    table.write(line_num, 5, recruit['comp_field'], style)
    table.write(line_num, 6, recruit['min_experience'], style)
    table.write(line_num, 7, recruit['max_experience'], style)
    table.write(line_num, 8, recruit['min_salary'], style)
    table.write(line_num, 9, recruit['max_salary'], style)
    table.write(line_num, 10, recruit['work_type'], style)
    table.write(line_num, 11, recruit['job_desc'], style)
    table.write(line_num, 12, recruit['hire_num'], style)
    table.write(line_num, 13, recruit['welfare'], style)
    table.write(line_num, 14, recruit['post_time'], style)
    table.write(line_num, 15, recruit['comp_location'], style)
    table.write(line_num, 16, recruit['comp_develop'], style)
    # table.write(line_num, 16, comp_link, style)
    # table.write(line_num, 17, comp_img_src, style)
    table.write(line_num, 17, recruit['url'], style)
    table.write(line_num, 18, recruit['source'], style)

    '''依据爬取的总的招聘数目，每单个excel两万个招聘条目'''

    # 保存excel文件
    excel_file.save('../data/com_info_baidu' + extract_date + '.xls')