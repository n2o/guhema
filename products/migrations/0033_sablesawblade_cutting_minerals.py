# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20160102_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='sablesawblade',
            name='cutting_minerals',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Schnittbereich Mineralisch'),
        ),
    ]