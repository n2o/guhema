# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 11:55
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20160102_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='SableSawBlade',
            fields=[
                ('sawblade_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.SawBlade')),
                ('toothing', models.IntegerField(blank=True, verbose_name='Verzahnung')),
                ('cutting_metal', models.CharField(blank=True, max_length=255, verbose_name='Schnittbereich Metall')),
                ('cutting_wood', models.CharField(blank=True, max_length=255, verbose_name='Schnittbereich Holz')),
            ],
            options={
                'verbose_name': 'Säbelsägeblatt',
                'verbose_name_plural': 'Säbelsägeblätter',
            },
            bases=('products.sawblade',),
        ),
    ]
