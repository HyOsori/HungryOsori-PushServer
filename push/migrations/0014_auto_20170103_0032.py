# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0013_auto_20170102_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawldata',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 3, 0, 32, 40, 152748)),
        ),
    ]
