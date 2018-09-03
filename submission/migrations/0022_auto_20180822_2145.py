# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-22 21:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('submission', '0021_auto_20180717_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrintCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('generated_pdf', models.TextField(blank=True)),
                ('pages', models.PositiveIntegerField(default=1)),
                ('status', models.IntegerField(choices=[(-1, 'Processing'), (0, 'OK'), (1, 'Failed')], default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='PrintManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.PositiveIntegerField(default=50)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='printcode',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submission.PrintManager'),
        ),
        migrations.AddField(
            model_name='printcode',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]