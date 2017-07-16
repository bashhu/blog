# -*- coding: utf8 -*-
import os,sys
import hashlib
import hmac
import base64
import urllib
import time
import uuid
import requests
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

def _get_md5(content):
    m = hashlib.md5()
    m.update(buffer(content))
    return m.digest()

def get_md5_base64_str(content):
    return base64.encodestring(_get_md5(content)).strip()



class mac1(object):
    '''
    source：加密字符串
    secret：AccessKeySecret
    '''
    def get_sign_string(self, source, secret):
        h = hmac.new(secret, source, hashlib.sha1)
        signature = base64.encodestring(h.digest()).strip()
        return signature


    def get_signer_name(self):
        return "HMAC-SHA1"


    def get_singer_version(self):
        return "1.0"


class ShaHmac256:
    def __init__(self):
        pass

    def get_sign_string(self, source, accessSecret):
        h = hmac.new(accessSecret, source, hashlib.sha256)
        signature = base64.encodestring(h.digest()).strip()
        return signature

    def get_signer_name(self):
        return "HMAC-SHA256"

    def get_singer_version(self):
        return "1.0"

def get_encode_str(params):
    """
    transforms parameters to encoded string
    :param params: dict parameters
    :return: string
    """
    list_params = sorted(params.iteritems(), key=lambda d: d[0])
    encode_str = urllib.urlencode(list_params)
    if sys.stdin.encoding is None:
        res = urllib.quote(encode_str.decode('cp936').encode('utf8'), '')
    else:
        res = urllib.quote(
            encode_str.decode(
                sys.stdin.encoding).encode('utf8'), '')
    res = res.replace("+", "%20")
    res = res.replace("*", "%2A")
    res = res.replace("%7E", "~")
    return res

def __pop_standard_urlencode(query):
    ret = urllib.urlencode(query)
    ret = ret.replace('+', '%20')
    ret = ret.replace('*', '%2A')
    ret = ret.replace('%7E', '~')
    return ret

class helper(object):
    def __init__(self):
        self.TIME_ZONE = "GMT"
        self.FORMAT_ISO_8601 = "%Y-%m-%dT%H:%M:%SZ"
        self.FORMAT_RFC_2616 = "%a, %d %b %Y %X GMT"

    def get_uuid(self):
        return str(uuid.uuid4())

    def get_iso_8061_date(self):
        return time.strftime(self.FORMAT_ISO_8601, time.gmtime())

    def get_rfc_2616_date(self):
        return time.strftime(self.FORMAT_RFC_2616, time.gmtime())

def sign_parameters(
        parameters,
        access_key_id,
        accept_format="JSON",
        signer=mac1):
    if parameters is None or not isinstance(parameters, dict):
        parameters = dict()
    parameters["Timestamp"] = helper.get_iso_8061_date()
    parameters["SignatureMethod"] = signer.get_signer_name()
    parameters["SignatureVersion"] = signer.get_singer_version()
    parameters["SignatureNonce"] = helper.get_uuid()
    parameters["AccessKeyId"] = access_key_id
    if accept_format is not None:
        parameters["Format"] = accept_format
    return parameters

def __compose_string_to_sign(method, queries):
    canonicalized_query_string = ""
    sorted_parameters = sorted(queries.items(), key=lambda queries: queries[0])
    string_to_sign = method + "&%2F&" + \
        urllib.pathname2url(__pop_standard_urlencode(sorted_parameters))
    return string_to_sign

def hmac_sha1(content, key):
    base_str = hmac.new(key, content, hashlib.sha1).digest()
    return base64.b64encode(base_str)
uri='http://slb.aliyuncs.com?'
AccessKeySecret="xxxxxxxxxxxxxxxxxxxxxxxxxx"
parameters={}
ttime=helper()
parameters['HTTPMethod']='GET'
parameters['AccessKeyId']="xxxxxxxxxxxxxxxxxx"
parameters['Format']='json'
parameters['Version']='2014-05-15'
parameters['SignatureMethod']='HMAC-SHA1'
parameters['Timestamp']=ttime.get_iso_8061_date()
parameters['SignatureVersion']='1.0'
parameters['SignatureNonce']=ttime.get_uuid()
parameters['Action']='DescribeRegions'
parameters['LoadBalancerId']='lb-2zekxu2elibyexxoo9hlw'
#''
#
param_str_encode=''
param_str=''
for (k, v) in sorted(parameters.items()):
    param_str += "&" + urllib.quote(k, safe='') + "=" + urllib.quote(v, safe='')

print param_str
param_str=param_str[1:]
StringToSign= parameters['HTTPMethod'] + "&%2F&"  +  urllib.quote(param_str, safe='')
print StringToSign

base_str = hmac.new(AccessKeySecret+'&', StringToSign, hashlib.sha1).digest()
signature=base64.b64encode(base_str)
Signature = "Signature=" + urllib.quote(signature)
param = param_str + "&" + Signature

request_url = uri  + param
print request_url

s=requests.get(request_url)
print s.content