# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160429_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopitem',
            name='item_file',
            field=models.CharField(default=5, max_length=100),
            preserve_default=False,
        ),
    ]
