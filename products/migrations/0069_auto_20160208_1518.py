# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0068_auto_20160203_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holesaw',
            name='pilot_drill_length',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Zentrierbohrerlänge (in mm)'),
        ),
        migrations.AlterField(
            model_name='holesaw',
            name='saw_length',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Lochsägenlänge (in mm)'),
        ),
    ]
