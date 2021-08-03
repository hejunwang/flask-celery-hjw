#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@126.com
@software: pycharm
@file: test_001_case.py
@time: 2021-04-25 0:32
@desc:
'''
import json
import pytest
from api_interface import  interface
from api_interface.interface import Interface_api
from com_pkg.comm import Comm

from log_pkg.mylogger import Log
import allure
import configparser


def get_test_data(file_path, tag,rows=None,columns=None):
    '''
    读取配置文件，然后返回excel参数表的title
    :param file_path:
    :param tag:
    :param rows:
    :param columns:
    :return:
    '''
    Log().debug('tag---->'+tag)
    conf = configparser.ConfigParser()
    conf.read(file_path, encoding='utf-8')
    file_name = conf.get(tag,'file_name')
    sheet_name = conf.get(tag,'sheet_name')

    print('file_name-->{}'.format(file_name))
    print('sheet_name-->{}'.format(sheet_name))
    if rows==None and columns ==None:
        ls = Comm()._read_excel(file_name, sheet_name,rows=8,columns=7)
        return ls
    else:
        ls = Comm()._read_excel(file_name, sheet_name, rows=rows, columns=columns)
        return ls


def get_test_casename(file_name,sheet_name,rows = None,columns =None):
    '''
    获取测试用例的文件名称和sheetname,读取到列表中返回
    :param file_name:
    :param sheet_name:
    :param rows:
    :param columns:
    :return:
    '''
    if rows==None and columns ==None:
        ls = Comm()._read_excel(file_name, sheet_name,rows=8,columns=7)
        return ls
    else:
        ls = Comm()._read_excel(file_name, sheet_name, rows=rows, columns=columns)
        return ls



#fixture 只运行一次，后续每个case中都可以使用
@pytest.fixture(scope="session")
def token():
    print("---------------token---------------------")
    cf = configparser.ConfigParser()
    print(cf)
    cf.read('/root/flask-celery-hjw/flask-celery/pytest_pkg/param.ini', encoding='utf-8')
    _url = cf.get('conf', 'url')
    print(_url)

    _username = cf.get('conf', 'username')
    _password = cf.get('conf', 'password')
    _conttype = cf.get('conf', 'Content-Type')
    _uagent = cf.get('conf', 'User-Agent')
    _dt={}
    _headers={}
    _dt['username']=_username
    _dt['password']=_password
    _headers['Content-Type']=_conttype
    _headers['User-Agent']=_uagent

    print("---------------headers---------------------")

    # _url='https://test.xlvren.com/bp/login'
    # _dt = {}
    # _headers = {}
    # _dt['username'] = "13512341234"
    # _dt['password'] ="e10adc3949ba59abbe56e057f20f883e"
    # _headers['Content-Type'] = "application/json"
    # _headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"


    res = Interface_api(url=_url).post_interface(data=json.dumps(_dt),headers=_headers)
    print('*' * 50)
    ress = json.loads(res.text)
    Log().error('测试结果:{}'.format(ress))
    assert ress['errorCode'] == 0
    print('*' * 50)
    token = ress['data']['token']
    Log().debug("token:"+token)

    return token



@allure.feature("加购模块")
class Test_xlr2():

    @pytest.mark.run(order=1)
    def test_1(self,token):
        '''
        验证token 是否获取到
        :param token:
        :return:
        '''
        Log().debug("token:" + token)


    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('desc,url,add,method,pararm',
                             get_test_casename('/root/flask-celery-hjw/flask-celery/testcase-data/1.xlsx','Sheet',rows=16,columns=7))
    def test_2(self,desc,url,add,method,pararm,token):
        print('^--2--^'*20)
        tt = []
        tt.append(url)
        tt.append(add)
        _url = ''.join(tt)
        Log().info('case用例:'+desc)
        Log().info('地址url：{}'.format(_url))
        Log().info('token：{}'.format(token))


        headers = {}
        headers['Authorization'] = "Bearer {}".format(token)
        headers['Content-Type'] = 'application/json'
        print('header :{}'.format(headers))
        print('method :{}'.format(method))
        print('pararm :{}'.format(pararm))

        if method =='post':
            Log().debug('post 请求...')

            _data = json.loads(pararm)
            # Log().debug('_data:' + json.dumps(_data))
            # print("post 请求。。。。。")
            res = interface.Interface_api(url=_url).post_interface(data=json.dumps(_data),headers=headers)
            ss = json.loads(res.text)
            Log().debug('`````````````````````````````````````````````````')
            # print('测试结果:post,,,{}'.format(ss))
            assert ss['errorCode'] == 0
            res.close()
            print("post 请求 结束。。。。。")

        elif method=='get':
            Log().debug('get 请求 ....')
            _data = json.loads(pararm)
            # Log().debug('_data:' + json.dumps(_data))
            res = interface.Interface_api(url=_url).get_interface(params=_data,headers=headers)
            # print('get request:-->'+res.url)
            self.ress = res.text
            ss = json.loads(self.ress)
            Log().debug('测试结果:get,,,{}'.format(ss))
            assert ss["errorCode"] == 0
            # print('^' * 50)
            res.close()
            print('get 请求结束。。。。。。')


    # @pytest.mark.run(order=1)     #执行顺序
    # def test_3(self):
    #     print('测试结果 :3_')
    #
    # @pytest.mark.run(order=4)  # 执行顺序
    # def test_4(self):
    #     print('测试结果 :4_')
