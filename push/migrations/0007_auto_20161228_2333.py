# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0006_auto_20161228_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawldata',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 28, 23, 33, 54, 451445)),
        ),
    ]
