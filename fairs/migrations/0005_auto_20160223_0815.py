# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fairs', '0004_auto_20160203_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='fair',
            name='image_de',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Bild'),
        ),
        migrations.AddField(
            model_name='fair',
            name='image_en',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Bild'),
        ),
        migrations.AddField(
            model_name='fair',
            name='image_ru',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Bild'),
        ),
    ]
