# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0061_jigsawblade_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='jigsawblade',
            name='length',
            field=models.IntegerField(blank=True, default=0, max_length=255, verbose_name='Sägeblattlänge (in mm)'),
        ),
        migrations.AlterField(
            model_name='jigsawblade',
            name='cutting_metal',
            field=models.CharField(blank=True, max_length=255, verbose_name='Schnittbereich Metall (in mm)'),
        ),
        migrations.AlterField(
            model_name='jigsawblade',
            name='cutting_wood',
            field=models.CharField(blank=True, max_length=255, verbose_name='Schnittbereich Holz (in mm)'),
        ),
    ]
