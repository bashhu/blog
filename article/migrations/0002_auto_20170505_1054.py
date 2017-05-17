# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_time'], 'permissions': (('reader', 'Can read blog'), ('worker', 'Can change blog'), ('assessor', 'Can assessor blog'), ('master', 'Can manager'))},
        ),
    ]
