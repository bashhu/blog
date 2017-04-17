# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cmd_name', models.CharField(max_length=100)),
                ('cmd_cate', models.CharField(max_length=50, blank=True)),
                ('etime', models.DateTimeField(auto_now_add=True)),
                ('salt_mod', models.CharField(max_length=50)),
                ('salt_parm', models.CharField(max_length=50, null=True)),
                ('cmd_res', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-etime'],
            },
        ),
    ]
