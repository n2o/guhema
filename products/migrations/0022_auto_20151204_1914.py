# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_remove_sawblade_clamping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sawblade',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Clamping', verbose_name='Aufnahme'),
        ),
    ]
