# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-19 14:29
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('endorsement', models.PositiveSmallIntegerField(default=0, help_text='Please specify the amount of Achiever Points that will be rewarded on completion')),
                ('task_description', models.CharField(default='', help_text='Please provide a short description of the task.', max_length=250)),
                ('motivation', models.CharField(default='', help_text='Please provide the motivation behind the task.', max_length=250)),
                ('time_estimate', models.DurationField(default=0, help_text='Please specify how long the task is estimated to take.')),
                ('additional_information', models.TextField(blank=True, help_text="Please provide additional information that can help understanding the task's breadth and stakes", max_length=1000)),
                ('attachments', models.FileField(blank=True, upload_to='uploads/')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 19, 16, 29, 4, 476407))),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
