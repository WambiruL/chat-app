# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-27 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=300),
        ),
    ]
