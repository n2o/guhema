# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 18:53
from __future__ import unicode_literals

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_sawblade_clamping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clamping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name')),
            ],
        ),
        migrations.AlterField(
            model_name='sawblade',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Aufnahme', to='products.Clamping'),
        ),
    ]
