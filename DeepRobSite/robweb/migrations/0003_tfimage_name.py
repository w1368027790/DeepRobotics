# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robweb', '0002_auto_20161222_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='tfimage',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
