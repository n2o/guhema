# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-24 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20151124_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='length',
            field=models.FloatField(blank=True, default=0, verbose_name='Länge'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='strength',
            field=models.FloatField(blank=True, default=0, verbose_name='Stärke'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='width',
            field=models.FloatField(blank=True, default=0, verbose_name='Breite'),
        ),
    ]
