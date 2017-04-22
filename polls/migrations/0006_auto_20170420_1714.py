# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_userinfo_pub_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='pub_key',
            field=models.FileField(upload_to=polls.models.attachment_path),
        ),
    ]
