# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0014_auto_20170103_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawldata',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 7, 13, 35, 35, 644992)),
        ),
        migrations.AlterField(
            model_name='crawldata',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
