# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20151204_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sawblade',
            name='quality',
            field=models.CharField(blank=True, max_length=255, verbose_name='Qualität'),
        ),
    ]