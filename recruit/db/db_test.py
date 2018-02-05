# -*- coding: utf-8 -*-

import MySQLdb
from recruit.items import RecruitItem



# 建立连接
conn = MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='recommend',
    charset='utf8'
)
cursor = conn.cursor()

companyname = '阿里'
companyloc = '深圳'

# 构建sql语句
sql_select = "select CompanyId from companyinfo WHERE CompanyName = '%s' AND  CompanyLocation = '%s'" \
             % (companyname, companyloc)

sql_insert = "insert into companyinfo(CompanyName, CompanyLocation) values(%s,%s)"
param_comp = (companyname, companyloc)


try:
    # 执行查询语句
    cursor.execute(sql_select)
    results = cursor.fetchone()

    # 存在则返回id，不存在则执行插入操作
    if results:
        print results[0]
    else:
        cursor.execute(sql_insert, param_comp)
        cursor.execute('SELECT max(CompanyId) from companyinfo')
        rs = cursor.fetchone()

        print int(rs[0])

except Exception as e:
    print 'error:' + "--" + str(e)
    conn.rollback()

conn.commit()

# 关闭连接
cursor.close()
conn.close()
