# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkslb.request.v20140515 import DescribeRegionsRequest,AddBackendServersRequest,RemoveBackendServersRequest,SetBackendServersRequest,DescribeHealthStatusRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
# 创建 AcsClient 实例
client = AcsClient(
    "xxxxxxxxx",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "cn-beijing"
);

def add_server(slbid, server_list):
    '''
     创建 request，并设置参数
     slbid=>'lb-2zekxu2elibyexxoo9hlw'
    server_list=>[{"ServerId": "slb_id_1", "Weight": "100"},
    {"ServerId": "slb_id_2", "Weight": "100"}
    ]
    '''
    request = AddBackendServersRequest.AddBackendServersRequest()
    # 发起 API和参数 请求
    request.set_accept_format('json')
    request.set_LoadBalancerId(slbid)
    request.set_BackendServers(server_list)
    # 并打印返回
    response = client.do_action_with_exception(request)
    print response

def remove_server(slbid, ecsid_list):
    '''创建 request，并设置参数
    slbid:是负载均衡ID
     ecsid_list：['slb_id_1','slb_id_2','slb_id_3']
    '''
    request = RemoveBackendServersRequest.RemoveBackendServersRequest()
    request.set_accept_format('json')
    request.set_LoadBalancerId(slbid)
    request.set_BackendServers(ecsid_list)
    response = client.do_action_with_exception(request)
    print response

def set_wight(slbid, server_list):
    '''
     创建 request，并设置参数
     slbid=>'lb-2zekxu2elibyexxoo9hlw'
    server_list=>[{"ServerId": "slb_id_1", "Weight": "100"},
    {"ServerId": "slb_id_2", "Weight": "100"}
    ]
    '''
    request = SetBackendServersRequest.SetBackendServersRequest()
    # 发起 API和参数 请求
    request.set_accept_format('json')
    request.set_LoadBalancerId(slbid)
    request.set_BackendServers(server_list)
    # 并打印返回
    response = client.do_action_with_exception(request)
    print response


def health_status(slbid, port):
    '''创建 request，并设置参数
    slbid:是负载均衡ID
     ecsid_list：['slb_id_1','slb_id_2','slb_id_3']
    '''
    request = DescribeHealthStatusRequest.DescribeHealthStatusRequest()
    request.set_accept_format('json')
    request.set_LoadBalancerId(slbid)
    request.set_ListenerPort(port)
    response = client.do_action_with_exception(request)
    print response

def create_slb(LoadBalancerName, AddressType, VSwitchId):
    '''
    LoadBalancerName='test-slb-01'
    AddressType='intranet'
    VSwitchId='vsw-2ze130t0mdnzmtvx7uyck'
    create_slb(LoadBalancerName, AddressType,  VSwitchId)
    '''
    from aliyunsdkslb.request.v20140515 import CreateLoadBalancerRequest
    request = CreateLoadBalancerRequest.CreateLoadBalancerRequest()
    request.set_accept_format('json')
    request.set_LoadBalancerName(LoadBalancerName)
    request.set_AddressType(AddressType)
    request.set_VSwitchId(VSwitchId)
    response = client.do_action_with_exception(request)
    print response

def slb_regionid():
    '''
    slb_regionid():查看区域列表
    '''
    from aliyunsdkslb.request.v20140515 import DescribeRegionsRequest
    request = DescribeRegionsRequest.DescribeRegionsRequest()
    request.set_accept_format('json')
    response = client.do_action_with_exception(request)
    print response




