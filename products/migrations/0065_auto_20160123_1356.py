# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0064_auto_20160123_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circularsawbladeindicator',
            name='BW_3',
            field=models.IntegerField(blank=True, default=0, verbose_name='BW 3 mm'),
        ),
        migrations.AlterField(
            model_name='circularsawbladeindicator',
            name='BW_4',
            field=models.IntegerField(blank=True, default=0, verbose_name='BW 4 mm'),
        ),
        migrations.AlterField(
            model_name='circularsawbladeindicator',
            name='BW_7',
            field=models.IntegerField(blank=True, default=0, verbose_name='BW 7 mm'),
        ),
        migrations.AlterField(
            model_name='circularsawbladeindicator',
            name='HZ_10',
            field=models.IntegerField(blank=True, default=0, verbose_name='HZ 10 mm'),
        ),
        migrations.AlterField(
            model_name='circularsawbladeindicator',
            name='HZ_12',
            field=models.IntegerField(blank=True, default=0, verbose_name='HZ 12 mm'),
        ),
        migrations.AlterField(
            model_name='circularsawbladeindicator',
            name='HZ_14',
            field=models.IntegerField(blank=True, default=0, verbose_name='HZ 14 mm'),
        ),
        migrations.AlterField(
            model_name='circularsawbladeindicator',
            name='HZ_5',
            field=models.IntegerField(blank=True, default=0, verbose_name='HZ 5 mm'),
        ),
        migrations.AlterField(
            model_name='circularsawbladeindicator',
            name='HZ_6',
            field=models.IntegerField(blank=True, default=0, verbose_name='HZ 6 mm'),
        ),
        migrations.AlterField(
            model_name='circularsawbladeindicator',
            name='HZ_8',
            field=models.IntegerField(blank=True, default=0, verbose_name='HZ 8 mm'),
        ),
        migrations.AlterField(
            model_name='circularsawbladeindicator',
            name='HZ_9',
            field=models.IntegerField(blank=True, default=0, verbose_name='HZ 9 mm'),
        ),
    ]
