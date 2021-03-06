# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-24 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20151124_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tooth',
            name='diameter',
        ),
        migrations.AddField(
            model_name='indicator',
            name='diameter',
            field=models.FloatField(default=0.0, verbose_name='Durchmesser'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='hss',
            field=models.BooleanField(default=False, verbose_name='HSS?'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='teeth',
            field=models.ManyToManyField(blank=True, to='products.Tooth'),
        ),
    ]
