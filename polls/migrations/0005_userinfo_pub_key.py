# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170420_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='pub_key',
            field=models.FileField(default=1, upload_to=b'upload/key'),
            preserve_default=False,
        ),
    ]
