# -*- coding: utf8 -*-
import os,sys
import hashlib
import hmac
import base64
import urllib
import time
import uuid
import requests

TIME_ZONE = "GMT"
FORMAT_ISO_8601 = "%Y-%m-%dT%H:%M:%SZ"

def get_signature(StringToSign, AccessKeySecret):
    h = hmac.new(AccessKeySecret, StringToSign, hashlib.sha1)
    return  base64.encodestring(h.digest()).strip()

uri='http://slb.aliyuncs.com?'
AccessKeySecret="xxxxxxxxxxxxxxxx"

parameters={}
parameters['HTTPMethod']='GET'
parameters['AccessKeyId']="xxxxxxxxxxxxx"
parameters['Format']='json'
parameters['Version']='2014-05-15'
parameters['SignatureMethod']='HMAC-SHA1'
parameters['Timestamp']=time.strftime(FORMAT_ISO_8601, time.gmtime())
parameters['SignatureVersion']='1.0'
parameters['SignatureNonce']=str(uuid.uuid4())
parameters['Action']='DescribeRegions'
parameters['LoadBalancerId']='lb-2zekxu2elibyexxoo9hlw'


param_str=''
for (k, v) in sorted(parameters.items()):
    param_str += "&" + urllib.quote(k, safe='') + "=" + urllib.quote(v, safe='')

param_str=param_str[1:]
StringToSign= parameters['HTTPMethod'] + "&%2F&"  +  urllib.quote(param_str, safe='')
print StringToSign


signature=get_signature(StringToSign, AccessKeySecret+'&')
Signature = "Signature=" + urllib.quote(signature)
param = param_str + "&" + Signature

request_url = uri  + param
print request_url

s=requests.get(request_url)
print s.content