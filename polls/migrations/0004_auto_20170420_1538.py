# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(upload_to=b'upload/pic'),
        ),
    ]
