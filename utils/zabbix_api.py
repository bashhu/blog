#coding:utf-8
import json
import urllib2
import logging
logging.basicConfig(filename='./my_log_test.log', level=logging.INFO)

zbx_url = 'http://192.168.199.224:88/api_jsonrpc.php'
zabbix_user = 'admin'
zabbix_pwd = 'dianjoy.com'
class zbx_auth(object):
    '''help: https://www.zabbix.com/documentation/3.2/manual/api
    这里需要zabbix server url,User,password
    '''
    def get_token(self):
        url = zbx_url
        header = {"Content-Type": "application/json"}
        # auth user and password
        data = '''{
                "jsonrpc": "2.0",
                "method": "user.login",
                "params": {
                    "user": "%s",
                    "password": "%s"
                },
                "id": 0
            }''' % (zabbix_user,zabbix_pwd)
        #data = json.dumps(auth_str)
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
            msg ="Auth Successful. The Auth ID Is:%s" % response['result']
            logging.info(msg)
            return response['result']



class Zbx_base_api(object):
    def __init__(self, zbx_action, zbx_params):
        self.url = zbx_url
        self.header = {"Content-Type": "application/json"}
        r = zbx_auth()
        self.zbx_token = r.get_token()
        self.zbx_action = zbx_action
        self.zbx_params = zbx_params

    def zbx_req (self):
        ''' get host all graph '''
        data='''{
        "jsonrpc": "2.0",
        "method": "%s",
        "params": %s,
        "auth": "%s",
        "id": 1 }''' % (self.zbx_action, self.zbx_params, self.zbx_token)
        #data = json.dumps(s_data)
        print data
        request = urllib2.Request(self.url, data)

        for key in self.header:
            request.add_header(key, self.header[key])

        # auth and get authid
        try:
            result = urllib2.urlopen(request)
        except urllib2.URLError as e:
            print "Get Graph:", e.code
        else:
            #response = json.loads(result.read())
            return result.read()
            result.close()
            msg ="[%s] :%s" % (self.zbx_action, self.zbx_params)
            logging.info(msg)

class Zbx_api(object):
    def create_host(self,hostname,inter_ip,group_id,temlpate_id_list,proxy_hostid=0):
        '''创建主机
            hostname :主机名
            inter_ip :主机IP
            gourp_id :组id
            template_id : 监控模版id
            create_host('salt-node1','192.168.198.116','4','10001')
        '''
        self.hostname = hostname
        self.inter_ip = inter_ip
        self.group_id = group_id
        self.temlpate_id_list = temlpate_id_list
        self.temlpate_id=[]
        temlpate,temlpates = '',[]
        for temlpate_id in temlpate_id_list:
            temlpate = '{"templateid": "%d"}'% temlpate_id
            if len(temlpates)==0:
                temlpates = temlpate
            else:
                temlpates = '%s,%s' % (temlpates, temlpate)
        print temlpates
        zbx_action = 'host.create'

        zbx_params = '''{
            "host": "%s",
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": "%s",
                    "dns": "",
                    "port": "10050"
                }
            ],
            "groups": [
                {
                    "groupid": "%s"
                }
            ],
            "templates": [%s],
            "inventory_mode": 0,
            "inventory": {
                "macaddress_a": "01234",
                "macaddress_b": "56768"
            },
            "proxy_hostid": %s
            }''' % (hostname,inter_ip,group_id,temlpates,proxy_hostid)
        r=Zbx_base_api(zbx_action,zbx_params)
        return r.zbx_req()

    def update_host(self,host_id,temlpate_id):
        '''
        更新模版为这里配置的参数
        host_id :主机id
        temlpate_id :模版id
        update_host('10106','10093')
        '''
        self.host_id = host_id
        self.temlpate_id =temlpate_id
        zbx_action = 'host.update'
        zbx_params = '''{
            "hostid": "%s",
            "templates": [
                {
                    "templateid": "%s"
                }
            ]
        }''' % (host_id,temlpate_id)
        print   zbx_params
        r=Zbx_base_api(zbx_action,zbx_params)
        return r.zbx_req()

    def get_host(self, host_name):
        ''' 查看主机组信息
         参数：host_name
         s=Zbx_api()
        gstr="Zabbix server"
        print s.get_host(gstr)
        '''
        zbx_action = 'host.get'
        self.host_name = host_name
        zbx_params = '''{
        "output": "extend",
        "filter": {
            "name": [
                "%s"
            ]
        }
    }''' % (self.host_name)
        r = Zbx_base_api(zbx_action, zbx_params)
        return r.zbx_req()

    def create_group(self,group_name):
        ''' 创建主机组 '''
        zbx_action = 'hostgroup.create'
        zbx_params = '''{
            "hostid": "%s",
            "templates": "%s"
        }''' % (group_name)
        print   zbx_params
        r=Zbx_base_api(zbx_action,zbx_params)
        return r.zbx_req()

    def exists_group(self,group_name):
        ''' 查看主机组是否存在 '''
        self.group_name = group_name
        zbx_action = 'hostgroup.exists'
        zbx_params = '''{
            "hostid": "%s",
            "templates": "%s"
        }''' % (self.group_name)
        print   zbx_params
        r=Zbx_base_api(zbx_action,zbx_params)
        return r.zbx_req()

    def get_group(self, group_name):
        ''' 查看主机组信息 
        s=Zbx_api()
        res=s.get_group('aliyun-dianjoy-video')
        print res['groupid']
        '''
        zbx_action = 'hostgroup.get'
        self.group_name = group_name
        zbx_params = '''{
        "output": "extend",
        "filter": {
            "name": [
                "%s"
                ]
            }
        }''' % (self.group_name)
        r = Zbx_base_api(zbx_action, zbx_params)

        return json.loads(r.zbx_req())['result'][0]

    def create_screen(self,screen_name,screen_high,screen_width):
        '''创建screen
        name : SCREEN的名字
        hsize： screen的行数
        vsize： screen的列数
        screenitems： screen里面的item
            resourcetype : 当前数据源的类型"graph","map","url"更多请看传送门https://www.zabbix.com/documentation/2.4/manual/api/reference/screenitem/object#screen_item
            resourceid： itemid
            rowspan: 占据行数
            colspan：占据列数
            x： 屏幕x坐标轴位置
            y:  屏幕y坐标轴位置
         '''
        self.screen_name = screen_name
        self.screen_high = screen_high
        self.screen_width = screen_width
        zbx_action = 'screen.create'
        zbx_params = '''{
        "name": "%s",
        "hsize": %s,
        "vsize": %s,
        "screenitems": [
            {
                "resourcetype": 0,
                "resourceid": "524",
                "rowspan": 1,
                "colspan": 1,
                "x": 0,
                "y": 2
            }
        ]
    }''' % (self.screen_name,self.screen_high,self.screen_width)
        print   zbx_params
        r=Zbx_base_api(zbx_action,zbx_params)
        return r.zbx_req()

    def update_screen(self, screen_id,h_size,v_size,item_ids):
        '''创建screen
        name : SCREEN的名字
        screen_id: screen的id
        hsize： screen的宽度
        vsize： screen的高度
        screenitems： screen里面的item
            resourcetype : 当前数据源的类型"graph","map","url"更多请看传送门https://www.zabbix.com/documentation/2.4/manual/api/reference/screenitem/object#screen_item
            resourceid： itemid
            rowspan: 占据行数
            colspan：占据列数
            x： 屏幕x坐标轴位置
            y:  屏幕y坐标轴位置
            item_id: 是一个list ["itemid1","itemid2"]
            s=Zbx_api()
            s.zbx_update_screen("24","3","3",[517,547,549,526])
            s=Zbx_api()
            print s.zbx_update_screen("16","2","5",[523,524,555,556,557,558,559,560,583,579])
         '''
        self.screen_id = screen_id
        self.h_size = int(h_size)
        self.v_size = int(v_size)
        self.item_ids = item_ids
        row_id = 0
        col_id = 0
        item_str = []
        for item_id in self.item_ids:
            if  col_id < self.h_size and row_id < self.v_size:
                s = '''{
                      "resourcetype": 0,
                      "resourceid": "%s",
                      "rowspan": 1,
                      "colspan": 1,
                      "x": %s,
                      "y": %s
                      }''' % (item_id, col_id, row_id)
                item_str.append(s)
                print "show:", row_id, col_id, item_id
            elif row_id < self.v_size and col_id == self.h_size:
                col_id = 0
                row_id = row_id + 1
                if row_id < self.v_size:
                    s = '''{
                      "resourcetype": 0,
                      "resourceid": "%s",
                      "rowspan": 1,
                      "colspan": 1,
                      "x": %s,
                      "y": %s
                      }''' % (item_id, col_id, row_id)
                    item_str.append(s)
                    print "show:", row_id, col_id,item_id
                else:
                    print "column or row is too less !!!"
                    break
            else:
                print "column or row is too less !!!"
                break
            col_id = col_id + 1

        zbx_action = 'screen.update'
        item_id_list = ','.join(item_str)
        zbx_params = '''{
        "screenid": "%s",
        "hsize": %s,
        "vsize": %s,
        "screenitems": [%s]
    }''' % (self.screen_id,self.h_size,self.v_size,item_id_list)
        r = Zbx_base_api(zbx_action, zbx_params)
        return r.zbx_req()

    def get_tpl(self,template_name):
        ''' 查看模版信息 
        s=Zbx_api()
        res=s.get_tpl('aliyun-video-api')
        print res['templateid']

        '''
        zbx_action = 'template.get'
        self.template_name = template_name
        zbx_params = '''{
        "output": "extend",
        "filter": {
            "host": [
                "%s"
                ]
            }
        }''' % (self.template_name)
        r = Zbx_base_api(zbx_action, zbx_params)

        return json.loads(r.zbx_req())['result'][0]



zbx=Zbx_api()
group_id = zbx.get_group("aliyun-dianjoy-video")['groupid']
template_id = zbx.get_tpl('aliyun-video-api')['templateid']
inter_ip = '192.168.199.217'
hostname = 'ntest7.dianjoy.com'
proxy_hostid=10119
template_id_list=[10117,10001]
print zbx.create_host(hostname,inter_ip,group_id,template_id_list,proxy_hostid)