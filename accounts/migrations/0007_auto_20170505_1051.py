# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20170505_1044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'permissions': (('guest', 'Can access public msg'), ('user', 'Can access private msg'), ('admin', 'all privilege'))},
        ),
    ]
