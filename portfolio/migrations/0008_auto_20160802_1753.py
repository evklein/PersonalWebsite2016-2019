# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20160802_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='screenshot_url_2',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='screenshot_url_3',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='screenshot_url_4',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='screenshot_url_5',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='store_logo_url',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='store_url',
            field=models.CharField(default='null', max_length=300),
        ),
    ]