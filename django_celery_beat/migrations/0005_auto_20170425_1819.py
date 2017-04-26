# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0004_auto_20170221_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodictask',
            name='one_off',
            field=models.BooleanField(default=False, verbose_name='one-off task'),
        ),
        migrations.AddField(
            model_name='periodictask',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start_date'),
        ),
    ]
