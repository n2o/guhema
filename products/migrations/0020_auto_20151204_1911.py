# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20151204_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sawblade',
            name='clamping_img',
        ),
        migrations.AddField(
            model_name='clamping',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Bild'),
        ),
    ]