from django.shortcuts import render
from .models import ES
from django.views.generic import ListView
from elasticsearch import Elasticsearch
import json


# Create your views here.
class HomeView(ListView):
    model = ES
    template_name = 'esweb/index.html'
    context_object_name = 'es_list'
def Home(request):
    es = ES.objects.get(id=1)
    es_con = Elasticsearch(('%s:%s' % (es.ip, es.port)))
    cluster = es_con.cluster.health()
    return render(request, 'esweb/index.html',{'es':es, 'cluster':cluster})

def indexs_list(request):
    es_dst = ES.objects.get(id=1)
    es = Elasticsearch(('%s:%s' % (es_dst.ip, es_dst.port)))
    res = es.cluster.state()
    node_list = res['nodes']
    index_list = res['routing_table']['indices'].keys()
    shards_list=[]
    for index in res['routing_table']['indices'].keys():
        for shards_id in res['routing_table']['indices'][index]['shards'].keys():
            for shards in res['routing_table']['indices'][index]['shards'][shards_id]:
                shards_list.append(shards)
    return render(request, 'esweb/index_list.html', {'es_dst': es_dst,'index_list': index_list, 'shards_list': shards_list, 'node_list': node_list})

def node_list(request):
    es_dst = ES.objects.get(id=1)
    es = Elasticsearch(('%s:%s' % (es_dst.ip, es_dst.port)))
    res = es.nodes.stats()['nodes']
    node_list = res.keys()
    res = es.nodes.stats()['nodes']
    return render(request, 'esweb/node_list.html',{'es_dst': es_dst,'node_list': node_list, 'res':res})

def es_info(request, id):
    es_dst = ES.objects.get(id=id)
    es = Elasticsearch(('%s:%s' % (es_dst.ip, es_dst.port)))
    info = es.info()
    info =  json.dumps(info, sort_keys=True, indent=2)
    return render(request, 'esweb/es_info.html', {'info': info, 'es': es_dst})

def es_search(request, index, arg):
    es_dst = ES.objects.get(id=id)
    es = Elasticsearch(('%s:%s' % (es_dst.ip, es_dst.port)))
    res = es.search(index,arg)
    return render(request, 'esweb/es_search.html', {'res': res})

def index_all_info(request):
    es_dst = ES.objects.get(id=1)
    es = Elasticsearch(('%s:%s' % (es_dst.ip, es_dst.port)))
    es.indices.stats()
    es.indices.stats('docker-2017_05')['indices']['docker-2017_05']['total']['docs']
    pass
def index_info(request):
    es_dst = ES.objects.get(id=1)
    es = Elasticsearch(('%s:%s' % (es_dst.ip, es_dst.port)))
    es.indices.stats()
    es.indices.stats('docker-2017_05')['indices']['docker-2017_05']['total']['docs']
    pass
def shards_info(request):
    pass

def node_info(request):
    pass

def search(request):
    pass