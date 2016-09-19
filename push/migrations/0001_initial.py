# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-19 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crawler_id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('identification_number', models.IntegerField()),
                ('urls', models.CharField(max_length=200)),
                ('extra_data_1', models.CharField(max_length=100)),
                ('extra_data_2', models.CharField(max_length=100)),
                ('extra_data_3', models.CharField(max_length=100)),
            ],
        ),
    ]
