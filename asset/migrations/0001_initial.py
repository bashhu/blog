# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdcAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idc_name', models.CharField(max_length=20, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('idc_type', models.CharField(max_length=20, verbose_name='\u673a\u623f\u7c7b\u578b')),
                ('idc_location', models.CharField(max_length=30, verbose_name='\u673a\u623f\u4f4d\u7f6e')),
                ('contract_date', models.DateTimeField(verbose_name='\u5408\u540c\u5230\u671f\u65f6\u95f4', blank=True)),
                ('idc_contacts', models.CharField(max_length=30, verbose_name='\u673a\u623f\u503c\u73ed\u7535\u8bdd')),
                ('business_contacts', models.CharField(default=b'', max_length=30, verbose_name='\u5546\u52a1\u8054\u7cfb\u4eba')),
                ('service_contacts', models.CharField(default=b'', max_length=30, verbose_name='\u5ba2\u670d\u8054\u7cfb\u4eba')),
                ('remark', models.TextField(default=b'', max_length=50, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u673a\u623f\u7ba1\u7406',
                'verbose_name_plural': '\u673a\u623f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(default=b'', max_length=50, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.CharField(unique=True, max_length=50, verbose_name='IP\u5730\u5740')),
                ('manufacturer', models.CharField(default=b'', max_length=50, verbose_name='\u5382\u5546', blank=True)),
                ('productname', models.CharField(max_length=50, verbose_name='\u4ea7\u54c1\u578b\u53f7')),
                ('service_tag', models.CharField(max_length=80, verbose_name='\u5e8f\u5217\u53f7')),
                ('cpu_model', models.CharField(max_length=50, verbose_name='CPU\u578b\u53f7')),
                ('cpu_nums', models.PositiveSmallIntegerField(verbose_name='CPU\u7ebf\u7a0b\u6570')),
                ('cpu_groups', models.PositiveSmallIntegerField(verbose_name='CPU\u7269\u7406\u6838\u6570')),
                ('mem', models.CharField(max_length=5, verbose_name='\u5185\u5b58\u5927\u5c0f')),
                ('os', models.CharField(max_length=50, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('virtual', models.CharField(max_length=50, verbose_name='\u4e3b\u673a\u7c7b\u578b')),
                ('salt_control', models.BooleanField(default=False, verbose_name='\u662f\u5426Salt\u6258\u7ba1')),
                ('status', models.CharField(default=b'up', max_length=16, verbose_name='\u8282\u70b9\u72b6\u6001', choices=[(b'up', b'\xe6\xad\xa3\xe5\xb8\xb8\xe8\xbf\x90\xe8\xa1\x8c'), (b'down', b'\xe5\xb7\xb2\xe5\x85\xb3\xe9\x97\xad')])),
            ],
            options={
                'db_table': 'machine',
                'verbose_name': '\u4e3b\u673a\u7ba1\u7406',
                'verbose_name_plural': '\u4e3b\u673a\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='MachineGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u4e3b\u673a\u7ec4\u540d\u79f0')),
                ('remark', models.TextField(default=b'', max_length=50, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'db_table': 'machine_group',
                'verbose_name': '\u4e3b\u673a\u5206\u7ec4',
                'verbose_name_plural': '\u4e3b\u673a\u5206\u7ec4',
            },
        ),
        migrations.CreateModel(
            name='NetworkAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=20, verbose_name='IP\u5730\u5740')),
                ('hostname', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='\u5382\u5546')),
                ('productname', models.CharField(max_length=20, verbose_name='\u4ea7\u54c1\u578b\u53f7')),
                ('idc_jg', models.CharField(max_length=10, verbose_name='\u673a\u67dc\u7f16\u53f7', blank=True)),
                ('service_tag', models.CharField(unique=True, max_length=30, verbose_name='\u5e8f\u5217\u53f7')),
                ('remark', models.TextField(default=b'', max_length=50, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u7f51\u7edc\u8bbe\u5907',
                'verbose_name_plural': '\u7f51\u7edc\u8bbe\u5907',
            },
        ),
        migrations.CreateModel(
            name='ServiceGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u4e1a\u52a1\u670d\u52a1\u7ec4\u540d\u79f0')),
                ('remark', models.TextField(default=b'', max_length=50, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'db_table': 'service_group',
                'verbose_name': '\u4e1a\u52a1\u670d\u52a1\u5206\u7ec4',
                'verbose_name_plural': '\u4e1a\u52a1\u670d\u52a1\u5206\u7ec4',
            },
        ),
        migrations.AddField(
            model_name='machine',
            name='m_group',
            field=models.ForeignKey(verbose_name='\u4e3b\u673a\u5206\u7ec4', blank=True, to='asset.MachineGroup'),
        ),
        migrations.AddField(
            model_name='machine',
            name='s_group',
            field=models.ManyToManyField(to='asset.ServiceGroup', null=True, verbose_name='\u4e1a\u52a1\u670d\u52a1\u7ec4', blank=True),
        ),
    ]
