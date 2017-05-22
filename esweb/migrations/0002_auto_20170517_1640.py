# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('esweb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='es',
            old_name='es_ip',
            new_name='ip',
        ),
        migrations.RenameField(
            model_name='es',
            old_name='es_port',
            new_name='port',
        ),
        migrations.AddField(
            model_name='es',
            name='hostname',
            field=models.CharField(default=datetime.datetime(2017, 5, 17, 8, 40, 42, 679000, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
