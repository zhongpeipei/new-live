# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieDetail',
            fields=[
                ('create_time', models.TimeField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('release_time', models.CharField(max_length=50, null=True)),
                ('about', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('tag', models.CharField(max_length=100, null=True)),
                ('status', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'movie_detail',
            },
        ),
        migrations.CreateModel(
            name='MovieDownloadUrl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_id', models.IntegerField()),
                ('download_url', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'movie_download_url',
            },
        ),
        migrations.CreateModel(
            name='MovieImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_id', models.IntegerField()),
                ('image', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'movie_images',
            },
        ),
    ]
