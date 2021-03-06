# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_sensitivewords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviedownloadurl',
            name='movie_id',
        ),
        migrations.RemoveField(
            model_name='movieimages',
            name='movie_id',
        ),
        migrations.AddField(
            model_name='moviedownloadurl',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.MovieDetail'),
        ),
        migrations.AddField(
            model_name='movieimages',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.MovieDetail'),
        ),
        migrations.AlterField(
            model_name='moviedetail',
            name='release_time',
            field=models.DateTimeField(null=True),
        ),
    ]
