# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecruitItem(scrapy.Item):

    postTime = scrapy.Field()  # 发布时间 文件夹分类
    url = scrapy.Field()  # 招聘信息url
    content = scrapy.Field()  # html
    homePage = scrapy.Field()  # 获取homepage前缀

    comp_name = scrapy.Field()
    job_name = scrapy.Field()
    job_loca = scrapy.Field()
    requiredegree = scrapy.Field()
    min_experience = scrapy.Field()
    max_experience = scrapy.Field()
    min_salary = scrapy.Field()
    max_salary = scrapy.Field()
    work_type = scrapy.Field()
    job_desc = scrapy.Field()
    hire_num = scrapy.Field()
    welfare = scrapy.Field()
    post_time = scrapy.Field()
    comp_scale = scrapy.Field()
    comp_location = scrapy.Field()
    comp_develop = scrapy.Field()
    comp_link = scrapy.Field()
    comp_img_src = scrapy.Field()
    comp_field = scrapy.Field()
    source = scrapy.Field()  # 招聘网站简称

    json_file_name = scrapy.Field()

    # locality = scrapy.Field()  #工作地点
    pass
