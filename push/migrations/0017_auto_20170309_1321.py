# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-09 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0016_auto_20170309_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawldata',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
