# -*- coding: utf-8 -*-

import MySQLdb
from recruit.items import RecruitItem

def getcommpanyid(companyname, companyloc):

    # 建立连接
    conn = MySQLdb.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='9432',
        db='recommend',
        charset='utf8'
    )
    cursor = conn.cursor()

    # companyname = '百度'
    # companyloc = '北京'

    # 构建sql语句
    sql_select = "select CompanyId from companyinfo WHERE CompanyName = '%s' AND  CompanyLocation = '%s'" \
                 % (companyname, companyloc)

    sql_insert = "insert into companyinfo(CompanyName, CompanyLocation) values(%s,%s)"
    param_comp = (companyname, companyloc)


    try:
        # 执行查询语句
        cursor.execute(sql_select)
        results = cursor.fetchall()

        # 存在则返回id，不存在则执行插入操作
        for row in results:
            if row[0]:
                return row[0]
            else:
                cursor.execute(sql_insert, param_comp)
                cursor.execute('SELECT LAST_INSERT_ID()')
                rs = cursor.fetchone()
                return rs[0]

    except Exception as e:
        print 'error:' + "--" + str(e)
        conn.rollback()

    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()



'''将传过来的recruit信息写入数据库'''


def write2db(recruit):

    # 建立连接
    conn = MySQLdb.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='9432',
        db='recommend',
        charset='utf8'
    )
    cursor = conn.cursor()

    # 获取信息
    try:
        comp_name = recruit['comp_name'].encode('utf-8')
        job_name = recruit['job_name']
        job_loca = recruit['job_loca'].encode('utf-8')
        comp_scale = recruit['comp_scale']
        requiredegree = int(recruit['requiredegree'])
        comp_field = recruit['comp_field'].encode('utf-8')
        min_experience = int(recruit['min_experience'])
        max_experience = int(recruit['max_experience'])
        min_salary = int(recruit['min_salary'])
        max_salary = int(recruit['max_salary'])
        work_type = int(recruit['work_type'])
        job_desc = recruit['job_desc']
        hire_num = int(recruit['hire_num'])
        welfare = recruit['welfare']
        post_time = recruit['post_time']
        comp_location = recruit['comp_location'].encode('utf-8')
        comp_location = '北京'
        comp_develop = recruit['comp_develop'].encode('utf-8')
        url = recruit['url']
        # 中间变量公司id
        companyid = ''
    except Exception as e:
        print "db recerse error: " + str(e)

    '''执行获取公司id操作'''

    # sql语句

    sql_select_companyinfo = "select CompanyId from companyinfo WHERE CompanyName = '%s' AND  CompanyLocation = '%s'" \
                            % (comp_name, comp_location)

    sql_insert_companyinfo = "insert into companyinfo(CompanyName, CompanyLocation, CompanyDevelop, KeyWord) values(%s,%s,%s,%s)"
    param_comp = (comp_name, comp_location, comp_develop, comp_field) #field暂时表示keyword


    try:
        # 执行查询语句，判断公司是否已经存在
        cursor.execute(sql_select_companyinfo)
        results = cursor.fetchone()

        # 存在则返回id，不存在则执行插入公司信息的操作
        if results:
            companyid = int(results[0])
            # print companyid
        else:
            cursor.execute(sql_insert_companyinfo, param_comp)
            cursor.execute('SELECT max(CompanyId) from companyinfo')
            rs = cursor.fetchone()
            companyid = int(rs[0])
            # print companyid

    except Exception as e:
        print 'error:' + "--" + str(e)
        conn.rollback()


    '''执行插入job信息操作'''

    # sql 插入job信息语句
    sql_insert_jobinfo = "insert into jobinfo(CompanyId, JobName, Location, RequireDegree, MinExperience, MaxExperience, " \
                         "MinSalary, MaxSalary, WorkType, HireNum, Welfare, PostTime ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param_job = (companyid, job_name, job_loca, requiredegree, min_experience, max_experience,
                 min_salary, max_salary, work_type, hire_num, welfare, post_time)
    job_id=0
    try:
        # 插入jobinfo信息
        cursor.execute(sql_insert_jobinfo, param_job)
        cursor.execute('SELECT max(JobInfoId) from jobinfo')
        rs = cursor.fetchone()
        job_id=int(rs[0])

    except Exception as e:
        print 'error:' + "--" + str(e)
        conn.rollback()

    conn.commit()

    # 关闭指针和连接
    cursor.close()
    conn.close()

    print job_id
    return job_id




