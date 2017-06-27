# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_project_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='screenshot_url',
            new_name='screenshot_url_1',
        ),
        migrations.AddField(
            model_name='project',
            name='screenshot_url_2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='screenshot_url_3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='screenshot_url_4',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='screenshot_url_5',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]