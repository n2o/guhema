# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0056_auto_20160118_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='bandsawbladeindicator',
            name='AE',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ä'),
        ),
        migrations.AddField(
            model_name='bandsawbladeindicator',
            name='F',
            field=models.CharField(blank=True, max_length=255, verbose_name='F'),
        ),
        migrations.AddField(
            model_name='bandsawbladeindicator',
            name='RP',
            field=models.CharField(blank=True, max_length=255, verbose_name='RP'),
        ),
        migrations.AddField(
            model_name='bandsawbladeindicator',
            name='S',
            field=models.CharField(blank=True, max_length=255, verbose_name='S'),
        ),
        migrations.AddField(
            model_name='bandsawbladeindicator',
            name='SP',
            field=models.CharField(blank=True, max_length=255, verbose_name='SP'),
        ),
        migrations.AddField(
            model_name='bandsawbladeindicator',
            name='TP',
            field=models.CharField(blank=True, max_length=255, verbose_name='TP'),
        ),
        migrations.AddField(
            model_name='bandsawbladeindicator',
            name='UE',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ü'),
        ),
        migrations.AddField(
            model_name='bandsawbladeindicator',
            name='UP',
            field=models.CharField(blank=True, max_length=255, verbose_name='UP'),
        ),
        migrations.AddField(
            model_name='bandsawbladeindicator',
            name='VP',
            field=models.CharField(blank=True, max_length=255, verbose_name='VP'),
        ),
        migrations.AddField(
            model_name='bandsawbladeindicator',
            name='WP',
            field=models.CharField(blank=True, max_length=255, verbose_name='WP'),
        ),
        migrations.AddField(
            model_name='bandsawbladeindicator',
            name='star_p',
            field=models.CharField(blank=True, max_length=255, verbose_name='*P'),
        ),
    ]
