# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 19:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20151204_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sawblade',
            name='clamping',
        ),
    ]