# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-24 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tooth',
            name='diameter',
            field=models.FloatField(default=0.0, verbose_name='Durchmesser'),
        ),
    ]
