# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 15:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20151227_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sawblade',
            old_name='quality',
            new_name='type',
        ),
    ]
