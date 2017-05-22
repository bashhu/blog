#elasticsearch web 项目文档

##1. 安装包依赖
django==1.8.1

bootstrap==3.2.0


__elasticsearch的python API使用__
<pre>
from elasticsearch import Elasticsearch
es = Elasticsearch(('%s:%s' % (es.ip, es.port)))
</pre>

elasticsearch 的API文档
https://www.elastic.co/guide/en/elasticsearch/reference/5.0/modules-node.html


python SDK

__es.nodes.stats()__

这个函数是获取elasticsearch的node信息，其中包含node的系统信息，jvm，磁盘

__es.nodes.stats()['nodes']['Mp0wYL6tReSeXdTPhihIOA']['os']__
node的系统信息