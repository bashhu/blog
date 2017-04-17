# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_command_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='command_log',
            name='cmd_reson',
            field=models.TextField(null=True, blank=True),
        ),
    ]
