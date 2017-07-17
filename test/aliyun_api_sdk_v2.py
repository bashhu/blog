# coding=utf-8
"""
__created__ =  2017/6/9 17:33
__author__ = 'baishaohua'
# @Site    : https://github.com/bashhu
"""

import os, sys
import hashlib
import hmac
import base64
import urllib
import time
import uuid
import requests


def get_iso8601_time():
    TIME_ZONE = "GMT"
    FORMAT_ISO8601 = "%Y-%m-%dT%H:%M:%SZ"
    return time.strftime(FORMAT_ISO8601, time.gmtime())


def get_uuid():
    return str(uuid.uuid4())


def get_parameters(user_param, Action, AccessKeyId, Version):
    '''
    user_param: {"RegionId":"cn-beijing", "LoadBalancerName":"test-node1", "AddressType":"intranet", "VSwitchId":"vsw-2zevjlczuvp2mkhhch12x"}
    Action操作例如:CreateLoadBalancer
    AccessKeyId
    '''
    parameters = {}
    parameters['HTTPMethod'] = 'GET'
    parameters['AccessKeyId'] = AccessKeyId
    parameters['Format'] = 'json'
    parameters['Version'] = Version
    parameters['SignatureMethod'] = 'HMAC-SHA1'
    parameters['Timestamp'] = get_iso8601_time()
    parameters['SignatureVersion'] = '1.0'
    parameters['SignatureNonce'] = get_uuid()
    parameters['Action'] = Action
    for (k, v) in sorted(user_param.items()):
        parameters[k] = v
    return parameters


def get_param(parameters):
    '''把公共参数拼接成字符串'''
    param_str = ''
    for (k, v) in sorted(parameters.items()):
        param_str += "&" + urllib.quote(k, safe='') + "=" + urllib.quote(v, safe='')
    param_str = param_str[1:]
    return param_str


def get_StringToSign(parameters, param_str):
    '''拼接生成签名的字符串'''
    StringToSign = parameters['HTTPMethod'] + "&%2F&" + urllib.quote(param_str, safe='')
    return StringToSign


def get_signature(StringToSign, AccessKeySecret):
    '''构建签名'''
    h = hmac.new(AccessKeySecret, StringToSign, hashlib.sha1)
    signature = base64.encodestring(h.digest()).strip()
    return signature


def build_request(server_url, param_str, signature, AccessKeySecret):
    '''拼接url并进行请求'''
    Signature = "Signature=" + urllib.quote(signature)
    param = param_str + "&" + Signature
    request_url = server_url + param
    s = requests.get(request_url)
    print s.content

def get_regions(server_url, Action, user_param, AccessKeySecret, AccessKeyId, Version):
    '''对请求进行模块
    server_url： slb.aliyun.com
    Action = 'DescribeRegions'
    AccessKeySecret, AccessKeyId:也就是ak
    user_param = {'LoadBalancerId': 'lb-2zekxu2elibyexxoo9hlw'}
    Version:例如slb的版本是2014-05-15,每个服务都不相同
    '''
    server_url = 'https://' + server_url + '/?'
    AccessKeySecret = AccessKeySecret
    AccessKeyId = AccessKeyId
    parameters = get_parameters(user_param, Action, AccessKeyId, Version)
    param_str = get_param(parameters)
    StringToSign = get_StringToSign(parameters, param_str)
    signature = get_signature(StringToSign, AccessKeySecret + '&')
    build_request(server_url, param_str, signature, AccessKeySecret)

'''
#create slb
Action = 'CreateLoadBalancer'
user_param = {"RegionId":"cn-beijing", "LoadBalancerName":"test-node1", "AddressType":"intranet", "VSwitchId":"vsw-2zevjlczuvp2mkhhch12x"}
server_url = 'slb.aliyuncs.com'
Version = '2014-05-15'
AccessKeySecret='xxx'
AccessKeyId='xxxx'
get_regions(server_url, Action, user_param, AccessKeySecret, AccessKeyId, Version)

#create user
Action = 'CreateUser'
user_param = {"UserName":"baishaohua", "DisplayName":"白少华", "Email":"shaohua.bai@dianjoy.com", "Comments":"测试用户"}
server_url = 'ram.aliyuncs.com'
AccessKeySecret='xxx'
AccessKeyId='xxx'
Version = '2015-05-01'
get_regions(server_url, Action, user_param, AccessKeySecret, AccessKeyId, Version)
'''
if __name__ == '__main__':
    print "please import this model"


