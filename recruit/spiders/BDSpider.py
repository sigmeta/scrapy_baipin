# -*- coding: utf-8 -*-

from selenium import webdriver
from scrapy.http import FormRequest
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from recruit.items import RecruitItem
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from recruit.db import DbHandler
from recruit.extract_func import ExtractItems
from recruit.extract_func import ExcelHandler
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
import time
import random

reload(sys)
sys.setdefaultencoding('utf-8')

from recruit.tools.middlewares import MyProxySpiderMiddleware as mpsm

class RecruitSpider(CrawlSpider):

# http://zhaopin.baidu.com/api/async?query=&salary=&welfare=&education=&sort_key=&sort_type=1&city=%E4%B8%8A%E6%B5%B7&district=&experience=&employertype=&jobfirstclass=&jobsecondclass=&jobthirdclass=&date=&detailmode=close&rn=30&pn=30'''
#'程序员','网页设计','技术专员','软件工程师','测试工程师','运维工程师','技术支持','硬件工程师','系统工程师',
              #'通信工程师','数据工程师','前端工程师','APP开发','算法工程师','移动产品经理','数据产品经理','电商产品经理',
              #'互联网产品经理','产品运营','数据运营经理','大数据',
              #'高级产品经理','无线电','电路工程','自动化','电子维修','产品工艺','量化投资','技术经理','策略研究',
              #'理财顾问','证券分析','银行柜员','拍卖师','操盘手','银行经理','信贷管理','会计','财务','出纳','审计',
    name = "bdsz"
    allowed_domains = ["baidu.com"]
    '''
    fields = ['税务',
              '成本管理','投资顾问','投资助理','理财助理','行业研究','行业分析','互联网金融','衍生品']

    fields2 = ['数据运营', 'MySQL', '售前工程师', '实施工程师', '电商产品经理', 'Flash', '系统管理员',
               'CTO', '架构师', '数据产品经理', 'C#', '自动化测试', '系统集成', '单片机', '游戏美术总监','ui设计总监',
               'Java', 'PHP', 'C', 'C++', 'Python', '.NET', 'Hadoop','Spark', '数据挖掘', '数据分析', 'HTML5', 'Android', 'iOS',
               'web前端', '测试开发', 'MySQL','DBA']

    fields3 = ['全栈工程师', 'JavaScript', 'COCOS2D-X', '视觉设计', '游戏场景', '硬件测试', '游戏制作人', '电路设计',
               'IT支持', 'IDC', 'WEB安全', '网络安全', '运维开发工程师', '游戏测试', '手机测试',
               '系统安全', '运维经理', 'SQLServer', 'Oracle', 'DB2', 'MongoDB', '性能测试','Linux',
               'ETL', 'VB', 'Hive', '数据仓库', '运维总监', '技术合伙人', '测试总监', '安全专家', '驱动开发', '推荐系统',
               'ARM开发', 'BI工程师',  'Perl', 'Ruby', 'Node.js', '自然语言处理', '搜索算法','平面设计', '美术设计',
               '网络工程师','技术总监', '硬件工程师', '售后工程师', '嵌入式', '游戏策划', '产品设计师', '产品部经理',
               'UI', '交互设计', '运营', '功能测试','Java项目经理','.NET项目经理','PHP项目经理','机器学习',
               '深度学习','智能硬件','机器翻译']
    '''
    '''
    fields = ['Java', 'PHP', 'C', 'C++', 'Python', '.NET', 'Hadoop', '数据挖掘', '数据分析', 'HTML5', 'Android', 'iOS',
              'web前端', '测试开发', 'MySQL']

    fields2 = ['数据运营', 'MySQL', '前端工程师','实施工程师', '电商产品经理', 'Flash', '系统工程师', '系统管理员',
               '技术经理', 'CTO', '架构师', '数据产品经理', 'C#', '自动化测试', '系统集成', '单片机', '大数据']

    fields3 = ['全栈工程师', 'JavaScript','视觉设计', '游戏场景', '游戏制作', '电路设计','机器学习',
               'IT支持', 'IDC', 'WEB安全', '网络安全', '运维工程师', '游戏测试','测试工程师',
               '系统安全', '运维经理', 'SQLServer', 'Oracle', 'DB2', 'MongoDB', '性能测试',
               'ETL', 'VB', 'Hive', '数据仓库', '运维总监', '技术合伙人', '测试总监', '安全专家', '驱动开发', '精准推荐',
               'ARM开发', 'BI工程师', '移动产品经理', 'Perl', 'Ruby', 'Node.js', '自然语言处理', '搜索算法','平面设计',
               '网络工程师','技术总监', '自动化', '售前工程师', '售后工程师', '嵌入式', '游戏策划',
               'UI', '交互设计', '运营', '功能测试', '硬件工程师']
    '''
    '''
    fields=['Java', 'PHP', 'C', 'C++', 'Python', '.NET', 'HTML5', 'Android', 'iOS',
              'C#', 'JavaScript', 'VB',  'Perl', 'Ruby', 'Node.js', ]
              ['互联网金融', '交易员', '保险', '信托', '信贷', '分析师', '券商', '咨询', '基金', '审计', '并购', '成本管理',
               '投行', '投资', '清算', '理财', '私募', '租赁', '税务', '精算', '融资', '行业分析', '行业研究', '衍生品', '证券',
               '财务', '资产', '资信评估', '金融', '银行', '风控','产品经理','人力资源','高级管理','统计','数据分析','资产管理',
               '市场','会计','营销','量化','渠道','期货']
    '''

    fields =  ['互联网金融', '交易员', '保险', '信托', '信贷', '分析师', '券商', '咨询', '基金', '审计', '并购', '成本管理',
               '投行', '投资', '清算', '理财', '私募', '租赁', '税务', '精算', '融资', '行业分析', '行业研究', '衍生品', '证券',
               '财务', '资产', '资信评估', '金融', '银行', '风控','产品经理','人力资源','高级管理','统计','数据分析','资产管理',
               '市场','会计','营销','量化','渠道','期货']

    cities = ['北京', '上海', '广州', '深圳', '杭州', '南京', '成都', '广州','天津','重庆','厦门','青岛','济南','西安','武汉']

    educations = ['大专', '本科', '硕士', '博士','不限']

    salries = ['1_3000', '3001_5000', '5001_8000','8001_10000','10001_20000','20001_99999999']

    rn = 30    # item num of each json
    # 爬取的时间范围
    extract_date = '20171223_20171226'
    # extract_date = '' # 若时间没有指定，则默认为空。

    start_urls = ["http://zhaopin.baidu.com/"]

    errortimes=0

    #设置代理ip
    '''
    proxyip=mpsm.IPPOOL
    ip=random.choice(proxyip)
    proxy_handler = urllib2.ProxyHandler({'http': ip})
    print 'new ip'+ip
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    '''
    #防止出错，多次尝试获取页面
    def openlink(self,url,link):
        mnum = 10
        for tries in range(mnum):
            try:
                req_post = urllib2.urlopen(url, link, timeout=3)     #设置timeout防止网络波动导致假死
                return req_post
            except:
                self.errortimes = self.errortimes + 1
                if tries<mnum-1:
                    print "something wrong with the net, now try " +str(tries+1)+" time(s)..."
                    continue
                else:
                    print "Has tried "+str(mnum)+" times to access url "+link+", all failed!"
                    break

    # 打开网页链接
    def parse(self, response):
        # This receives the response from the start url. But we don't do anything with it.
        url = 'http://zhaopin.baidu.com/api/async'

        for field in self.fields:
            for city in self.cities:
                for education in self.educations:
                    for salary in self.salries:
                        print field, city, salary, education

                        # 先获取针对一个key组合的json_page num
                        payload = {'query': field, 'city': city, 'rn': '30', 'pn': str(0), 'salary': salary,
                                   'employertype': '', 'education': education, 'experience': '',
                                   'date': self.extract_date}
                        print payload

                        #如果尝试多次还不行的话，跳过这个url。捕获exception，continue，防止程序终止
                        try:
                            req_post = self.openlink(url, urllib.urlencode(payload))
                        except:
                            print "failed to get the text, skip this url, try next url..."
                            continue

                        try:
                            data_json = json.loads(req_post.read())
                            key_json_num = 1 + int(data_json['data']['data']['listNum']) // int(self.rn)
                            print 'key_json_num :', key_json_num

                            # 在已获得的页数里循环
                            for i in range(0, key_json_num):
                                payload = {'query': field, 'city': city, 'rn': '30', 'pn': str(30 * i),
                                           'salary': salary,
                                           'employertype': '', 'education': education, 'experience': '',
                                           'date': self.extract_date}
                                time.sleep(random.uniform(0, 5))
                                yield FormRequest(url, formdata=payload, callback=self.parse_items)
                        except Exception as e:
                            print field + city + education + salary + '： 这个key组合没有返回data'
                            continue  # 跳出循环
            print "net error times count:"+str(self.errortimes)
        '''
        for field in self.fields2:
            for city in self.cities:
                for salary in self.salries:
                    # 先获取针对一个key组合的json_page num
                    payload = {'query': field, 'city': city, 'rn': '30', 'pn': str(0), 'salary': salary,
                               'date': self.extract_date}
                    req_post = urllib2.urlopen(url, urllib.urlencode(payload))
                    try:
                        data_json = json.loads(req_post.read())
                        key_json_num = 1 + int(data_json['data']['data']['listNum']) // int(self.rn)

                        # 在已获得的页数里循环
                        for i in range(0, key_json_num):
                            payload = {'query': field, 'city': city, 'rn': '30', 'pn': str(30 * i), 'salary': salary,
                                       'employertype': '', 'education': '', 'experience': '',
                                       'date': self.extract_date}
                            time.sleep(random.uniform(0, 10))
                            yield FormRequest(url, formdata=payload, callback=self.parse_items)

                    except Exception as e:
                        print field + city + salary + '： 这个key组合没有返回data'
                        continue  # 跳出循环

        for field in self.fields3:
            for city in self.cities:
                payload = {'query': field, 'city': city, 'rn': '30', 'pn': str(0),
                           'date': self.extract_date}  # 先获取针对一个key组合的json_page num
                req_post = urllib2.urlopen(url, urllib.urlencode(payload))
                try:
                    data_json = json.loads(req_post.read())
                    key_json_num = 1 + int(data_json['data']['data']['listNum']) // int(self.rn)

                    # 在已获得的页数里循环
                    for i in range(0, 1):
                        payload = {'query': field, 'city': city, 'rn': '30', 'pn': str(30 * i), 'salary': '',
                                   'employertype': '', 'education': '', 'experience': '',
                                   'date': self.extract_date}
                        time.sleep(random.uniform(0, 10))
                        yield FormRequest(url, formdata=payload, callback=self.parse_items)
                except Exception as e:
                    print field + city + '： 这个key组合没有返回data'
                    continue  # 跳出循环
        '''
    #处理的递归函数
    def parse_items(self, response):

        data = json.loads(response.body)
        #data = data.decode('utf-8')

        #disp_len = len(data['data']['data']['disp_data'])

        # 通过关键字构造json名字
        json_key_list = urllib.unquote(response.request.body).split('&')
        json_name = str(json_key_list[3]) + str(json_key_list[1]) + str(json_key_list[4]) + \
                         str(json_key_list[0]) + str(json_key_list[6]) + \
                         'pn=' + str(int(json_key_list[7].lstrip(r'pn=')) / 30)
        print json_name
        json_full_name = json_name.decode('utf-8') + '.json'

        '''将response得到的json保存到文件中'''
        #"E:\\Py\\bd\\data\\"+self.extract_date+"\\"
        json_file_dir = "E:\\Py\\bd\\data\\"+self.extract_date+"\\"  #conf.data_dir + self.name + r'/'
        # 建立文件夹和文件
        FileIO.mkmydr(json_file_dir)
        FileIO.write(json_file_dir + json_full_name, '')
        # 写入json格式的文件
        with open(json_file_dir + json_full_name, 'w') as f:
            json.dump(data, f,ensure_ascii=False)
        '''ff=open("json.txt","w")
        data2=json.dumps(data)
        data2=data2.decode('utf-8')
        ff.write(data2)
        ff.close()'''

        '''
        # 调用函数, 解析json为具体的字段
        recruit_list = ExtractItems.extractdata(self,data)

        for recruit in recruit_list:
            yield recruit

        # 调用函数，写入excel
            ExcelHandler.write2excel(recruit, self.extract_date,100)
        '''



        #yield self.recruit


            #DbHandler.write2db(recruit)
