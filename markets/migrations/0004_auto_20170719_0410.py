# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0003_auto_20170711_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]