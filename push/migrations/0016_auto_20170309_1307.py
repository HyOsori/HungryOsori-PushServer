# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-09 04:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0015_auto_20170307_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crawldata',
            name='extra_data_1',
        ),
        migrations.RemoveField(
            model_name='crawldata',
            name='extra_data_2',
        ),
        migrations.RemoveField(
            model_name='crawldata',
            name='extra_data_3',
        ),
        migrations.RemoveField(
            model_name='crawldata',
            name='identification_number',
        ),
        migrations.AlterField(
            model_name='crawldata',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 9, 13, 7, 6, 346040)),
        ),
    ]
