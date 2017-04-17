# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20170414_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='command_log',
            old_name='cmd_cate',
            new_name='salt_cate',
        ),
        migrations.RenameField(
            model_name='command_log',
            old_name='cmd_name',
            new_name='salt_name',
        ),
        migrations.RenameField(
            model_name='command_log',
            old_name='cmd_reason',
            new_name='salt_reason',
        ),
        migrations.RenameField(
            model_name='command_log',
            old_name='cmd_res',
            new_name='salt_res',
        ),
    ]
