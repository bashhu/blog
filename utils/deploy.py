#!/usr/bin/env python
#coding:utf-8
############################################################
# Name:         auth_deploy.py
# Version:      v2.0
# Function:     deploy auth api Server
# Author:       baishaohua
# organization: auth.91atm.com
# Create Date:  2017-05-11
############################################################
import os,tarfile,shutil,paramiko
import datetime,time
from gittle import Gittle,GittleAuth


''' Date/Time veriables'''



def sftp_host(host, private_key, user='www', port=22):
    pkey=paramiko.RSAKey.from_private_key_file(private_key)
    scp = paramiko.Transport((host,port))
    scp.connect(pkey=pkey,username=user)
    sftp = paramiko.SFTPClient.from_transport(scp)
    return sftp
def ssh_host(cmd, host, private_key, user='www', port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        pkey=paramiko.RSAKey.from_private_key_file(private_key)
        ssh.load_system_host_keys()
        ssh.connect(host, port, user, pkey)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        res = stdout.read()
        err = stderr.read()
        ssh.close()
        return res
    except:
        res='ssh connect error'
        return res

def echo_info(context):
    print "\033[1;34;42m %s \033[0m" % context
def echo_warn(context):
    print "\033[5;34m %s \033[0m" % context
def echo_error(context):
    print "\033[4;41m %s \033[0m" % context
class Project(object):
    def __init__(self, CONFIG_SRC, CODE_DIR, TMP_DIR, DST_DIR, PRO_NAME, REPO_URL,HOST_FILE, key_file, port=22, user='www'):
        self.CONFIG_SRC = CONFIG_SRC
        self.CODE_DIR = CODE_DIR
        self.TMP_DIR = TMP_DIR
        self.DST_DIR = DST_DIR
        self.PRO_NAME = PRO_NAME
        self.REPO_URL = REPO_URL
        self.SHELLNAME = __file__
        self.SCRIPTDIR = os.getcwd()
        self.HOST_FILE = HOST_FILE
        self.key_file = key_file
        self.user = user
        self.port = port
        self.CTIME= time.strftime('%Y_%m_%d_%H_%M')
        #self.LOGFILE='./log/{SHELLNAME}_{CTIME}.log'.format(SHELLNAME=SHELLNAME, CTIME=CTIME)
        
        
    def usage():
        print("Usage: %s [ deploy  | restart ]" % SHELLNAME)
    
    
    def git_pull(self, TMP_DIR, CODE_DIR):
        ''' git pull code
            use commit id tag you code
        lastest = [info['sha'] for info in repo.commit_info()[1:3]]
        print((repo.diff(*lastest, diff_type='classic')))
        '''
        print("========%s: git pull for env:test=========" % self.PRO_NAME)
        repo = Gittle(self.CODE_DIR, self.REPO_URL)
        command= 'cd %s && git pull' % self.CODE_DIR
        os.system('command')
        COMMIT_ID=repo.commit()[0:-30]
        CVER="%s_%s_%s" % (self.PRO_NAME, self.CTIME, COMMIT_ID)
        CODE_TMP = '%s/%s' % (TMP_DIR, CVER)
        shutil.copytree(CODE_DIR, CODE_TMP)
        echo_info("git pull success")
        return CVER
        
    
    def config(self, CVER,  CONFIG_SRC, CONFIG_DST=None):
        ''' cp config file to code '''
        if CONFIG_DST == None:
            CONFIG_DST = '%s/%s' %(self.TMP_DIR, CVER)
        else:
            CONFIG_DST  = '%s/%s%s' %(TMP_DIR, CVER, CONFIG_DST)
        print("====%s: copy test config to code dir=====" % self.PRO_NAME)
        command = '/bin/cp -r %s %s ' % (CONFIG_SRC, CONFIG_DST)
        os.system(command)
    
    def scp(self, CVER):
        ''' CVER: code version
		pk_name: packages name
		dst_dir: client code.tar.gz dir
		dst_fil: client code.tar.gz path
		'''
        print "=====scp %s : %s.tar.gz====" % (self.PRO_NAME, CVER)
        CODE_TMP = '%s/%s' %(self.TMP_DIR, CVER)
        shutil.make_archive(CODE_TMP, 'gztar', CODE_TMP)
        pk_name = '%s.tar.gz' % CODE_TMP
        dst_file = '%s/%s.tar.gz' % (self.DST_DIR, CVER)
        dst_dir = '%s/%s' % (self.DST_DIR, CVER)
        f=open(self.HOST_FILE)
        ip_list=f.readlines()
        for ip in ip_list:
            ip = ip.strip('\n')
            try:
                print ip, self.key_file, self.user, self.port
                sftp = sftp_host(ip, self.key_file, self.user, self.port)
                sftp.put(pk_name, dst_file)
                echo_info(("%s code scp success" % ip))
            except:
                echo_error(("%s  code scp Failed !!!" % ip))
        sftp.mkdir(dst_dir)
        
    def deploy(self, CVER, WEB_ROOT):
        '''
        dst_dir: 拷贝到客户端节点目录
        cmd: 执行的解压命令
        '''
        print("=========== deploy %s code =========" % self.PRO_NAME)
        dst_dir = '%s/%s' % (self.DST_DIR, CVER)
        cmd = "tar zxf %s.tar.gz -C %s" % (dst_dir, dst_dir)
        f=open(self.HOST_FILE)
        ip_list=f.readlines()
        for ip in ip_list:
            ip = ip.strip('\n')
            res = ssh_host(cmd, ip, self.key_file, self.user, self.port)
            sftp = sftp_host(ip, self.key_file, self.user, self.port)
            echo_info(("%s remote exec success" % ip))
            try:
                sftp.unlink(WEB_ROOT)
                sftp.symlink(dst_dir, WEB_ROOT)
                echo_info(("%s remote deploy success" % ip))
            except:
                echo_WARN(("The %s does not have WEBROOT ,Create now  !!!" % ip))
                sftp.symlink(dst_dir, WEB_ROOT)

    def reload(self,recmd):
        '''
        recmd: restart service command
        '''
        print ("============ %s Reload Service  ========" % self.PRO_NAME)
        f=open(self.HOST_FILE)
        ip_list=f.readlines()
        for ip in ip_list:
            ip = ip.strip('\n')
            #try:
            res = ssh_host(recmd, ip, self.key_file, self.user, self.port)
            if res.strip()=='':
                echo_error(("%s service or command is Not Exist !!!" % ip))
            else:
                echo_info(("%s reload success,result: %s" % (ip, res.strip())))
            #except:

if __name__ == "__main__":
    ''' Shell variables
      SHELLNAME: you shell name
      SCRIPTDIR: shell path
     CONFIG_SRC: Project configuration source file
       CODE_DIR: Project code source path(git clone from gitlab)
        TMP_DIR: The code here adds configuration files and packages
       REPO_URL: gitlab path
       key_file: The private key to connect to another node
      user/port: ssh or scp user/port
       PRO_NAME: project name,example: oms, baidu, qq, blog
      HOST_FILE: The client host name or IP to be deployed
        DST_DIR: Client code save location
    '''
    SHELLNAME = __file__
    SCRIPTDIR = os.getcwd()
    DEPLOY_DIR="/data/deploy"
    CONFIG_SRC="/data/deploy/config/auth"
    CODE_DIR = "/data/deploy/code/web-api"
    TMP_DIR  = "/data/deploy/web-tmp"
    REPO_URL = 'git@github.com:bashhu/jumpserver.git'
    key_file = '/home/www/.ssh/id_rsa'
    user = 'www'
    port = 22
    PRO_NAME = 'salt'
    HOST_FILE = './host.list'
    DST_DIR = '/data'
    #example: begin deploy code
    deploy = Project(CONFIG_SRC, CODE_DIR, TMP_DIR, DST_DIR, PRO_NAME, HOST_FILE, key_file)
    code_version = deploy.git_pull(TMP_DIR, CODE_DIR)
    deploy.config(code_version, CONFIG_SRC)
    deploy.scp(code_version)
    deploy.deploy(code_version, '/WEBROOT/jump_server')
    deploy.reload('sudo /etc/init.d/php-fpm reload')
