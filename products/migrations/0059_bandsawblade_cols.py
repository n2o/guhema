# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0058_bandsawblade_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='bandsawblade',
            name='cols',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Spalten'),
        ),
    ]
