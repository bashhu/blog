#coding:utf-8
from django.contrib import admin
from article.models import Article,Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time')
admin.site.register(Article
                    ,ArticleAdmin
                     )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('catename',)
admin.site.register(Category,
                    CategoryAdmin
                     )