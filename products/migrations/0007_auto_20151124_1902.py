# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-24 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20151124_1732'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tooth',
        ),
        migrations.AlterModelOptions(
            name='indicator',
            options={'ordering': ('value',), 'verbose_name': 'Kennziffer', 'verbose_name_plural': 'Kennziffer'},
        ),
        migrations.AlterModelOptions(
            name='sawblade',
            options={'verbose_name': 'Maschinensägeblatt', 'verbose_name_plural': 'Maschinensägeblätter'},
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='number',
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='teeth',
        ),
        migrations.AddField(
            model_name='indicator',
            name='value',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Kennziffer'),
        ),
        migrations.AlterField(
            model_name='sawblade',
            name='indicators',
            field=models.ManyToManyField(to='products.Indicator', verbose_name='Kennziffern'),
        ),
    ]
