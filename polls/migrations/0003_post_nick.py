# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20161213_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nick',
            field=models.CharField(default='admin', max_length=50),
        ),
    ]