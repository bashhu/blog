# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_command_log_cmd_reson'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='salt_host',
            field=models.CharField(default=datetime.datetime(2017, 4, 13, 8, 55, 39, 291000, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='command_log',
            name='salt_host',
            field=models.CharField(default=datetime.datetime(2017, 4, 13, 8, 55, 52, 283000, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
