# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0077_auto_20160217_0649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sawblade',
            name='image_de',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='image_en',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='image_ru',
        ),
        migrations.AddField(
            model_name='clamping',
            name='image_de',
            field=models.ImageField(blank=True, null=True, upload_to='blades/', verbose_name='Bild'),
        ),
        migrations.AddField(
            model_name='clamping',
            name='image_en',
            field=models.ImageField(blank=True, null=True, upload_to='blades/', verbose_name='Bild'),
        ),
        migrations.AddField(
            model_name='clamping',
            name='image_ru',
            field=models.ImageField(blank=True, null=True, upload_to='blades/', verbose_name='Bild'),
        ),
    ]
