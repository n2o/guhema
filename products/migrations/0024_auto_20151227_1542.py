# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20151222_1853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sawblade',
            options={'verbose_name': 'Sägeblatt', 'verbose_name_plural': 'Sägeblätter'},
        ),
        migrations.AlterField(
            model_name='sawblade',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Clamping', verbose_name='Aufnahme'),
        ),
    ]