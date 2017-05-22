#coding:utf-8
from django.contrib import admin
from article.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_time')
admin.site.register(Article
                    ,ArticleAdmin
                     )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('catename',)
