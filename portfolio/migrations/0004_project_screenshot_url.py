# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project_technologies_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='screenshot_url',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
