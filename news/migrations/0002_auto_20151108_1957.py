# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-08 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Anhang'),
        ),
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Bild'),
        ),
    ]
