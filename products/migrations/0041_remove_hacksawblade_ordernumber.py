# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 17:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0040_auto_20160112_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hacksawblade',
            name='ordernumber',
        ),
    ]
