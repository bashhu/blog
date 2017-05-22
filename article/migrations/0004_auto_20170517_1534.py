# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20170505_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default=datetime.datetime(2017, 5, 17, 7, 34, 6, 513000, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
