# -*- coding: utf-8 -*-

import MySQLdb

conn = MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='recommend',
    charset='utf8'
)

cursor = conn.cursor()

companyname = '百度'
companyloc = '上海'
sql_insert = "insert into companyinfo(CompanyName, CompanyLocation) values(%s,%s)"
sql = "SELECT MAX(CompanyId) AS maxid FROM %s" % ("companyinfo", )

param = (companyname, companyloc)


# cursor.execute(sql_insert, param)
cursor.execute(sql)


conn.commit()


cursor.close()
conn.close()

