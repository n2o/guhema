# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_hacksawblade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sawblade',
            old_name='name',
            new_name='quality',
        ),
    ]
