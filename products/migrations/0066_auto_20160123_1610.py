# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0065_auto_20160123_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='hacksawblade',
            name='subcategory',
            field=models.CharField(blank=True, max_length=255, verbose_name='Unterkategorie'),
        ),
        migrations.AlterField(
            model_name='bandsawblade',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='blades/', verbose_name='2. Produktabbildung'),
        ),
        migrations.AlterField(
            model_name='clamping',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blades/', verbose_name='Bild'),
        ),
        migrations.AlterField(
            model_name='holesaw',
            name='image',
            field=models.ImageField(blank=True, upload_to='blades/', verbose_name='Abbildung'),
        ),
        migrations.AlterField(
            model_name='productgroup',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blades/', verbose_name='Produktabbildung'),
        ),
        migrations.AlterField(
            model_name='sawblade',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blades/', verbose_name='Produktabbildung'),
        ),
    ]