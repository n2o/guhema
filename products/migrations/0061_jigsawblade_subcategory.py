# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0060_jigsawblade'),
    ]

    operations = [
        migrations.AddField(
            model_name='jigsawblade',
            name='subcategory',
            field=models.CharField(blank=True, max_length=255, verbose_name='Unterkategorie'),
        ),
    ]