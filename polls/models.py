#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models
import os,hashlib
from django.utils import timezone
import datetime
# Create your models here.
def attachment_path(instance, filename):
    now = datetime.datetime.now()
    suffix = os.path.splitext(filename)[1]
    md5 = hashlib.md5(now.strftime("%Y%m%d%H%M%S") + filename)
    return "db_job/%s/%s%s" % (now.strftime("%Y%m%d"), md5.hexdigest(), suffix)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '近期发布'

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question_text =  models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Userinfo(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='upload/pic')
    pub_key = models.FileField(upload_to=attachment_path)

    def __str__(self):
        return self.name