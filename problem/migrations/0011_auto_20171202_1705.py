# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-02 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import problem.models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0010_auto_20171002_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='alias',
            field=models.CharField(blank=True, max_length=64, validators=[problem.models.AliasValidator()], verbose_name='Alias'),
        ),
    ]
