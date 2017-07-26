# coding=utf-8
"""

__created__ =  2017/7/26 14:52
__author__ = 'baishaohua'
# @Site    : https://github.com/bashhu
"""

import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109 import  DescribeDomainRecordsRequest,UpdateDomainRecordRequest,DeleteDomainRecordRequest

# 创建 AcsClient 实例
client = AcsClient(
    "xxxx",
    "xxxxx",
    "cn-beijing"
);

def get_dns_records(domain):
    request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    # 发起 API和参数 请求
    request.set_accept_format('json')
    request.set_DomainName(domain)
    # 并打印返回
    response = client.do_action_with_exception(request)
    f = open('./record.txt','a+')
    f.write("%s\n" % response)
    f.close()
    return response

def update_dns_records(RecordId,RR,Type,Value):
    request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    # 发起 API和参数 请求
    request.set_accept_format('json')
    request.set_RecordId(RecordId)
    request.set_RR(RR)
    request.set_Type(Type)
    request.set_Value(Value)
    # 并打印返回
    response = client.do_action_with_exception(request)
    f = open('./record.txt', 'a+')
    f.write("%s\n" % response)
    f.close()


def delete_dns_records(RecordId):
    request = DeleteDomainRecordRequest.DeleteDomainRecordRequest()
    # 发起 API和参数 请求
    request.set_accept_format('json')
    request.set_RecordId(RecordId)
    # 并打印返回
    response = client.do_action_with_exception(request)
    f = open('./record.txt', 'a+')
    f.write("%s\n" % response)
    f.close()
    print response

list=open('./utils/list.txt')
l = list.readlines()
list.close()
for i in l:
    result = get_dns_records(i.strip('\n'))
    result = json.loads(result)

    for i in result['DomainRecords']['Record']:
        if i['Value'] == '192.168.1.10':
            print  i







