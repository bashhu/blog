# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20170413_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='command_log',
            old_name='cmd_reson',
            new_name='cmd_reason',
        ),
    ]
