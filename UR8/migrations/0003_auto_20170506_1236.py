# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 12:36
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UR8', '0002_video_thumpnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='dislikedBy',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), null=True, size=None),
        ),
        migrations.AddField(
            model_name='video',
            name='likedBy',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), null=True, size=None),
        ),
        migrations.AddField(
            model_name='video',
            name='rated1',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), null=True, size=None),
        ),
        migrations.AddField(
            model_name='video',
            name='rated2',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), null=True, size=None),
        ),
        migrations.AddField(
            model_name='video',
            name='rated3',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), null=True, size=None),
        ),
        migrations.AddField(
            model_name='video',
            name='rated4',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), null=True, size=None),
        ),
        migrations.AddField(
            model_name='video',
            name='rated5',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), null=True, size=None),
        ),
    ]
