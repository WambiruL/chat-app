# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-27 20:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20210727_2300'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['date_created']},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='date',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(),
        ),
    ]
