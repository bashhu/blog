#coding:utf-8
import json
import urllib2
import logging
import ssl
import time
'''因为salt-api默认没有CA证书,所以需要忽略验证，否则会出现证书验证问题'''
ssl._create_default_https_context = ssl._create_unverified_context
logging.basicConfig(filename='./salt-api.log', level=logging.INFO)

SALT_API_HOST = "http://localhost:8000/"
SALT_API_USER = "saltapi"
SALT_API_PASSWORD = "saltapi"



class Salt_auth(object):
    '''help: http://salt-api.readthedocs.io/en/latest/ref/netapis/all/saltapi.netapi.rest_cherrypy.html#authentication
    这里需要salt-api url,User,password
    '''
    def get_token(self):
        url = SALT_API_HOST + "/login"
        salt_user_name = SALT_API_USER
        salt_user_pwd = SALT_API_PASSWORD
        header = {"Content-Type": "application/json"}
        # auth user and password
        data = '''{"username":"%s","password":"%s","eauth":"pam"}''' % (salt_user_name,salt_user_pwd)
        # create request object
        request = urllib2.Request(url,data)
        for key in header:
            request.add_header(key,header[key])
            # auth and get authid
        try:
            result = urllib2.urlopen(request)
        except urllib2.URLError as e:
            print "Auth Failed, Please Check Your Name And Password:",e.code
        else:
            response = json.loads(result.read())
            result.close()
            #msg ="Auth Successful. The Auth ID Is:%s" % response['return'][0]['token']
            logging.info(data)
            return response['return'][0]['token']


class Salt_base_api(object):
    def __init__(self):
        '''初始化url，用户，密码，获取token后添加到header
        % curl -sS localhost:8000/run \
         -H 'Accept: application/x-yaml' \
         -d client='local' \
         -d tgt='*' \
         -d fun='test.ping' \
         -d username='saltdev' \
         -d password='saltdev' \
         -d eauth='pam
        '''
        r = Salt_auth()
        salt_user_token = r.get_token()
        self.header = {"Content-Type": "application/json","Accept":"application/json","X-Auth-Token": salt_user_token}
        print self.header

    def salt_req (self,salt_params,salt_path):
        ''' 构建请求模型 
        s=Salt_base_api()
        print s.salt_req('{ "tgt":"*","fun":"test.ping"}','/minions')'''
        self.salt_path = salt_path
        self.salt_params = salt_params
        self.url = SALT_API_HOST + self.salt_path
        self.data = self.salt_params
        request = urllib2.Request(self.url, self.data)

        for key in self.header:
            request.add_header(key, self.header[key])
        # auth and get authid
        try:
            logging.info(self.data)
            result = urllib2.urlopen(request)
        except urllib2.URLError as e:
            print "Get result:", e.code
        else:
            response = json.loads(result.read())
            return response
            result.close()
            logging.info(response)

    def salt_gethost_info(self,tgt_name):
        ''' 查询host的全部静态信息 grains.items '''
        self.tgt_name = tgt_name
        self.url = SALT_API_HOST + self.tgt_name
        request = urllib2.Request(self.url)

        for key in self.header:
            request.add_header(key, self.header[key])
        # auth and get authid
        try:
            result = urllib2.urlopen(request)
        except urllib2.URLError as e:
            print "Get result:", e.code
        else:
            response = json.loads(result.read())
            for res in response['return'][0]:
                return response['return'][0][res]
            result.close()
            logging.info(response)

    def salt_get_job(self,salt_job_id):
        ''' 查询job '''
        self.salt_job_id = salt_job_id
        self.url = SALT_API_HOST +"/jobs/"+ self.salt_job_id
        print self.url
        request = urllib2.Request(self.url)

        for key in self.header:
            request.add_header(key, self.header[key])
        # auth and get authid
        try:
            result = urllib2.urlopen(request)
            print result.read()
        except urllib2.URLError as e:
            print "Get result:", e.code
        else:
            response = json.loads(result.read())
            return response
            result.close()
            logging.info(response)

    def salt_cmd_run(self,tgt_name,salt_arg):
        ''' 使用cmd.run模块
         tgt_name：操作目标主机名
         salt_arg：操作命令参数
         '''
        self.salt_arg = salt_arg
        self.tgt_name = tgt_name
        self.url = SALT_API_HOST
        self.data = '''{
        "client":"local",
        "tgt":"%s",
        "fun":"cmd.run",
        "arg":"%s",
        "eauth":"pam"
        }''' % (self.tgt_name, self.salt_arg)
        print self.data
        request = urllib2.Request(self.url, self.data)

        for key in self.header:
            request.add_header(key, self.header[key])
        # auth and get authid
        try:
            result = urllib2.urlopen(request)
        except urllib2.URLError as e:
            print "Get result:", e.code
        else:
            response = result.read()
            result.close()
            for res in response['return'][0]:
                print "%s exec result: \n%s" % (res,response['return'][0][res])
            #return response
            logging.info(result)
            return response

    def salt_create_zbx_host(self, tgt_name, salt_arg):
        ''' 使用salt创建zabbix host
        from zabbix_api import Zbx_api
        salt_host = Zbx_api
        host_info = s.salt_get_info('/minions/salt-master')
        salt_host.zbx_create_host(hostname=,inter_ip=,group_id=,temlpate_id=)'''
        pass

#s=Salt_base_api()
#print s.salt_req('{ "tgt":"*","fun":"test.ping"}','/minions')
#print s.salt_req('{ "tgt":"ntest2.dianjoy.com","fun":"test.ping"}','/minions')
#print s.salt_get_info('/minions/salt-master')

#ntest2.dianjoy.com
#res=s.salt_req('{ "client":"local","tgt":"ntest2.dianjoy.com","fun":"cmd.run","arg":"w"}','')
#res=s.salt_req('{ "client":"local","tgt":"ntest2.dianjoy.com","fun":"cmd.run","arg":"df"}','')
#print res

#f = open('yaq.json', mode='a+')
#f.write('\naaavvvv\n')
#f.flush()
#f.close()
#headers = { 'Host':"map.baidu.com", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.5", "Connection": "keep-alive", "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0" }
#import requests
#url='http://www.baidu.com'
#s=requests.get(url,headers,proxy)
