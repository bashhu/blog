# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20170414_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='command_log',
            old_name='salt_cate',
            new_name='cmd_cate',
        ),
        migrations.RenameField(
            model_name='command_log',
            old_name='salt_name',
            new_name='cmd_name',
        ),
    ]
