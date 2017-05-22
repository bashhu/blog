# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
# Create your views here.
''' index.html 
def home(request):
    
    posts = Article.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'article/index.html', {'post_list': post_list})
'''

class Indexview(generic.ListView):
    model = Article
    template_name = 'article/index.html'
    context_object_name = 'post_list'
    def home(self,request):
        posts = Article.objects.all()
        paginator = Paginator(posts, 2)
        page = request.GET.get('page')


class DetailView(generic.DetailView):
    ''' looking one blog page
         try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    #post.content = post.content.replace(' ', '&nbsp;').replace('\n', '<br>')
    return render(request, 'article/post.html', {'post': post})'''
    model = Article
    template_name = 'article/post.html'
    context_object_name = 'post'

def Search_tag(request, tag):
    ''' search blog us tag'''
    try:
        post_list = Article.objects.filter(category__iexact = tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article/tag.html', {'post_list': post_list})





class ArchView(generic.ListView):
    ''' watching all blog '''
    model = Article
    template_name = 'article/archives.html'
    context_object_name = 'post_list'


def about_me(request):
    return render(request, 'article/aboutme.html')



def blog_search(request):
    '''blog title search with word'''
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'article/home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0:
                return render(request, 'article/archives.html', {'post_list': post_list, 'error': True})
            else:
                return render(request, 'article/archives.html', {'post_list': post_list, 'error': False})
    return redirect('/')

class RSSFeed(Feed):
    ''' manage you Rss '''
    title = 'RSS Feed - article'
    link = "feeds/posts/"
    description = "Rss Feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content