#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/22 0022 下午 11:47
# @Author  : toby
# @Site    : 
# @File    : mydb.py
# @Software: PyCharm




import pymysql


from com_pkg import comm
import time

class MyDB:

    def __init__(self,host,port,user,passwd):
        '''
        connect the mysql
        :param host:
        :port port :
        :param user:
        :param passwd:
        :param db:
        '''
        # 打开数据库连接
        self.conn = pymysql.connect(host=host,port= port, user=user, passwd=passwd, db='autocharge')
        # 获取游标
        self.cursor = self.conn.cursor()
        print('Get curse success!')

    # sql执行
    def sel_sql(self,sql_string):
        '''
        run the query_sql
        :param sql_string:
        :return:
        '''

        self._query = sql_string
        print('查询语句:{}'.format(self._query))
        try:
            self.cursor.execute(query=self._query)
            self.conn.commit()

            result = self.cursor.fetchall()
            print(result)

            cm = comm.Comm()
            name1 = str(time.time())
            name = name1.split('.',1)[0]
            print('{}'.format(name))

            cm._write_excel(name,result)
            print('写入完成!')

        except:
            self.conn.rollback()
            print('执行查询的失败 ,excel 写入失败 ,回滚 !')

    def close_(self):
        '''
        Closed mysql
        :return: None
        '''
        self.cursor.close()
        self.conn.close()
        print('mysql closed')


# def readcfg():
#     conf = configparser.ConfigParser()
#     print('--------------')
#     conf.read('../celery_task/cfg.ini', encoding='utf-8')
#     print(conf.sections())
#
#     sections = conf.sections()  # 获取配置文件中所有sections，sections是列表
#     print(sections)
#
#     host = conf.get('db', 'HOST')
#     port = conf.get('db', 'PORT')
#     user = conf.get('db', 'USER')
#     passwd = conf.get('db', 'PASSWD')
#     print('Read '
#           'config file !')
#     print(host, port, user, passwd)
#
#     db = MyDB(host=host, port=int(port), user=user, passwd=passwd)
#     return db
#
#



if __name__ == '__main__':

    # db = readcfg()
    # db = MyDB(host=host,port=int(port),user=user,passwd=passwd)
    sql = 'select * from t_charge_alarm ORDER BY rowkey DESC LIMIT 100;'
    #
    #
    # db.sel_sql(sql_string=sql)
    # db.close_()
    pass

