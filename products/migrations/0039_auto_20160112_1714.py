# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0038_auto_20160112_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sablesawblade',
            name='accessory',
        ),
        migrations.RemoveField(
            model_name='sablesawblade',
            name='ordernumber',
        ),
        migrations.AddField(
            model_name='hacksawblade',
            name='accessory',
            field=models.BooleanField(default=False, verbose_name='Zubehörartikel?'),
        ),
        migrations.AddField(
            model_name='hacksawblade',
            name='ordernumber',
            field=models.CharField(blank=True, max_length=255, verbose_name='Bestellnr.'),
        ),
    ]
