# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0076_auto_20160212_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='sawblade',
            name='image_de',
            field=models.ImageField(blank=True, null=True, upload_to='blades/', verbose_name='Produktabbildung'),
        ),
        migrations.AddField(
            model_name='sawblade',
            name='image_en',
            field=models.ImageField(blank=True, null=True, upload_to='blades/', verbose_name='Produktabbildung'),
        ),
        migrations.AddField(
            model_name='sawblade',
            name='image_ru',
            field=models.ImageField(blank=True, null=True, upload_to='blades/', verbose_name='Produktabbildung'),
        ),
    ]
