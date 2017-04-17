# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20170414_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='command_log',
            name='task_id',
            field=models.IntegerField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
