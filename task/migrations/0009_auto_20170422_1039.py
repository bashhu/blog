# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_command_log_task_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crontab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('con_name', models.CharField(max_length=100)),
                ('con_cate', models.CharField(max_length=50, blank=True)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('con_cmd', models.CharField(max_length=250)),
                ('con_time', models.CharField(max_length=250)),
                ('con_user', models.CharField(max_length=50)),
                ('utime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-ctime'],
            },
        ),
        migrations.AlterField(
            model_name='command_log',
            name='task_id',
            field=models.IntegerField(),
        ),
    ]
