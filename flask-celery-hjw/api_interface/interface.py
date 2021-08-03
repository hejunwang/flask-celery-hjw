#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@126.com
@software: pycharm
@file: Interface.py
@time: 2021-04-28 23:52
@desc:
'''
import json,os
import requests
from  log_pkg.mylogger import Log

class Interface_api:
    '''
    API接口封装
    '''
    def __init__(self,url):
        self.url = url

    def get_interface(self,params=None,headers=None):
        '''
        get 请求
        :param url:
        :param params:
        :param headers:
        :return:
        '''
        res = requests.get(url=self.url,params=params,headers=headers)
        # print(res)
        return  res


    def post_interface(self,data,headers=None):
        '''
        post 请求
        :param url:
        :param data:
        :param headers:
        :return:
        '''
        res = requests.post(url=self.url,data=data,headers=headers)
        return  res

    def put_interface(self,params,headers):
        '''
        put 请求
        :param url:
        :param data:
        :param headers:
        :return:
        '''
        res = requests.put(url=self.url,params=params, headers=headers)
        return  res
        pass

    def delete_interface(self,data,headers):
        '''
        delete 请求
        :param url:
        :param headers:
        :return:
        '''
        res = requests.delete(url=self.url,data=data, headers=headers)

        return  res


if __name__ == '__main__':

    url = 'https://test.xlvren.com/bp/login'
    params =json.dumps( {
            'password':'e10adc3949ba59abbe56e057f20f883e',
            'username': '13512341234'
            })
    headers = {
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }

    rs = Interface_api(url=url).post_interface(data=params,headers=headers)
    print(type(rs.text))
    res = json.loads(rs.text)
    print(res)
    print((res['data'])['token'])

    url1 ="https://test.xlvren.com/bp/bp/find/chargeDealStatistic"
    params2 = {"stationIds":100213}
    headers['Authorization']='Bearer {}'.format((res['data'])['token'])
    print(headers)
    rs1 = Interface_api(url=url1).get_interface(params=params2,headers=headers)
    print(type(rs1.text))
    print(rs1.text)
    ss = json.loads(rs1.text)
    print(ss)
    assert ss['errorCode'] == 0



