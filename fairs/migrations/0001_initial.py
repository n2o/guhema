# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 16:02
from __future__ import unicode_literals

import datetime

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name der Messe')),
                ('location', models.TextField(blank=True, verbose_name='Veranstaltungsort')),
                ('hall', models.CharField(blank=True, max_length=50, verbose_name='Halle')),
                ('stand', models.CharField(blank=True, max_length=50, verbose_name='Stand')),
                ('start', models.DateTimeField(default=datetime.datetime.now, verbose_name='Beginn')),
                ('end', models.DateTimeField(default=datetime.datetime.now, verbose_name='Ende')),
                ('description', models.TextField(blank=True, verbose_name='Beschreibung')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Bild')),
                ('attachment', models.FileField(blank=True, null=True, upload_to='', verbose_name='Anhang')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title')),
                ('archive', models.BooleanField(default=False, verbose_name='Archiviert?')),
                ('public', models.BooleanField(default=True, verbose_name='Öffentlich?')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Erstellt am')),
            ],
            options={
                'verbose_name_plural': 'Messen',
                'ordering': ('created',),
                'verbose_name': 'Messe',
            },
        ),
    ]
