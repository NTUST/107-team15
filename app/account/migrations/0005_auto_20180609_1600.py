# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cart',
            field=models.ManyToManyField(blank=True, to='post.Commodity'),
        ),
    ]
