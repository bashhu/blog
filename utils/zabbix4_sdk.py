#coding:utf-8
import json
import urllib2,requests
import logging
import pdb
logging.basicConfig(filename='./my_log_test.log', level=logging.INFO)


class Zbx(object):
    '''help: https://www.zabbix.com/documentation/3.2/manual/api
    这里需要zabbix server url,User,password
    '''

    def __init__(self, *args, **kwargs):

        parms = ['url','user','passwd']
        for parm in parms:
            if parm not in kwargs:
                print "Zabx class init Fail,", parm, "is null !!!"

        self.url = kwargs['url']
        self.user = kwargs['user']
        self.passwd = kwargs['passwd']

        self.header = {"Content-Type": "application/json-rpc"}
        # auth user and password
        data = '''{
                "jsonrpc": "2.0",
                "method": "user.login",
                "params": {
                    "user": "%s",
                    "password": "%s"
                },
                "id": 0
            }''' % (self.user, self.passwd)

        # create request object

        self.request = urllib2.Request(self.url, data)
        for key in self.header:
            self.request.add_header(key,self.header[key])

        try:
            result = urllib2.urlopen(self.request)
        except urllib2.URLError as e:
            print "Auth Failed, Please Check Your Name And Password:",e.code
        else:
            response = json.loads(result.read())
            result.close()
            self.token = response['result']
            print self.token

    def get_api_info(self):
        method="apiinfo.version"
        params={
            "jsonrpc": "2.0",
            "method": method,
            "params": {},
            "auth": str(self.token),
            "id": 1
        }
        ret = requests.get(self.url, headers=self.header, data=params)
        pdb.set_trace()
        # auth and get authid
        try:
            result = urllib2.urlopen(self.request)
            pdb.set_trace()
        except urllib2.URLError as e:
            print "Get Graph:", e.code
        else:
            # response = json.loads(result.read())
            return result.read()
            result.close()


if __name__ == '__main__':
    zbx_url = 'http://127.0.0.1:80/zabbix/api_jsonrpc.php'
    zabbix_user = 'admin_api'
    zabbix_pwd = 'nginxs.net'

    zbx = Zbx(url=zbx_url, user=zabbix_user, passwd=zabbix_pwd)
    print zbx.get_api_info()
