#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@126.com
@software: pycharm
@file: logger.py
@time: 2020-11-18 23:20
@desc:
'''
# MNJUFOYUIBJAKWFG    邮箱pass


import os
import time
import threading

log_dir = '../logs'
import logging

class Log(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Log, "_instance"):
            with Log._instance_lock:
                if not hasattr(Log, "_instance"):
                    Log._instance = object.__new__(cls)
        return Log._instance

    def __init__(self,filename=None):

        import os
        folder_or_dir = log_dir
        print('log_dir:'+log_dir)

        if not os.path.exists(folder_or_dir):

            print("folder or dir not exist !!!!!!")
            os.makedirs(folder_or_dir)  # 创建目录或文件夹

        else:
            print('folder exist!')

        # 文件命名   os.path.join()：  将多个路径组合后返回
        self.logname = os.path.join(log_dir, '%s.log' % time.strftime('%Y-%m-%d'))
        # 生成记录器对象
        self.logger = logging.getLogger()
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)
        if filename==None:
            # 日志输出格式
            fm = '[%(asctime)s] | %(filename)s |%(levelname)-6s: %(message)s'
            # fm = '%(levelname)：%(levelno)s：%(name)s：%(funcName)s：%(asctime)：%(pathname)：%(filename)：%(module)：%(thread)：%(threadName)'
            self.formatter = logging.Formatter(fm)
        else:
            fm ='[%(asctime)s] | %('+filename+')s |%(levelname)-6s: %(message)s'
            self.formatter = logging.Formatter(fm)



    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地日志文件
        fh = logging.FileHandler(self.logname, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(self.formatter)
        self.logger.addHandler(sh)

        # 判断日志级别
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # removeHandler在记录日志之后移除句柄，避免日志输出重复问题
        self.logger.removeHandler(sh)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    # debug < info< warning< error< critical
    # debug模式
    def debug(self, message):
        self.__console('debug', message)

    # info模式
    def info(self, message):
        self.__console('info', message)

    # warning模式
    def warning(self, message):
        self.__console('warning', message)

    # error模式
    def error(self, message):
        self.__console('error', message)

    """
    filename: 指定日志文件名
    filemode: 和file函数意义相同，指定日志文件的打开模式，’w’或’a’
    format: 指定输出的格式和内容，format可以输出很多有用信息。显示的条目可以是以下内容：
    %(levelname)：日志级别的名字格式
    %(levelno)s：日志级别的数字表示
    %(name)s：日志名字
    %(funcName)s：函数名字
    %(asctime)：日志时间，可以使用datefmt去定义时间格式，如上图。
    %(pathname)：脚本的绝对路径
    %(filename)：脚本的名字
    %(module)：模块的名字
    %(thread)：thread id
    %(threadName)：线程的名字 
    """

if __name__ == '__main__':

    mylog = Log()
    mylog.info("main logging")
    print(log_dir)