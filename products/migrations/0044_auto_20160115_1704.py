# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0043_holesaw'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoleSawDiameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diameter', models.IntegerField(verbose_name='Durchmesser in mm')),
            ],
            options={
                'verbose_name_plural': 'Durchmesser',
                'verbose_name': 'Durchmesser',
            },
        ),
        migrations.AddField(
            model_name='holesaw',
            name='diameter',
            field=models.ManyToManyField(to='products.HoleSawDiameter', verbose_name='Durchmesser in mm'),
        ),
    ]
