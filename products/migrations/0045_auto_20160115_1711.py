# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0044_auto_20160115_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='holesaw',
            name='quality',
            field=models.CharField(blank=True, max_length=255, verbose_name='Stahlsorte'),
        ),
        migrations.AddField(
            model_name='holesaw',
            name='toothing',
            field=models.CharField(blank=True, max_length=255, verbose_name='Verzahnung'),
        ),
    ]
