# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 07:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20170314_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedetail',
            name='release_time',
            field=models.DateField(blank=True, default=datetime.date(2017, 3, 14), null=True),
        ),
    ]
