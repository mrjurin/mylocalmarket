# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-21 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0005_auto_20170721_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='website',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
