# coding=utf-8
"""

__created__ =  2017/6/24 12:12
__author__ = 'baishaohua'
# @Site    : https://github.com/bashhu
"""

import urllib2
import sys
macfile=open(sys.argv[1],'rU')
seq=0
for line in macfile:
    #跳过空行
    if line.strip() == '' :
        continue
    seq+=1
    #mac地址以':'分割
    if ':' in line :
        maclist=line.split(':')
        macstr='-'.join(maclist).strip()
    #mac地址以'-'分割
    else :
        macstr=line.strip()
    url='http://api.macvendors.com/'+macstr
    try:
        html=urllib2.urlopen(url,timeout=3).read()
    except urllib2.HTTPError:
        print '%-4d\t%-17s\t%s' %(seq,macstr,'[NOT FOUND]')
    except:
        print '%-4d\t%-17s\t%s' %(seq,macstr,'[OPEN ERROR]')
        continue
    else:
        print '%-4d\t%-17s\t%s' %(seq,macstr,html)
print 'done.'