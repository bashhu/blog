# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cmd_cate',
        ),
        migrations.RemoveField(
            model_name='user',
            name='salt_host',
        ),
        migrations.RemoveField(
            model_name='user',
            name='salt_mod',
        ),
        migrations.RemoveField(
            model_name='user',
            name='salt_parm',
        ),
        migrations.RemoveField(
            model_name='user',
            name='salt_parm_c',
        ),
    ]
