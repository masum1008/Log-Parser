# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_formats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logformats',
            name='log_format',
            field=models.CharField(max_length=100),
        ),
    ]