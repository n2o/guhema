# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-24 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_tooth_diameter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Kennziffer')),
                ('teeth', models.ManyToManyField(to='products.Tooth')),
            ],
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_2301',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_2301_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_2302',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_2302_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_2352',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_2352_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_2402',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_2402_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_3302',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_3302_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_3352',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_3352_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_3354',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_3354_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_3402',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_3402_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_3404',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_3404_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_3454',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_3454_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4354',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4354_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4356',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4356_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4404',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4404_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4406',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4406_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4409',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4409_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4451',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4451_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4454',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4454_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4456',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4456_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4459',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4459_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4476',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4476_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4501',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4501_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4509',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4509_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4551',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4551_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4559',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_4559_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5501',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5501_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5504',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5504_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5551',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5551_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5554',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5554_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5571',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5571_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5574',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5574_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5604',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5604_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5628',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5628_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5654',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5654_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5704',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5704_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5707',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_5707_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_6658',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_6658_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_6708',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_6708_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_6758',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_6758_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_6801',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_6801_hss',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_6954',
        ),
        migrations.RemoveField(
            model_name='sawblade',
            name='ind_6954_hss',
        ),
        migrations.AddField(
            model_name='sawblade',
            name='indicators',
            field=models.ManyToManyField(to='products.Indicator'),
        ),
    ]