# coding=utf-8
"""
__created__ =  2017/6/9 17:33
__author__ = 'baishaohua'
# @Site    : https://github.com/bashhu
"""
import ConfigParser,sys,os,time

class Config(object):
    def __init__(self, file_path):
        '''初始化类，并加载配置文件'''
        conf_file = file_path
        self.config = ConfigParser.ConfigParser()
        conf = self.config.read(conf_file)

    def load_config(self, project):
        if self.config.has_section(project):
            node = self.config.get(project, "node").split(',')
            port = self.config.get(project, "port")
            home = self.config.get(project, "home")
            print home

            print """
                node: %s
                port: %s
                home: %s
            """ % (node, port, home)

            return node, port, home
        else:
            print "not exist %s" % project
            sys.exit(1)

#类的继承
class A():
    def foo1(self):
        print "A"
    def __unicode__(self):
        return "A"
class B(A):
    def foo2(self):
        pass
class C(A):
    def foo1(self):
        print "C"
class D(B, C):
    pass

def log(text):
    def info(func):
        def text(*args):
            print '[INFO]:',args
            return func(*args)
    return info

def now():
    print '2013-12-25'



def test1(*args, **kw):
    for i in args:
        print 'value:',i

    for key in kw:
        print "%s:%s" % (key, kw[key])


##类的初始化参数
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = int(score)

    def __unicode__(self):
        print "A"

    def level(self):
        if self.__score >90:
            print "%s is A" % (self.name)
        elif self.__score >80 :
            print "%s is B" % (self.name)
        elif self.__score >60 :
            return "%s is C" % (self.name)
        else:
            print "%s is D" % (self.name)


##迭代器
def testA():
    f=open('./test/test.conf')
    for i in f.readlines():
        yield i
    f.close()

s= testA()
print s.next()
print s.next()

