# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ES',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project', models.CharField(max_length=50)),
                ('es_ip', models.CharField(max_length=100)),
                ('es_port', models.CharField(default=9200, max_length=5)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-ctime'],
            },
        ),
    ]
