# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'permissions': (('open_discussion', 'Can create a discussion'), ('reply_discussion', 'Can reply discussion'), ('close_discussion', 'Can remove a discussion by setting its status as closed'))},
        ),
    ]
