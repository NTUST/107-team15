# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_remove_commodity_ranker'),
        ('account', '0003_auto_20180528_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cart',
            field=models.ManyToManyField(to='post.Commodity'),
        ),
    ]
