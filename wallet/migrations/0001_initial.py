# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='wrecodde', max_length=25)),
                ('email', models.EmailField(default='wrecodde@gmail.com', max_length=254)),
                ('password', models.CharField(default='decodded', max_length=45)),
            ],
        ),
    ]
