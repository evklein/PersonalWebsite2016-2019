# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20160801_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='technologies_used',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
