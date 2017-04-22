#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.contrib import admin
from models import Question,Choice,Userinfo
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)

admin.site.register(Userinfo)